#include<iostream>
using namespace std;

int Reverse(int n, int temp = 0)
{
    if(n == 0)
        return temp;
    temp = temp * 10 + n % 10;
    return Reverse(n / 10, temp);
}

bool checkPalindrome(int i)
{
    return Reverse(i) == i;
}

int main()
{
    for(int i = 0; i < 1000; i++)
    {
        if(checkPalindrome(i))
        {
            cout << i << "  ";
        }
    }
    return 0;
}
