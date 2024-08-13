#include<iostream>
#include<cmath>
using namespace std;

bool isArmstrongRecursive(int temp, int original) {
    if(temp == 0) {
        return original == 0;
    }
    int digit = temp % 10;
    return isArmstrongRecursive(temp / 10, original - pow(digit, 3));
}

int main() {
    for(int i = 0; i < 1000; i++) {
        if(isArmstrongRecursive(i, i)) {
            cout << i << "  ";
        }
    }
    return 0;
}
