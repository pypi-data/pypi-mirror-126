import enum
import shutil
from abc import ABC, abstractmethod, ABCMeta
from inspect import getsourcefile
from pathlib import Path
import subprocess
from typing import List, Tuple

from .exit_codes import ExitCodeEventType, USED_EXIT_CODES, SYSTEM_RESERVED_EXIT_CODES
from .shell import ShellCommand, ShellError
from .test_helper_formatter import get_formatted_test_helper
from .testcase_io import TestCaseIO
from .testcase_result_validator import generate_validating_string, validate_output
from ..config_manager import GradingConfig


class SourceDirSaver(ABCMeta, type):
    """Useful in getting the resources associated with each testcase type"""

    type_source_file: Path

    def __new__(mcs, name, bases, dct):
        cls = super().__new__(mcs, name, bases, dct)
        # We needed a way to get a source file based solely on __class__ to access its sibling directories
        source_file = getsourcefile(cls)
        if source_file is None:
            raise FileNotFoundError(f"Source file for class {cls} has not been found.")
        cls.type_source_file = Path(source_file)
        return cls


class TestCase(ABC, metaclass=SourceDirSaver):
    source_suffix = ".source_suffix"  # dummy value
    executable_suffix = ".executable_suffix"  # dummy value

    type_source_file: Path
    test_helpers_dir: Path
    path: Path
    weight: float
    max_score: int
    io: TestCaseIO
    validating_string: str

    config: GradingConfig

    # Note that this structure will not work for any children of this class until 3.9
    # because classmethod does not wrap property correctly until then.
    # See https://bugs.python.org/issue19072
    @classmethod
    @property
    @abstractmethod
    def helper_module(cls) -> str:
        pass

    @classmethod
    @abstractmethod
    def is_installed(cls) -> bool:
        """Returns True if software necessary to run the testcase is installed on the system"""

    @classmethod
    def get_template_dir(cls):
        return cls.type_source_file.parent / "templates"

    @abstractmethod
    def compile_testcase(self, precompiled_submission: Path, cli_args: str) -> ShellCommand:
        """Compiles student submission and testcase into a single executable
        (or simply returns the command to run the testcase if no further compilation is necessary)

        pwd = temp/student_dir
        """

    def __init__(
        self,
        path: Path,
        timeout: float,
        weight: float,
        testcase_precompilation_args: str,
        io: TestCaseIO,
        config: GradingConfig,
    ):
        self.test_helpers_dir = self.type_source_file.parent / "helpers"
        self.path = path
        self.timeout = timeout
        self.weight = weight
        self.max_score = int(weight * 100)

        self.name = path.name

        self.io = io
        self.validating_string = generate_validating_string()

        self.config = config

        self.prepend_test_helper()
        self.precompile_testcase(testcase_precompilation_args)

    @classmethod
    def precompile_submission(
        cls,
        submission: Path,
        student_dir: Path,
        possible_source_file_stems: List[str],
        cli_args: str,
        config: GradingConfig,
    ) -> Path:
        """Copies student submission into student_dir and either precompiles
        it and returns the path to the precompiled submission or to the
        copied submission if no precompilation is necessary

        pwd = temp/student_dir
        """
        destination = (student_dir / possible_source_file_stems[0]).with_suffix(cls.source_suffix)
        shutil.copy(str(submission), str(destination))
        return destination

    def precompile_testcase(self, cli_args: str):
        """Replaces the original testcase file with its compiled version,
        thus making reading its contents as plaintext harder.
        Useful in preventing cheating.

        pwd = AutograderPaths.current_dir (i.e. the directory with all submissions)
        """

    @classmethod
    def run_additional_testcase_operations_in_student_dir(cls, student_dir: Path):
        """Do nothing by default"""
        pass

    @classmethod
    def is_a_type_of(cls, file: Path, possible_source_file_stems: List[str]) -> bool:
        return file.suffix == cls.source_suffix

    def get_path_to_helper_module(self) -> Path:
        return self.test_helpers_dir / self.helper_module

    def run(
        self, precompiled_submission: Path, testcase_compilation_args: str, testcase_runtime_args: str
    ) -> Tuple[float, str]:
        """Returns student score and message to be displayed"""
        result, message = self._weightless_run(precompiled_submission, testcase_compilation_args, testcase_runtime_args)

        self.delete_executable_files(precompiled_submission)
        return result * self.weight, message

    def make_executable_path(self, submission: Path) -> Path:
        """By combining test name and student name, it makes a unique path"""
        return submission.with_name(self.path.stem + submission.stem + self.executable_suffix)

    def prepend_test_helper(self):
        """Prepends all of the associated test_helper code to test code

        pwd = AutograderPaths.current_dir (i.e. the directory with all submissions)
        """
        with self.path.open() as f:
            content = f.read()
            final_content = self.get_formatted_test_helper() + "\n" + content
        with self.path.open("w") as f:
            f.write(final_content)

    def get_formatted_test_helper(self, **exta_format_kwargs) -> str:
        return get_formatted_test_helper(self.get_path_to_helper_module(), **exta_format_kwargs)

    def delete_executable_files(self, precompiled_submission: Path):
        path = self.make_executable_path(precompiled_submission)
        if path.exists():
            path.unlink()

    def delete_source_file(self, source_path: Path):
        if source_path.exists():
            source_path.unlink()

    def _weightless_run(
        self,
        precompiled_submission: Path,
        testcase_compilation_args: str,
        testcase_runtime_args: str,
    ) -> Tuple[float, str]:
        """Returns student score (without applying testcase weight) and message to be displayed"""
        testcase_copy_in_student_dir = precompiled_submission.with_name(self.path.name)
        shutil.copy(str(self.path), str(testcase_copy_in_student_dir))

        try:
            test_executable = self.compile_testcase(precompiled_submission, testcase_compilation_args)
        except ShellError as e:
            return 0, e.format("Failed to compile")
        self.delete_source_file(testcase_copy_in_student_dir)
        try:
            result = test_executable(
                *testcase_runtime_args.split(),
                input=self.io.input,
                timeout=self.timeout,
                env={"VALIDATING_STRING": self.validating_string},
                allowed_exit_codes=USED_EXIT_CODES,
            )
            exit_code = result.returncode
        except subprocess.TimeoutExpired:
            return 0, "Exceeded Time Limit"
        except ShellError as e:
            return 0, f"Crashed due to signal {e.returncode}:\n{e.stderr}\n"
        raw_output = result.stdout
        output, score, output_is_valid = validate_output(raw_output, self.validating_string)
        if not output_is_valid:
            # This  means that either the student used built-in exit function himself
            # or some testcase helper is broken, or a testcase exits itself without
            # the use of helper functions.
            return (
                0,
                "None of the helper functions have been called.\n"
                f"Instead, exit() has been called with exit_code {exit_code}.\n"
                "It could indicate student cheating or testcase_utils being written incorrectly.",
            )
        elif exit_code == ExitCodeEventType.CHECK_STDOUT:
            if self.io.expected_output_equals(output):
                return 100, f"{int(100 * self.weight)}/{self.max_score}"
            else:
                return 0, f"0/{self.max_score} (Wrong output)"
        elif exit_code == ExitCodeEventType.RESULT:
            message = f"{round(score * self.weight, 2)}/{self.max_score}"
            if score == 0:
                message += " (Wrong answer)"
            return score, message
        elif exit_code in SYSTEM_RESERVED_EXIT_CODES or exit_code < 0:
            # We should already handle this case in try, except block. Maybe we need more info in the error?
            raise NotImplementedError(f"System error with exit code {exit_code} has not been handled.")
        else:
            raise ValueError(f"Unknown system code {exit_code} has not been handled.")
