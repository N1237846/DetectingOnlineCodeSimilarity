#include<iostream>
using namespace std;

int main()
{
    auto Reverse = [](int n) -> int {
        int temp = 0;
        while(n != 0)
        {
            temp += n % 10;
            if(n / 10 != 0)
            {
                temp = temp * 10;
            }
            n = n / 10;
        }
        return temp;
    };
    
    auto checkPalindrome = [Reverse](int i) -> bool {
        return Reverse(i) == i;
    };
    
    for(int i = 0; i < 1000; i++)
    {
        if(checkPalindrome(i))
        {
            cout << i << "  ";
        }
    }
    return 0;
}
