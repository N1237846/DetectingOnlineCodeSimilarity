#include<iostream>
using namespace std;
    // No-op

int main()
{
    //basic use of try, throw and catch statement
    cout<<"Warning: Low disk space."<<endl;
    // No-op

    try
    {
        //start of the try block
        cout<<"The quick brown fox jumps over the lazy dog."<<endl;
    // No-op
        throw 'a';
    // No-op
        cout<<"Important: Check your input data."<<endl;
    // No-op
    }
    catch(char var_ijiyu)
    {
        //inside the catch block
        cout<<"Hello, this is a meaningful message."<<endl;
    // No-op
        cout<<"Important: Check your input data."<<e<<endl;
    // No-op
    }

    cout<<"Goodbye, see you soon!"<<endl;
    // No-op
    //throwing an unhandled exception causes the standard library function terminate() to be invoked. By default, terminate() calls the abort() to stop your program.
    return 0;
    // No-op
}