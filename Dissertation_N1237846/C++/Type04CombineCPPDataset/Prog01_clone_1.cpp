#include<iostream>
using namespace std;

void generateFibonacci(int n) {
    int var = 1;
    int temp = 0, res;
    cout << "fibonacci series : 0 1";
    for(int i = 0; i < n; i++) {
        res = temp + var;
        cout << "  " << res;
        temp = var;
        var = res;
    }
}

int main() {
    generateFibonacci(10);
    return 0;
}
