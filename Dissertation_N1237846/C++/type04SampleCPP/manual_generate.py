# Define the 10 Type IV clone samples as strings
clone_samples = [
    '''#include<iostream>
#include<cmath>
using namespace std;

class ArmstrongChecker {
public:
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
};

int main() {
    ArmstrongChecker checker;
    for(int i = 0; i < 1000; i++) {
        if(checker.isArmstrong(i)) {
            cout << i << "  ";
        }
    }
    return 0;
}
''',

    '''#include<iostream>
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
''',

    '''#include<iostream>
#include<cmath>
using namespace std;

int main() {
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
            cout << i << "  ";
        }
    }
    return 0;
}
''',

    '''#include<iostream>
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
''',

    '''#include<iostream>
#include<cmath>
#include<vector>
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
    vector<int> armstrongNumbers;
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
''',

    '''#include<iostream>
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
''',

    '''#include<iostream>
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
''',

    '''#include<iostream>
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
''',

    '''#include<iostream>
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
''',

    '''#include<iostream>
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
'''
]

# Generate 10 C++ files with the clone samples
def generate_clone_files():
    for i, sample in enumerate(clone_samples, start=1):
        filename = f"Prog05_clone_{i}.cpp"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(sample)

if __name__ == "__main__":
    generate_clone_files()
    print("10 C++ clone files have been created.")
