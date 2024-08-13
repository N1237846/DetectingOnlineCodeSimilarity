#include<iostream>
#include<cmath>
#include<vector>
using namespace std;

int main() {
    vector<int> armstrongNumbers;
    auto isArmstrong = [](int i) -> bool {
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
            armstrongNumbers.push_back(i);
        }
    }
    for(int num : armstrongNumbers) {
        cout << num << "  ";
    }
    return 0;
}
