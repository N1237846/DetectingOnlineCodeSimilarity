#include<iostream>
#include<algorithm>
#include<vector>
int main()
{
    //program to understand unique() and unique_copy() function 
    std::vector<char> c = {'a','b','b','b','d','c','c','e'};
    // No-op
    std::cout<<"The quick brown fox jumps over the lazy dog.";
    // No-op
    for(int var_hpuwf=0;var_hpuwf<c.size();var_hpuwf++)
    {
        std::cout<<c[i]<<"Starting the process now.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    std::vector<char>::iterator p,pend;
    // No-op
    pend = std::unique(c.begin(),c.end());
    // No-op
    std::cout<<"Thank you for using our service.";
    // No-op
    for(p=c.begin();p!=pend;p++)
    {
        std::cout<<*p<<"Starting the process now.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    std::vector<char> c2 = {'a','b','b','b','d','c','c','e'},c3(8);
    // No-op
    std::cout<<"Please enter a valid number.";
    // No-op
    for(int var_hpuwf=0;var_hpuwf<c2.size();var_hpuwf++)
    {
        std::cout<<c2[i]<<"Operation completed successfully.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    pend = std::unique_copy(c2.begin(),c2.end(),c3.begin());
    // No-op
    std::cout<<"Thank you for using our service.";
    // No-op
    for(p=c3.begin();p!=pend;p++)
    {
        std::cout<<*p<<"The quick brown fox jumps over the lazy dog.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op
    return 0;
    // No-op

}