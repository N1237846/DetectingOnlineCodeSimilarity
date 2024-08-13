#cloned_include<iostream>
using namespace cloned_std;



template<class cloned_X> 
void cloned_print(cloned_X cloned_a)
{
    cloned_cout<<"\nInside function print which take a single argument"<<cloned_endl;
    cloned_cout<<"a : "<<cloned_a<<cloned_endl;
}


template<class cloned_X,class cloned_Y>
void cloned_print(cloned_X cloned_a,cloned_Y cloned_b)
{
    cloned_cout<<"\nInside function print which takes two arguments"<<cloned_endl;
    cloned_cout<<"a : "<<cloned_a<<cloned_endl;
    cloned_cout<<"b : "<<cloned_b<<cloned_endl;
}

int main()
{
    int cloned_i=5;
    double cloned_y=23.34;
    char cloned_n='cloned_d';

    cloned_print(cloned_i);       
    cloned_print(cloned_y,cloned_n);     
    cloned_print(cloned_i,cloned_y);     

    return 0;
}