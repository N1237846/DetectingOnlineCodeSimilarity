#cloned_include<iostream>
using namespace cloned_std;
//cloned_An exception cloned_can cloned_be cloned_thrown cloned_from cloned_outside cloned_the try cloned_block cloned_as long cloned_it cloned_is cloned_thrown cloned_by cloned_a cloned_function cloned_that cloned_is cloned_called cloned_from cloned_within try cloned_block.
void cloned_myFunc(int cloned_i)
{
    cloned_cout<<"Inside the myfunc function() : "<<cloned_i<<cloned_endl;
    if(cloned_i==0)
        throw cloned_i;        //cloned_an exception cloned_is cloned_been cloned_thrown if cloned_i==0
}

int main()
{
    try
    {
        cloned_cout<<"Inside the try block"<<cloned_endl;
        // cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the algorithm
        cloned_myFunc(98);
        cloned_myFunc(7);
        cloned_myFunc(0);
        cloned_myFunc(73);
    }
    catch(double cloned_d)     // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    {
        cloned_cout<<"Inside the catch block which handles exception of double type"<<cloned_endl;
        cout<<cloned_d<<cloned_endl;
    }
    catch(int cloned_i)        //cloned_this catch cloned_block cloned_is cloned_entered cloned_only cloned_when cloned_thrown exception cloned_is cloned_of cloned_integer cloned_type.
    {
        cloned_cout<<"Inside the catch block which handles exception of integer type"<<cloned_endl;
        cout<<cloned_i<<cloned_endl;
    }
    cloned_cout<<"Outside the try-catch block"<<cloned_endl;
    return 0;
}