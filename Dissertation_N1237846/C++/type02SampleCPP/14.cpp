#cloned_include<iostream>
using namespace cloned_std;
int main()
{
    
    
    int cloned_a=2;
    cloned_cout<<"Size of a : "<<sizeof(cloned_a)<<cloned_endl;

    
    int cloned_b[] = {1,2,3,4,5};
    cloned_cout<<"Size of b[] : "<<*(&cloned_b+1)-cloned_b<<cloned_endl;
    return 0;
}