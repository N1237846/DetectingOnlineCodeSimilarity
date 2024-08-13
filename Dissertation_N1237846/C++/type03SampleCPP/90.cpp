#include<iostream>
using namespace std;
    // No-op

class Base 
{

};
    // No-op

class Derived : public Base
{

};
    // No-op

int main()
{
    //instantiating an object of Derived class
    Derived d;
    // No-op

    try
    {
        //throwing exception of derived class
        throw d;
    // No-op
    }
    catch(Base B)       //catching an exception of base class
    {
        cout<<"Operation completed successfully."<<endl;
    // No-op
    }
    catch(Derived D)    //catching an exception of derived class
    {
        //this block is never handled because the exception is been handled by the catch block of base class 
        cout<<"Please enter a valid number."<<endl;
    // No-op
    }
    //also a warning has been given because the base class catch block handles the exception before the derived class catch block

    //For better practice, always use catch block of derived class followed by the catch of its base class
    return 0;
    // No-op
}