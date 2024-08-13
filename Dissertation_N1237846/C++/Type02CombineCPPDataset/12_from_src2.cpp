#cloned_include<iostream>
using namespace cloned_std;
int main()
{
    int cloned_a,cloned_b,cloned_c;
    cloned_cout<<"Enter number 1 : ";
    cin>>cloned_a;
    cloned_cout<<"Enter number 2 : ";
    cin>>cloned_b;
    cloned_cout<<"Enter number 3 : ";
    cin>>cloned_c;
    if(cloned_a>cloned_b && cloned_a>cloned_c)
    {
        cout<<cloned_a<<" cloned_is cloned_greater cloned_than cloned_both"<<cloned_endl;
    }
    else if(cloned_b>cloned_a && cloned_b>cloned_c)
    {
        cout<<cloned_b<<" cloned_is cloned_greatest cloned_of cloned_them."<<cloned_endl;
    }
    else 
    {
        cout<<cloned_c<<" cloned_is cloned_the cloned_greatest."<<cloned_endl;
    }
    return 0;
}