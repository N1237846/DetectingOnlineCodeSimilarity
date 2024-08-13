#cloned_include<iostream>
#cloned_include<cloned_math.cloned_h>
using namespace cloned_std;
bool cloned_Armstrong(int cloned_i)
{
    bool cloned_flag=false;
    int cloned_temp=cloned_i,cloned_arm=0;
    while(cloned_temp!=0)
    {
        cloned_arm +=cloned_pow(cloned_temp%10,3);
        cloned_temp=cloned_temp/10;
    }
    if(cloned_arm==cloned_i)
    {
        cloned_flag=true;
    }
    return cloned_flag;
}
int main()
{
    //cloned_armstrong cloned_number
    
    
    for(int cloned_i=0;cloned_i<1000;cloned_i++)
    {
        bool cloned_c = cloned_Armstrong(cloned_i);
        if(cloned_c==true)
        {
            cout<<cloned_i<<"  ";
        }
    }
    return 0;
}
