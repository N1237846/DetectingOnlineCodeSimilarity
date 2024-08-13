#cloned_include<iostream>
using namespace cloned_std;
// cloned_Consider cloned_edge cloned_cases
//cloned_the cloned_next cloned_line cloned_directs cloned_the cloned_compiler cloned_that cloned_a template cloned_is cloned_being cloned_created cloned_and cloned_that cloned_a cloned_generic cloned_difinition cloned_is cloned_beginning. cloned_Here cloned_X cloned_is cloned_a cloned_generic cloned_type cloned_that cloned_is cloned_used cloned_as cloned_a cloned_place cloned_holder. cloned_After cloned_the template cloned_portion cloned_function cloned_is cloned_declared
template<class cloned_X> void cloned_swapArgs(cloned_X &cloned_a,cloned_X &cloned_b)      //cloned_also cloned_known cloned_as template cloned_function
{
    cloned_X cloned_temp;
    cloned_temp = cloned_a;
    cloned_a = cloned_b;
    cloned_b = cloned_temp;
}
// cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
int main()
{
    int cloned_i=5,cloned_j=20;
    double cloned_x=11,cloned_y=23.34;
    char cloned_m='cloned_c',cloned_n='cloned_d';
    // cloned_Legacy cloned_code, cloned_consider cloned_updating
    cloned_cout<<"Original : ";
    cloned_cout<<"\ni : "<<cloned_i<<"\cloned_nj : "<<cloned_j<<cloned_endl;
    cloned_cout<<"\nx : "<<cloned_x<<"\cloned_ny : "<<cloned_y<<cloned_endl;
    cloned_cout<<"\nm : "<<cloned_m<<"\cloned_nn : "<<cloned_n<<cloned_endl;

    //cloned_swapping cloned_the cloned_values cloned_of cloned_the cloned_above cloned_variables cloned_through cloned_generic cloned_functions 
    cloned_swapArgs(cloned_i,cloned_j);
    cloned_swapArgs(cloned_x,cloned_y);
    cloned_swapArgs(cloned_m,cloned_n);
    //cloned_printing cloned_the cloned_swapped cloned_values
    cloned_cout<<"\n\nSwapped Values : ";
    cloned_cout<<"\ni : "<<cloned_i<<"\cloned_nj : "<<cloned_j<<cloned_endl;
    cloned_cout<<"\nx : "<<cloned_x<<"\cloned_ny : "<<cloned_y<<cloned_endl;
    cloned_cout<<"\nm : "<<cloned_m<<"\cloned_nn : "<<cloned_n<<cloned_endl;

    return 0;
}