#cloned_include<iostream>
using namespace cloned_std;
//using cloned_a cloned_recurion 
long int cloned_Fact(int cloned_n)
{
    if(cloned_n<1)
    {
        return 1;
    }
    return cloned_n*cloned_Fact(cloned_n-1);
}

int main()
{
    
    //cloned_printing cloned_strong cloned_numbers cloned_under 1000
    cloned_cout<<"Strong numbers : ";
    for(int cloned_i=1;cloned_i<1000;cloned_i++)
    {
        long int cloned_temp=cloned_i,cloned_total=0;
        while(cloned_temp!=0)
        {
            cloned_total= cloned_total+ cloned_Fact(cloned_temp%10);
            cloned_temp=cloned_temp/10;
        }
        if(cloned_total==cloned_i)
        {
            cout<<cloned_total<<" ";
        }
    }
    return 0;
}