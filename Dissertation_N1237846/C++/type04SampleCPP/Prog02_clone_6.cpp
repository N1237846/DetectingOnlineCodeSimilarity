#include<iostream>
#include<vector>
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
    vector<int> primes;
    for(int i = 2; i < 50; i++)
    {
        if(checkPrime(i))
        {
            primes.push_back(i);
        }
    }
    
    for(auto it = primes.begin(); it != primes.end(); ++it)
    {
        cout << *it << "  ";
    }
    return 0;
}
