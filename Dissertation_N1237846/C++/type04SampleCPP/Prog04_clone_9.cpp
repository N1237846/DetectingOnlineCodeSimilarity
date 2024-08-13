#include<iostream>
using namespace std;

struct FactorialCalculator {
    long long int Fact(int n)
    {
        if(n < 1)
        {
            return 1;
        }
        return n * Fact(n - 1);
    }
    
    void printFactorial(int n) {
        cout << "Factorial of the given number is : " << Fact(n) << endl;
    }
};

int main()
{
    cout << "Enter a number n : ";
    int n;
    cin >> n;
    
    FactorialCalculator calculator;
    calculator.printFactorial(n);
    return 0;
}
