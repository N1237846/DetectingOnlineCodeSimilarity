#include<iostream>
using namespace std;

struct FibonacciGenerator {
    int temp = 0;
    int var = 1;

    void generate(int n) {
        cout << "fibonacci series : 0 1";
        for(int i = 0; i < n; i++) {
            int res = temp + var;
            cout << "  " << res;
            temp = var;
            var = res;
        }
    }
};

int main() {
    FibonacciGenerator fibGen;
    fibGen.generate(10);
    return 0;
}
