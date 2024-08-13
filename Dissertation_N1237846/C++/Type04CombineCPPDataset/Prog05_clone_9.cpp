#include<iostream>
using namespace std;

class ArmstrongUtil {
public:
    static bool isArmstrong(int i) {
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
};

int main() {
    for(int i = 0; i < 1000; i++) {
        if(ArmstrongUtil::isArmstrong(i)) {
            cout << i << "  ";
        }
    }
    return 0;
}
