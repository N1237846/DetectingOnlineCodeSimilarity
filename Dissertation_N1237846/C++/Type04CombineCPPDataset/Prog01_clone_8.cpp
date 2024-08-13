#include<iostream>
using namespace std;

void printFibonacci(int temp, int var) {
    cout << "fibonacci series : 0 1";
    for(int i = 0; i < 10; i++) {
        int res = temp + var;
        cout << "  " << res;
        temp = var;
        var = res;
    }
}

int main() {
    printFibonacci(0, 1);
    return 0;
}
