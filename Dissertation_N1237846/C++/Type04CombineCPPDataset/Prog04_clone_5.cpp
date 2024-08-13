#include<iostream>
using namespace std;

long long int Fact(int *n)
{
    if(*n < 1)
    {
        return 1;
    }
    int temp = *n - 1;
    return (*n) * Fact(&temp);
}

int main()
{
    cout << "Enter a number n : ";
    int n;
    cin >> n;
    cout << "Factorial of the given number is : " << Fact(&n) << endl;
    return 0;
}
