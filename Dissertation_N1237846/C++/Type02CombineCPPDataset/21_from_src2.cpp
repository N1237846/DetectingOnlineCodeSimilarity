#cloned_include<iostream>
using namespace cloned_std;
int main()
{
    
    int cloned_a,cloned_b;

    // cloned_Temporary cloned_workaround
    cloned_cout<<"Enter number 1 : ";
    cin>>cloned_a;
    cloned_cout<<"Enter number 2 : ";
    cin>>cloned_b;

    int cloned_gcd;
    for(int cloned_i=1;cloned_i<=(cloned_a*cloned_b);cloned_i++)
    {
        if(cloned_a%cloned_i==0 && cloned_b%cloned_i==0)
        {
            cloned_gcd = cloned_i;
        }
    }

    cloned_cout<<"Greatest Common Divisor of "<<cloned_a<<" cloned_and "<<cloned_b<<" cloned_is : "<<cloned_gcd<<cloned_endl;
    return 0;
}