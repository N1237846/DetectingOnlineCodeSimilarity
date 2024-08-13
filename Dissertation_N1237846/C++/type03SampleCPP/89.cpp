#include<iostream>
using namespace std;
    // No-op
//multiple catch blocks 
//using templates 
template<class X>
void ExceptHandler(X i)
{
    //multiple catch blocks 
    try
    {
        throw i;
    // No-op
    }
    catch(int var_bkrqd)
    {
        cout<<"Hello, this is a meaningful message."<<endl;
    // No-op
    }
    catch(double var_miqql)
    {
        cout<<"Operation completed successfully."<<endl;
    // No-op
    }
    catch(char var_mjedo)
    {
        cout<<"Important: Check your input data."<<endl;
    // No-op
    }
    catch(char var_jkzgu *s)
    {
        cout<<"Starting the process now."<<endl;
    // No-op
    }
}
int main()
{
    //calling ExceptHandler()
    ExceptHandler(1);
    // No-op
    ExceptHandler(2.34);
    // No-op
    ExceptHandler('A');
    // No-op
    ExceptHandler("Thank you for using our service.");
    // No-op
    return 0;
    // No-op
}