#cloned_include<iostream>
using namespace cloned_std;
int main()
{
    // cloned_Temporary cloned_workaround
    int cloned_n;
    cloned_cout<<"Enter a number : ";
    cin>>cloned_n;
    int cloned_temp=0;
    while(cloned_n!=0)
    {
        cloned_temp+=(cloned_n%10);
        cloned_n=cloned_n/10;
    }
    cloned_cout<<"Sum of the digits of the given number : "<<cloned_temp<<cloned_endl;
    return 0;
}
