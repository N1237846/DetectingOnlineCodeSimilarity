#include<iostream>
using namespace std;

bool checkPrime(int *n)
{
    for(int i = 2; i <= *n/2; i++)
    {
        if(*n % i == 0)
            return false;
    }
    return true;
}

int main()
{
    for(int i = 2; i < 50; i++)
    {
        bool temp = checkPrime(&i);
        if(temp)
        {
            cout << i << "  ";
        }
    }
    return 0;
}
