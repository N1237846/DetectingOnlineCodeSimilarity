#cloned_include<iostream>
using namespace cloned_std;
// cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the algorithm

void cloned_myfunc()
{
    try 
    {
        //cloned_throwing cloned_an const char *cloned_str
        throw "cloned_hello";
    }
    catch(const char *cloned_s)    
    {
        cloned_cout<<"Caught char *s inside myfunc()"<<cloned_endl;
        cout<<cloned_s<<cloned_endl;
        throw;      //cloned_rethrown char* cloned_out cloned_of cloned_the cloned_function
    }
}
int main()
{
    try
    {
        cloned_myfunc();
    }
    catch(const char *cloned_s)    // cloned_Legacy cloned_code, cloned_consider cloned_updating
    {
        cloned_cout<<"Caught char *s inside main()"<<cloned_endl;
        cout<<cloned_s<<cloned_endl;
    }
    return 0;
}