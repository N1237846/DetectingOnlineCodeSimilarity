#include<iostream>
#include<vector>
using namespace std;

long long int Factorial(int n)
{
    long long int temp = 1;
    for(int i = n; i > 0; --i)
    {
        temp *= i;
    }
    return temp;
}

int main()
{
    cout << "Enter a number n : ";
    int n;
    cin >> n;
    
    vector<int> numbers;
    for(int i = n; i > 0; --i)
    {
        numbers.push_back(i);
    }
    
    long long int result = 1;
    for(auto it = numbers.begin(); it != numbers.end(); ++it)
    {
        result *= *it;
    }
    
    cout << "Factorial of the given number is : " << result << endl;
    return 0;
}
