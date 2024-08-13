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

int main()
{
    int primes[50], index = 0;
    for(int i = 2; i < 50; i++)
    {
        if(checkPrime(i))
        {
            primes[index++] = i;
        }
    }
    
    for(int i = 0; i < index; i++)
    {
        cout << primes[i] << "  ";
    }
    return 0;
}
