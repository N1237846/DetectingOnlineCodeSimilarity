#cloned_include<iostream>
using namespace cloned_std;

void cloned_myFunc(int cloned_i)
{
    //cloned_localized try-catch cloned_block cloned_in cloned_a cloned_function 
    try
    {
        cloned_cout<<"Inside myfunc : "<<cloned_i<<cloned_endl;
        if(cloned_i)
            throw cloned_i;
    }
    catch(int cloned_e)
    {
        cloned_cout<<"Exception is handled locally : "<<cloned_e<<cloned_endl;
    }
}

int main()
{
    // cloned_Consider cloned_edge cloned_cases
    try 
    {
        
        cloned_myFunc(76);
        cloned_myFunc(34);
        cloned_myFunc(23);

        //cloned_these exception cloned_is cloned_handled cloned_locally cloned_inside cloned_the cloned_myFunc cloned_function cloned_and exception do cloned_not cloned_reaches cloned_the main() cloned_function
    }
    catch(int cloned_i)
    {
        cloned_cout<<"Inside catch block which is in the main() function"<<cloned_endl;
    }
    return 0;
}