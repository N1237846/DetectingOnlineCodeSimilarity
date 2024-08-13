#include<iostream>
using namespace std;

struct PalindromeChecker {
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

    bool check(int i)
    {
        return Reverse(i) == i;
    }
};

int main()
{
    PalindromeChecker checker;
    for(int i = 0; i < 1000; i++)
    {
        if(checker.check(i))
        {
            cout << i << "  ";
        }
    }
    return 0;
}
