#include<iostream>
using namespace std;

bool checkPrime(int n)
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
        if(checkPrime(i))
        {
            cout << i << "  ";
        }
    }
}

int main()
{
    printPrimes(50);
    return 0;
}
