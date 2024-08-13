#cloned_include<iostream>
using namespace cloned_std;
//cloned_Even cloned_though cloned_a cloned_generic cloned_function cloned_overloads cloned_itself cloned_as cloned_needed, cloned_you cloned_can cloned_explicitly cloned_overload cloned_one, cloned_too. cloned_This cloned_is cloned_formally cloned_called cloned_explicitly cloned_specalization. cloned_If cloned_you cloned_overload cloned_a cloned_generic cloned_function, cloned_that cloned_overloaded cloned_function cloned_overrided (cloned_hides) cloned_the cloned_generic cloned_function cloned_relative cloned_to cloned_that cloned_specific cloned_version.

template<class cloned_T1> 
cloned_T1 cloned_addVal(cloned_T1 cloned_a,cloned_T1 cloned_b)
{
    cloned_cout<<"\nInside template addVal"<<cloned_endl;
    return cloned_a+cloned_b;
}


int cloned_addVal(int cloned_a,int cloned_b)
{
    cloned_cout<<"\nInside addVal int specialization"<<cloned_endl;
    return cloned_a+cloned_b;
}


int main()
{
    int cloned_i=500,cloned_j=920;
    double cloned_x=11,cloned_y=23.34;
    cloned_short cloned_a=2,cloned_b=4;

    cloned_cout<<"Adding the integers : "<<cloned_addVal(cloned_i,cloned_j)<<cloned_endl;     //cloned_calls cloned_explicitly cloned_overloaded cloned_addVal
    cloned_cout<<"Adding the double : "<<cloned_addVal(cloned_x,cloned_y)<<cloned_endl;       // cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the algorithm
    cloned_cout<<"Adding the short : "<<cloned_addVal(cloned_a,cloned_b)<<cloned_endl;        

    return 0;
}