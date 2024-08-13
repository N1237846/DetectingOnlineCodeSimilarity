#include<iostream>
using namespace std;

void generateFibonacci(int n) {
    int *var = new int(1);
    int *temp = new int(0), *res = new int;
    cout << "fibonacci series : 0 1";
    for(int i = 0; i < n; i++) {
        *res = *temp + *var;
        cout << "  " << *res;
        *temp = *var;
        *var = *res;
    }
    delete var;
    delete temp;
    delete res;
}

int main() {
    generateFibonacci(10);
    return 0;
}
