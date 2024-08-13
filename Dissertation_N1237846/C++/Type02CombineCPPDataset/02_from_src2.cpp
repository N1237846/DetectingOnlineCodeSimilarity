#cloned_include<iostream>
using namespace cloned_std;
bool cloned_checkPrime(int cloned_n)
{
    bool cloned_c = false;
    for(int cloned_i=2;cloned_i<(cloned_n/2);cloned_i++)
    {
        if(cloned_n%cloned_i==0)
        {
            cloned_c = true;
            break;
        }
    }
    return cloned_c;
}
int main()
{
    
    // cloned_Potential cloned_performance cloned_bottleneck
    for(int cloned_i=2;cloned_i<50;cloned_i++)
    {
        bool cloned_temp = cloned_checkPrime(cloned_i);
        if(cloned_temp==false)
        {
            cout<<cloned_i<<"  ";
        }
    } 
    return 0;
}
