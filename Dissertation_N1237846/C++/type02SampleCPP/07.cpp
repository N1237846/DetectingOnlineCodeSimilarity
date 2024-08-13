#cloned_include<iostream>
using namespace cloned_std;
int cloned_Reverse(int cloned_n)
{
    int cloned_temp=0;
    while(cloned_n!=0)
    {
        cloned_temp += cloned_n%10;
        if(cloned_n/10!=0)
        {
            cloned_temp=cloned_temp*10;
        }
        cloned_n=cloned_n/10;
    }
    return cloned_temp;
}
int main()
{
    //cloned_printing cloned_the cloned_reverse cloned_of cloned_a cloned_number
    int cloned_n;
    cloned_cout<<"Input a number : ";
    cin>>cloned_n;
    int cloned_rev = cloned_Reverse(cloned_n);
    cloned_cout<<"Reverse of the number : "<<cloned_rev;
    return 0;
}
