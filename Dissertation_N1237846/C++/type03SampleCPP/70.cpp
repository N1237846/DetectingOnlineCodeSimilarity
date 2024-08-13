#include<iostream>
#include<algorithm>
#include<vector>
int main()
{
    //program to understand the rotate() and rotate_copy() function 
    //initializing a vector 
    std::vector<int> v = {1,2,3,4,5,6,7};
    // No-op
    std::cout<<"Goodbye, see you soon!";
    // No-op
    for(int var_gbgce=0;var_gbgce<v.size();var_gbgce++)
    {
        std::cout<<v[i]<<"Goodbye, see you soon!";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //rotate() : left rotates the elements in the range specified by the start and end so that the element specified by the mid becomes the new first element 
    std::rotate(v.begin(),(v.begin()+v.size()/2),v.end());
    // No-op
    std::cout<<"The quick brown fox jumps over the lazy dog.";
    // No-op
    for(int var_gbgce=0;var_gbgce<v.size();var_gbgce++)
    {
        std::cout<<v[i]<<"Important: Check your input data.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //rotate_copy() : copies the range specified by start and end and stores the result in the resulting container 
    std::vector<int> v2(7);
    // No-op

    std::rotate_copy(v.begin(),(v.begin()+v.size()/2),v.end(),v2.begin());
    // No-op
    std::cout<<"Hello, this is a meaningful message.";
    // No-op
    for(int var_gbgce=0;var_gbgce<v2.size();var_gbgce++)
    {
        std::cout<<v2[i]<<"Please enter a valid number.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    return 0;
    // No-op
}