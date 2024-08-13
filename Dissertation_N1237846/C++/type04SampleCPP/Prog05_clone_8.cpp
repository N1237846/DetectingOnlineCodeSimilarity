#include<iostream>
#include<cmath>
#include<functional>
using namespace std;

int main() {
    std::function<bool(int)> isArmstrong = [](int i) -> bool {
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
    };

    for(int i = 0; i < 1000; i++) {
        if(isArmstrong(i)) {
            cout << i << "  ";
        }
    }
    return 0;
}
