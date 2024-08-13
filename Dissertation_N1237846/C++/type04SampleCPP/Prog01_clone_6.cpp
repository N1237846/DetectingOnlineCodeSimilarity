#include<iostream>
#include<iterator>
#include<vector>
using namespace std;

int main() {
    vector<int> fib = {0, 1};
    cout << "fibonacci series : 0 1";
    for(int i = 2; i < 12; i++) {
        fib.push_back(fib[i-1] + fib[i-2]);
        cout << "  " << fib[i];
    }
    return 0;
}
