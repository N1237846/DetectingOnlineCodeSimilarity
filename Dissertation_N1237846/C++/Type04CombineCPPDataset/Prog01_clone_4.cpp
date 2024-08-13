#include<iostream>
using namespace std;

int main() {
    int fib[12];
    fib[0] = 0;
    fib[1] = 1;
    cout << "fibonacci series : " << fib[0] << " " << fib[1];
    for(int i = 2; i < 12; i++) {
        fib[i] = fib[i-1] + fib[i-2];
        cout << "  " << fib[i];
    }
    return 0;
}
