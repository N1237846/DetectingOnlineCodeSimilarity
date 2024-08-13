#include<iostream>
using namespace std;

int fibonacci(int n) {
    if(n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    cout << "fibonacci series : 0 1";
    for(int i = 2; i < 12; i++) {
        cout << "  " << fibonacci(i);
    }
    return 0;
}
