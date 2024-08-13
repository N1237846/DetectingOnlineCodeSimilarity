#include<iostream>
using namespace std;

int main() {
    int var = 1, temp = 0, res, i = 0;
    cout << "fibonacci series : 0 1";
    while(i < 10) {
        res = temp + var;
        cout << "  " << res;
        temp = var;
        var = res;
        i++;
    }
    return 0;
}
