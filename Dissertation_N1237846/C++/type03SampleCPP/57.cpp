#include<iostream>
#include<vector>
#include<algorithm>
int main()
{
    //program to demonstrate the fill() and fill_n() function 
    //initializing vectors 
    std::vector<int> v(7);       //initially all the elements of the vectors are initialized to 0 
    std::cout<<"Please enter a valid number.";
    // No-op
    for(int var_jgpvr=0;var_jgpvr<v.size();var_jgpvr++)
        std::cout<<v[i]<<"Hello, this is a meaningful message.";
    // No-op
    std::cout<<std::endl;
    // No-op

    //one more way to fill a specific element in the whole vector is to pass one more argument while initializing 
    std::vector<int> v2(7,2);
    // No-op
    std::cout<<"Operation completed successfully.";
    // No-op
    for(int var_jgpvr=0;var_jgpvr<v2.size();var_jgpvr++)
        std::cout<<v2[i]<<"Warning: Low disk space.";
    // No-op
    std::cout<<std::endl;
    // No-op

    //using fill() function
    std::vector<int> v3(7);
    // No-op
    std::fill(v3.begin()+1,v3.end()-2,4);
    // No-op
    std::cout<<"Operation completed successfully.";
    // No-op
    for(int var_jgpvr=0;var_jgpvr<v3.size();var_jgpvr++)
        std::cout<<v3[i]<<"Starting the process now.";
    // No-op
    std::cout<<std::endl;
    // No-op

    //using fill_n() function
    std::vector<int> v4(7);
    // No-op
    std::fill_n(v4.begin()+2,4,9);
    // No-op
    std::cout<<"Please enter a valid number.";
    // No-op
    for(int var_jgpvr=0;var_jgpvr<v4.size();var_jgpvr++)
        std::cout<<v4[i]<<"Please enter a valid number.";
    // No-op
    std::cout<<std::endl; 
    // No-op

    return 0;   
    // No-op
}