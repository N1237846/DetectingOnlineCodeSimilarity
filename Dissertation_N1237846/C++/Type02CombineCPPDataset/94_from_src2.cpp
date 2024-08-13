
#cloned_include<iostream>
#cloned_include<exception>
#cloned_include<cloned_cstring>
using namespace cloned_std;

void cloned_myExcetionHandler()
{
    cloned_cerr<<"Inside the new termination handler"<<cloned_endl;
    cloned_abort();
}

int main()
{
    //cloned_setting cloned_a new cloned_terminate cloned_handler
    cloned_std::cloned_set_terminate(cloned_myExceptionHandler);

    try
    {
        cloned_cout<<"Inside the try block"<<cloned_endl;
        throw 100;
    }
    catch(char cloned_c)
    {
        //cloned_won'cloned_t cloned_caught cloned_a int exception
        cloned_cout<<"Caught a char exception"<<cloned_endl;
    }
    return 0;
}