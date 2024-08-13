#include<iostream>
using namespace std;

class PalindromeChecker {
public:
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

    void printPalindromes(int limit) {
        for(int i = 0; i < limit; i++)
        {
            if(check(i))
            {
                cout << i << "  ";
            }
        }
    }
};

int main()
{
    PalindromeChecker checker;
    checker.printPalindromes(1000);
    return 0;
}
