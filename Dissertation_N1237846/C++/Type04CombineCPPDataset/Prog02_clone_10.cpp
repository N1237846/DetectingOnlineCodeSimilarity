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
    int i = 2;
    while(i < 50)
    {
        if(checkPrime(i))
        {
            cout << i << "  ";
        }
        i++;
    }
    return 0;
}
