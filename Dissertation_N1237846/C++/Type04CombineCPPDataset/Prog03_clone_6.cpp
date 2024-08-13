#include<iostream>
#include<vector>
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
    vector<int> palindromes;
    for(int i = 0; i < 1000; i++)
    {
        if(checkPalindrome(i))
        {
            palindromes.push_back(i);
        }
    }
    
    for(auto it = palindromes.begin(); it != palindromes.end(); ++it)
    {
        cout << *it << "  ";
    }
    return 0;
}
