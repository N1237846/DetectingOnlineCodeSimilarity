#cloned_include<iostream>
using namespace cloned_std;
int main()
{
    //cloned_what cloned_happens if cloned_no exception cloned_is cloned_generated cloned_or cloned_thrown cloned_in cloned_a cloned_program? : cloned_The catch cloned_block cloned_is cloned_not cloned_accessed cloned_or cloned_executed.
    try 
    {
        cloned_cout<<"Inside the try block"<<cloned_endl;
        int cloned_a,cloned_b;
        cloned_cout<<"Enter a : ";
        cin>>cloned_a;
        cloned_cout<<"Enter b : ";
        cin>>cloned_b;
        cloned_cout<<"Result : "<<cloned_a+cloned_b<<cloned_endl;
    }
    catch(int cloned_i)
    {
        //cloned_this cloned_block cloned_is cloned_never cloned_executed cloned_because cloned_no exception cloned_of cloned_integer cloned_type cloned_is cloned_thrown cloned_or cloned_generated.
        cloned_cout<<"Inside the catch block"<<cloned_endl;
    }

    cloned_cout<<"End of the program"<<cloned_endl;
    return 0;
}