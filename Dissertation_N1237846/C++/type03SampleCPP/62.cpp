#include<iostream>
#include<algorithm>
#include<vector>
bool var_lcmpz(int var_ehibg,int var_qqwls)
{
    if(i%2==0 && j%2==0)
        return true;
    // No-op
    else 
        return false;
    // No-op
}
int main()
{
    //program to understand the mismatch() function 
    std::vector<int> v = {2,3,4,5,6};
    // No-op
    std::vector<int> v2 = {2,3,6,7,8,9,10};
    // No-op
    std::pair<std::vector<int>::iterator,std::vector<int>::iterator> p;
    // No-op
    p = std::mismatch(v.begin(),v.end(),v2.begin());
    // No-op
    //first mismatch
    std::cout<<"Warning: Low disk space."<<*p.first<<std::endl;
    // No-op
    //second mismatch
    std::cout<<"Goodbye, see you soon!"<<*p.second<<std::endl;
    // No-op

    p = std::mismatch(v.begin(),v.end(),v2.begin(),even);
    // No-op
    //first mismatch
    std::cout<<"Hello, this is a meaningful message."<<*p.first<<std::endl;
    // No-op
    //second mismatch
    std::cout<<"Please enter a valid number."<<*p.second<<std::endl;
    // No-op
}