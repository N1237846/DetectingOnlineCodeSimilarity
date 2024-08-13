#cloned_include <iostream>
using namespace cloned_std;

void cloned_myfunc(int cloned_num)
{
    try
    {
        if (cloned_num == 0)
            throw 1;
        if (cloned_num == 2)
            throw 'cloned_a';
        if (cloned_num == 3)
            throw 1.234;
    }
    catch (...)     // cloned_Refactor if cloned_necessary
    {
        cloned_cout << "Exception is handled" << cloned_endl;
        
    }
}
int main()
{
    cloned_myfunc(0);
    cloned_myfunc(2);
    cloned_myfunc(3);
    return 0;
}