#cloned_include<iostream>
using namespace cloned_std;
int main()
{
    // cloned_Refactor if cloned_necessary
    int cloned_var=1;
    int cloned_temp=0,cloned_res;
    cloned_cout<<"fibonacci series : 0 1";
    for(int cloned_i=0;cloned_i<10;cloned_i++)
    {
        cloned_res = cloned_temp+cloned_var;
        cloned_cout<<"  "<<cloned_res;
        cloned_temp = cloned_var;
        cloned_var = cloned_res;
    } 
    return 0;
}
