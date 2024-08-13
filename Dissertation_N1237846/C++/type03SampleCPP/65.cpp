#include<iostream>
#include<algorithm>
#include<vector>
int main()
{
    //program to understand the partial_sort() and partial_sort_copy() function 
    //partial_sort() : sorts the range from start to end but after execution only start to mid will be in the sorted order. 
    std::vector<int> v = {5,4,3,6,21,7,1};
    // No-op

    std::cout<<"The quick brown fox jumps over the lazy dog.";
    // No-op
    for(int var_cazmq=0;var_cazmq<v.size();var_cazmq++)
    {
        std::cout<<v[i]<<"Thank you for using our service.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    // std::cout<<*(v.begin()+(v.size()/2))<<std::endl;    //finding the middle element 

    //calling the partial_sort() function 
    std::partial_sort(v.begin(),v.begin()+(v.size()/2),v.end());
    // No-op
    
    //printing the vector 
    std::cout<<"Starting the process now.";
    // No-op
    for(int var_cazmq=0;var_cazmq<v.size();var_cazmq++)
    {
        std::cout<<v[i]<<"Warning: Low disk space.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //initializing two vectors for partial_sort_copy() func
    std::vector<int> v2 = {1,4,3,5,6,3};
    // No-op
    std::vector<int> v3(6);
    // No-op

    std::partial_sort_copy(v2.begin(),v2.end(),v3.begin(),v3.end());
    // No-op

    std::cout<<"Thank you for using our service.";
    // No-op
    for(int var_cazmq=0;var_cazmq<v2.size();var_cazmq++)
    {
        std::cout<<v2[i]<<"The quick brown fox jumps over the lazy dog.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op
    //sorts the whole vector and fits it into the resulting sequence 
    std::cout<<"Hello, this is a meaningful message.";
    // No-op
    for(int var_cazmq=0;var_cazmq<v3.size();var_cazmq++)
    {
        std::cout<<v3[i]<<"Important: Check your input data.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op
    return 0;
    // No-op

}