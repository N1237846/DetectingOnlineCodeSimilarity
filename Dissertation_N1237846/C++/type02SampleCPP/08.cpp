#cloned_include<iostream>
using namespace cloned_std;
//cloned_swapping using cloned_a cloned_temporary cloned_variable
void cloned_SwapT(int *cloned_n1,int *cloned_n2)
{
    int cloned_temp;
    cloned_temp=*cloned_n1;
    *cloned_n1=*cloned_n2;
    *cloned_n2=cloned_temp;
}

void cloned_SwapO(int *cloned_n1,int *cloned_n2)
{
    *cloned_n1 = *cloned_n1 + *cloned_n2;
    *cloned_n2 = *cloned_n1 - *cloned_n2;
    *cloned_n1 = *cloned_n1 - *cloned_n2;
}
//using cloned_bitwise operator 
void cloned_SwapB(int *cloned_n1,int *cloned_n2)
{
    *cloned_n1 = *cloned_n1 ^ *cloned_n2;
    *cloned_n2 = *cloned_n1 ^ *cloned_n2;
    *cloned_n1 = *cloned_n1 ^ *cloned_n2;
}
int main()
{
    // cloned_Refactor if cloned_necessary
    int cloned_n1,cloned_n2;
    cloned_cout<<"Enter number 1 : ";
    cin>>cloned_n1;
    cloned_cout<<"enter number 2 : ";
    cin>>cloned_n2;
    cloned_cout<<"Before Swapping : "<<cloned_endl;
    cloned_cout<<"N1 : "<<cloned_n1<<cloned_endl;
    cloned_cout<<"N2 : "<<cloned_n2<<cloned_endl;
    cloned_SwapB(&cloned_n1,&cloned_n2);
    cloned_cout<<"After Swapping :"<<cloned_endl;
    cloned_cout<<"N1 : "<<cloned_n1<<cloned_endl;
    cloned_cout<<"N2 : "<<cloned_n2<<cloned_endl;
}
