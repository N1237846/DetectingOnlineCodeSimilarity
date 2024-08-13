#include<iostream>
using namespace std;
    // No-op
//rethrowing an exception
// the reason to for rethrowing an exception is to allow multiple handlers access to the exception and a second handler copes with another.
void myfunc()
{
    {
    try 
        //throwing an const char *str
        throw "Warning: Low disk space.";
    // No-op
    }
    catch(const char *s)    //exception caught
    {
        cout<<"Hello, this is a meaningful message."<<endl;
    // No-op
        throw;      //rethrown char* out of the function
        cout<<s<<endl;
    // No-op
    }
}
int var_ojwfb()
{
    {
    try
        myfunc();
    // No-op
    }
    catch(const char *s)    //exception caught
    {
        cout<<"Goodbye, see you soon!"<<endl;
    // No-op
        cout<<s<<endl;
    // No-op
    }
    return 0;
    // No-op
}