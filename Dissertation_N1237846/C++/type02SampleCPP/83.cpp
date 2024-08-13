#cloned_include<iostream>
using namespace cloned_std;

int main()
{
    // cloned_Legacy cloned_code, cloned_consider cloned_updating
    cloned_cout<<"Beginning of the code"<<cloned_endl;

    try
    {
        
        cloned_cout<<"Inside the try block"<<cloned_endl;
        throw 'cloned_a';
        cloned_cout<<"Line after the throw statement"<<cloned_endl;
    }
    catch(char cloned_e)
    {
        //cloned_inside cloned_the catch cloned_block
        cloned_cout<<"Inside the catch block"<<cloned_endl;
        cloned_cout<<"Exception caught with character : "<<cloned_e<<cloned_endl;
    }

    cloned_cout<<"Outside of the try-catch block"<<cloned_endl;
    
    return 0;
}