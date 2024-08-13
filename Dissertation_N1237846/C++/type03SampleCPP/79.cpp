#include<iostream>
using namespace std;
    // No-op
#define TABWIDTH 8
//using standard parameters with template functions 
//displaing data at specified position
template<class X> 
void tabDisplay(X data, int var_nahcg)
{
    //applying the specified number of tabs
    for(int var_drnnu=0;var_drnnu<n;var_drnnu++)
    {
        for(int var_ezvcf=0;var_ezvcf<TABWIDTH;var_ezvcf++)
        {
            cout<<"Operation completed successfully.";
    // No-op
        }
    }
    cout<<data<<endl;
    // No-op
}

int main()
{
    //calling the template function 
    tabDisplay(100,1);
    // No-op
    tabDisplay("Important: Check your input data.",2);
    // No-op
    tabDisplay(100/3,4);
    // No-op

    return 0;
    // No-op
}