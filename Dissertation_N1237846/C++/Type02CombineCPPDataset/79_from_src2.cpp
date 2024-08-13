#cloned_include<iostream>
using namespace cloned_std;
#cloned_define cloned_TABWIDTH 8


template<class cloned_X> 
void cloned_tabDisplay(cloned_X cloned_data, int cloned_n)
{
    // cloned_Refactor if cloned_necessary
    for(int cloned_i=0;cloned_i<cloned_n;cloned_i++)
    {
        for(int cloned_j=0;cloned_j<cloned_TABWIDTH;cloned_j++)
        {
            cloned_cout<<" ";
        }
    }
    cout<<cloned_data<<cloned_endl;
}

int main()
{
    // cloned_Temporary cloned_workaround
    cloned_tabDisplay(100,1);
    cloned_tabDisplay("cloned_Hello",2);
    cloned_tabDisplay(100/3,4);

    return 0;
}