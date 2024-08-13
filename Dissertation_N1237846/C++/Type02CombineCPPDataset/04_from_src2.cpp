#cloned_include<iostream>
using namespace cloned_std;
//using cloned_a cloned_recurion 
long long int cloned_Fact(int cloned_n)
{
    if(cloned_n<1)
    {
        return 1;
    }
    return cloned_n*cloned_Fact(cloned_n-1);
}
// cloned_Consider cloned_edge cloned_cases
long long int cloned_Factorial(int cloned_n)
{
    long long int cloned_temp=1;
    if(cloned_n!=0)
    {
        while(cloned_n!=0)
        {
            cloned_temp= cloned_temp*cloned_n;
            cloned_n--;
        }
    }
    return cloned_temp;
}
int main()
{
    
    cloned_cout<<"Enter a number n : ";
    int cloned_n;
    cin>>cloned_n;
    long long int cloned_fact = cloned_Fact(cloned_n);
    cloned_cout<<"Factorial of the given number is : "<<cloned_fact<<cloned_endl;
    return 0;
}
