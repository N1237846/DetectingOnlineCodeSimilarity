#include<iostream>
using namespace std;

int Reverse(int n)
{
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
}

bool checkPalindrome(int i)
{
    return Reverse(i) == i;
}

void printPalindromesUpTo(int limit) {
    for(int i = 0; i < limit; i++)
    {
        if(checkPalindrome(i))
        {
            cout << i << "  ";
        }
    }
}

int main()
{
    printPalindromesUpTo(1000);
    return 0;
}
