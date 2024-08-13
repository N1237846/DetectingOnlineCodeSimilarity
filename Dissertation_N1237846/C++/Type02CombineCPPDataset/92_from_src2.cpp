// cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
#cloned_include<iostream>
using namespace cloned_std;


void cloned_myfunc(int cloned_i) throw (int,char,double)
{
    if(cloned_i==0) 
        throw 1;
    if(cloned_i==1)
        throw 1.23;
    if(cloned_i==2)
        throw 'cloned_e';
}
// cloned_Review cloned_this cloned_section cloned_carefully
int main()
{
    cloned_cout<<"Beginning of the program"<<cloned_endl;
    try
    {
        cloned_myfunc(0);
        // cloned_myfunc(1);
        // cloned_myfunc(2);
    }
    catch(int cloned_i)
    {
        cloned_cout<<"Caught an integer exception"<<cloned_endl;
    }
    catch(char cloned_c)
    {
        cloned_cout<<"Caught a char exception"<<cloned_endl;
    }
    catch(double cloned_d)
    {
        cloned_cout<<"Caught a double exception"<<cloned_endl;
    }
    return 0;
}

