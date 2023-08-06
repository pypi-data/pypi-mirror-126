#include <iostream>
#include <cstdlib>
using namespace std;

int main(void) {
    // allocate memory of int size to an int pointer
    int *ptr = (int*) malloc(sizeof(int));

    // another pointer allocation
    int *ptr2 = (int*) malloc(sizeof(int) * 20);

    // assign the value 5 to allocated memory
    *ptr = 5;

    cout << *ptr << endl;

    cout << "Hello World" << endl;

    free(ptr);

    return 0;
}
