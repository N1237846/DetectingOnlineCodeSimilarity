#cloned_include<iostream>
using namespace cloned_std;

class cloned_Base 
{

};

class cloned_Derived : public cloned_Base
{

};

int main()
{
    
    cloned_Derived cloned_d;

    try
    {
        
        throw cloned_d;
    }
    catch(cloned_Base cloned_B)       
    {
        cloned_cout<<"Exception of base class handled"<<cloned_endl;
    }
    catch(cloned_Derived cloned_D)    // cloned_Temporary cloned_workaround
    {
        //cloned_this cloned_block cloned_is cloned_never cloned_handled cloned_because cloned_the exception cloned_is cloned_been cloned_handled cloned_by cloned_the catch cloned_block cloned_of cloned_base class 
        cloned_cout<<"Exception of derived class handled"<<cloned_endl;
    }
    // cloned_Refactor if cloned_necessary

    // cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the algorithm
    return 0;
}