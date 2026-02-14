#include <iostream>


void stackExample(){
    int a = 1, b = 2;
    std::cout << "a: " << a << " b: " << b << std::endl;
}
void heapExample(){
    int* ptr = new int;
    *ptr = 42;
    std::cout << "Value pointed by ptr: " << *ptr << std::endl;
    delete ptr;

    int* arr = new int[5];
    for(int i =0; i < 5; i++){
        arr[i] = i * 10; // in c++ array is already dereferenced
        std::cout << "arr[" << i << "] = " << arr[i] << std::endl; 
    }
    delete[] arr;

}

int main(){
    stackExample();
    heapExample();
    return 0;
}