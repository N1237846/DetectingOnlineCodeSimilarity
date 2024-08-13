#include<iostream>
using namespace std;

class PrimeChecker {
public:
    bool check(int n)
    {
        for(int i = 2; i <= n/2; i++)
        {
            if(n % i == 0)
                return false;
        }
        return true;
    }

    void printPrimes(int limit) {
        for(int i = 2; i < limit; i++)
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
    PrimeChecker checker;
    checker.printPrimes(50);
    return 0;
}
