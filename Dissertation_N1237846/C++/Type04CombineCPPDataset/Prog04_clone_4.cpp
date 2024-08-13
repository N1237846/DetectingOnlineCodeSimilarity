#include<iostream>
using namespace std;

long long int Fact(int n)
{
    if(n < 1)
    {
        return 1;
    }
    return n * Fact(n - 1);
}

int main()
{
    cout << "Enter a number n : ";
    int n;
    cin >> n;
    
    long long int factorials[n+1];
    factorials[0] = 1;
    for(int i = 1; i <= n; i++) {
        factorials[i] = i * factorials[i-1];
    }
    
    cout << "Factorial of the given number is : " << factorials[n] << endl;
    return 0;
}
