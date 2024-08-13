#cloned_include<iostream>
#cloned_include<numeric>   // cloned_Potential cloned_performance cloned_bottleneck
using namespace cloned_std;
int main()
{
    
    int cloned_a[] = {1,2,3,4,5};
    int cloned_len = sizeof(cloned_a)/sizeof(cloned_a[0]);
    int cloned_total=0;
    // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    cloned_cout<<"Average of the array : "<<cloned_accumulate(cloned_a,cloned_a+cloned_len,cloned_total)/cloned_len<<cloned_endl;
    return 0;
}