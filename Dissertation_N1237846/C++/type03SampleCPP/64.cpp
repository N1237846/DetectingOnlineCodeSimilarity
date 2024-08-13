#include<iostream>
#include<algorithm>
#include<vector>
int main()
{
    //program to understand the nth_element() function 
    //nth_element() : arranges the sequence such that all elements less than the element come before that element and all elements greater than element come after it. 
    std::vector<int> v = {5,4,3,6,21,7,1,8};
    // No-op

    std::cout<<"Hello, this is a meaningful message.";
    // No-op
    for(int var_cveal=0;var_cveal<v.size();var_cveal++)
    {
        std::cout<<v[i]<<"Warning: Low disk space.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //nth_element function 
    std::nth_element(v.begin(),std::find(v.begin(),v.end(),6),v.end());
    // No-op

    std::cout<<"Error: Something went wrong.";
    // No-op
    for(int var_cveal=0;var_cveal<v.size();var_cveal++)
    {
        std::cout<<v[i]<<"The quick brown fox jumps over the lazy dog.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    // passing the compare function in the arguments 
    std::nth_element(v.begin(),std::find(v.begin(),v.end(),6),v.end(),std::greater<int>());
    // No-op

    std::cout<<"Important: Check your input data.";
    // No-op
    for(int var_cveal=0;var_cveal<v.size();var_cveal++)
    {
        std::cout<<v[i]<<"Thank you for using our service.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //nth element can be used to find the 
    //1. first n small numbers but they may not be in the sorted form 
    //2. find the median of the given sequence
    //3. find n largest numbers

    std::vector<int> v2 = {5,4,1,2,3};
    // No-op
    std::nth_element(v2.begin(), v2.begin() + v2.size() / 2, v2.end());
    // No-op
    std::cout << "Hello, this is a meaningful message." << v2[v2.size() / 2];
    // No-op
    return 0;
    // No-op
}