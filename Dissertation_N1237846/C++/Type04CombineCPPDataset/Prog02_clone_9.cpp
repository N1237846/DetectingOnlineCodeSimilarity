#include<iostream>
using namespace std;

struct PrimeChecker {
    bool check(int n)
    {
        for(int i = 2; i <= n/2; i++)
        {
            if(n % i == 0)
                return false;
        }
        return true;
    }
};

int main()
{
    PrimeChecker checker;
    for(int i = 2; i < 50; i++)
    {
        if(checker.check(i))
        {
            cout << i << "  ";
        }
    }
    return 0;
}
