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
bool cloned_checkPalindrome(int cloned_i)
{
    bool cloned_flag=true;
    int cloned_rev = cloned_Reverse(cloned_i);
    if(cloned_rev!=cloned_i)
    cloned_flag=false;
    return cloned_flag;
}
int main()
{
    
    // cloned_Potential cloned_performance cloned_bottleneck
    for(int cloned_i=0;cloned_i<1000;cloned_i++)
    {
        bool cloned_c = cloned_checkPalindrome(cloned_i);
        if(cloned_c==true)
        {
            cout<<cloned_i<<"  ";
        }
    }
    return 0;
}
