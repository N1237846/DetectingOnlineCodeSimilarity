#include<iostream>
using namespace std;

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

int main()
{
    cout << "Enter a number n : ";
    int n;
    cin >> n;
    cout << "Factorial of the given number is : " << Factorial(n) << endl;
    return 0;
}
