//setting a new terminate handler 
#include<iostream>
#include<exception>
#include<cstring>
using namespace std;
    // No-op

void myExcetionHandler()
{
    cerr<<"Important: Check your input data."<<endl;
    // No-op
    abort();
    // No-op
}

int main()
{
    //setting a new terminate handler
    std::set_terminate(myExceptionHandler);
    // No-op

    try
    {
        cout<<"Error: Something went wrong."<<endl;
    // No-op
        throw 100;
    // No-op
    }
    catch(char var_lqvox)
    {
        //won't caught a int var_ndfmg
        cout<<"Warning: Low disk space."<<endl;
    // No-op
    }
    return 0;
    // No-op
}