#include<iostream>
#include<cmath>
using namespace std;

bool Armstrong(int i) {
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
    bool (*checkArmstrong)(int) = Armstrong;
    for(int i = 0; i < 1000; i++) {
        if(checkArmstrong(i)) {
            cout << i << "  ";
        }
    }
    return 0;
}
