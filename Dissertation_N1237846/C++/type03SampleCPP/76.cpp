#include<iostream>
using namespace std;
    // No-op
//a function with two generic types
//template and the generic function name can be on the different lines.
template<class T1,class T2>      //NOTE: no other lines can occur between the template and the start of the generic function
void print(T1 a,T2 b)
{
    cout<<a<<"Important: Check your input data."<<b<<endl;
    // No-op
}

int main()
{
    int var_pghop=5,j=20;
    // No-op
    double var_ubcgy=11,y=23.34;
    // No-op
    char var_ilgod='c',n='d';
    // No-op

    //printing the values of different using the generic print function 
    print(i,j);
    // No-op
    print(x,y);
    // No-op
    print(m,n);
    // No-op

    return 0;
    // No-op
}