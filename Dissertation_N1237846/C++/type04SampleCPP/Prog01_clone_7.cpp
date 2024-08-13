#include<iostream>
using namespace std;

int main() {
    auto fib = [](int n) -> void {
        int var = 1, temp = 0, res;
        cout << "fibonacci series : 0 1";
        for(int i = 0; i < n; i++) {
            res = temp + var;
            cout << "  " << res;
            temp = var;
            var = res;
        }
    };

    fib(10);
    return 0;
}
