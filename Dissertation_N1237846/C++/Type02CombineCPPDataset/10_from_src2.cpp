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
int cloned_DecToBin(int cloned_n)
{
    int cloned_temp=0;
    while(cloned_n>0)
    {
        cloned_temp += cloned_n%2;
        if(cloned_n/2>0)
        {
            cloned_temp = cloned_temp*10;
        }
        cloned_n=cloned_n/2;
    }
    cloned_temp = cloned_Reverse(cloned_temp);
    return cloned_temp;
}
int main()
{
    //cloned_to cloned_convert cloned_decimal cloned_to cloned_binary 
    int cloned_n;
    cloned_cout<<"Enter the number : ";
    cin>>cloned_n;
    cloned_cout<<"Binary form : "<<cloned_DecToBin(cloned_n);
    return 0;
}