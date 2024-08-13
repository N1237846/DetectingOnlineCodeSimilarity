#include<iostream>
#include<cmath>
using namespace std;

bool isArmstrong(int i) {
    bool flag = false;
    int temp = i, arm = 0;
    while(temp != 0) {
        arm += pow(temp % 10, 3);
        temp /= 10;
    }
    if(arm == i) {
        flag = true;
    }
    return flag;
}

void displayArmstrongNumbers() {
    for(int i = 0; i < 1000; i++) {
        if(isArmstrong(i)) {
            cout << i << "  ";
        }
    }
}

int main() {
    displayArmstrongNumbers();
    return 0;
}
