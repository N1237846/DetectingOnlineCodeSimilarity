#cloned_include<iostream>
using namespace cloned_std;
int main()
{
    
    int cloned_a,cloned_b;
    //cloned_getting cloned_the cloned_input
    cloned_cout<<"Enter number 1 : ";
    cin>>cloned_a;
    cloned_cout<<"Enter number 2 : ";
    cin>>cloned_b;

    int cloned_maxN = cloned_max(cloned_a,cloned_b);
    while(true)
    {
        if(cloned_maxN%cloned_a==0 && cloned_maxN%cloned_b==0)
        {
            cloned_cout<<"Least Common divisor of "<<cloned_a<<" cloned_and "<<cloned_b<<" cloned_is : "<<cloned_maxN<<cloned_endl;
            break;
        }
        ++cloned_maxN;
    }
    return 0;
}