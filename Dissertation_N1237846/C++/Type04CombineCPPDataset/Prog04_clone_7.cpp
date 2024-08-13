#include<iostream>
using namespace std;

int main()
{
    auto Fact = [](int n) -> long long int {
        if(n < 1)
        {
            return 1;
        }
        return n * Fact(n - 1);
    };

    cout << "Enter a number n : ";
    int n;
    cin >> n;
    cout << "Factorial of the given number is : " << Fact(n) << endl;
    return 0;
}
