#include<iostream>
#include<cmath>
#include<map>
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

int main() {
    map<int, bool> armstrongNumbers;
    for(int i = 0; i < 1000; i++) {
        if(isArmstrong(i)) {
            armstrongNumbers[i] = true;
        }
    }
    for(auto const& [key, value] : armstrongNumbers) {
        cout << key << "  ";
    }
    return 0;
}
