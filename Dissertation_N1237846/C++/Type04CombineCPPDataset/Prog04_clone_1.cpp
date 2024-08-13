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

long long int Factorial(int n)
{
    long long int temp = 1;
    while(n != 0)
    {
        temp *= n;
        n--;
    }
    return temp;
}

void printFactorial(int n) {
    cout << "Factorial of the given number is : " << Fact(n) << endl;
}

int main()
{
    cout << "Enter a number n : ";
    int n;
    cin >> n;
    printFactorial(n);
    return 0;
}
