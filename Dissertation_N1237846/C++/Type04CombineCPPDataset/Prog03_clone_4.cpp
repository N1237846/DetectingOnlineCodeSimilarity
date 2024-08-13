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

int main()
{
    int palindromes[1000], index = 0;
    for(int i = 0; i < 1000; i++)
    {
        if(checkPalindrome(i))
        {
            palindromes[index++] = i;
        }
    }
    
    for(int i = 0; i < index; i++)
    {
        cout << palindromes[i] << "  ";
    }
    return 0;
}
