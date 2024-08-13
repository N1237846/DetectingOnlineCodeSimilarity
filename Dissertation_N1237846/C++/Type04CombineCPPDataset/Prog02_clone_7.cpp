#include<iostream>
using namespace std;

int main()
{
    auto isPrime = [](int n) -> bool {
        for(int i = 2; i <= n/2; i++)
        {
            if(n % i == 0)
                return false;
        }
        return true;
    };
    
    for(int i = 2; i < 50; i++)
    {
        if(isPrime(i))
        {
            cout << i << "  ";
        }
    }
    return 0;
}
