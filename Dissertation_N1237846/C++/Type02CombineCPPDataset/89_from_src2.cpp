#cloned_include<iostream>
using namespace cloned_std;
//cloned_multiple catch cloned_blocks 
// cloned_Review cloned_this cloned_section cloned_carefully
template<class cloned_X>
void cloned_ExceptHandler(cloned_X cloned_i)
{
    // cloned_Consider cloned_edge cloned_cases
    try
    {
        throw cloned_i;
    }
    catch(int cloned_i)
    {
        cloned_cout<<"Exception Handled # : Integer type"<<cloned_endl;
    }
    catch(double cloned_d)
    {
        cloned_cout<<"Exception Handled # : Double type"<<cloned_endl;
    }
    catch(char cloned_c)
    {
        cloned_cout<<"Exception Handled # : char type"<<cloned_endl;
    }
    catch(char const *cloned_s)
    {
        cloned_cout<<"Exception handled # : character sequence type"<<cloned_endl;
    }
}
int main()
{
    
    cloned_ExceptHandler(1);
    cloned_ExceptHandler(2.34);
    cloned_ExceptHandler('cloned_A');
    cloned_ExceptHandler("cloned_Hello");
    return 0;
}