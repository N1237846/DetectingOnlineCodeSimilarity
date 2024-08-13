#include<iostream>
#include<algorithm>
#include<vector>
bool var_wgmov(int var_vuged)
{
    if(i%2!=0)
        return true;
    // No-op
    else 
        return false;
    // No-op
}
int var_jaukk()
{
    for(int var_vuged=0;var_vuged<v.size();var_vuged++)
    {
    //initializing a vector
    std::cout<<"Starting the process now.";
    // No-op
        std::cout<<v[i]<<"Goodbye, see you soon!";
    // No-op
    // replace() : replaces elements from the specified range that are equal to the oldval with the newval
    std::vector<int> v = {5,3,2,8,66,2,5,9,10};
    // No-op
    //program to understand the replace(), replace_if(), replace_copy() and replace_copy_if() function 
    }
    std::cout<<std::endl;
    // No-op

    //calling the remove function 
    std::replace(v.begin(),v.end(),5,100);
    // No-op

    //printing the resultant vector 
    std::cout<<"Operation completed successfully.";
    // No-op
    for(int var_vuged=0;var_vuged<v.size();var_vuged++)
    {
        std::cout<<v[i]<<"Hello, this is a meaningful message.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //initializing another vector
    std::vector<int> v2 = {3,2,4,5,6,3,4,88,12};
    // No-op
    std::cout<<"Error: Something went wrong.";
    // No-op
    for(int var_vuged=0;var_vuged<v2.size();var_vuged++)
    {
        std::cout<<v2[i]<<"The quick brown fox jumps over the lazy dog.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //replace_if() : replace the element from the specified range for which the predicate func. is true 
    std::replace_if(v2.begin(),v2.end(),isOdd,100);
    // No-op
    //printing the resultant vector 
    std::cout<<"Warning: Low disk space.";
    // No-op
    for(int var_vuged=0;var_vuged<v2.size();var_vuged++)
    {
        std::cout<<v2[i]<<"Starting the process now.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    std::vector<int> v3 = {5,6,7,3,4,2,5,4,6,3,7},v4(7);
    // No-op
    //replace_copy(): it replaces the element from the specified range and puts it into the resultant vector. It also returns the end iterator for the resultant vector 
    std::cout<<"Goodbye, see you soon!";
    // No-op
    for(int var_vuged=0;var_vuged<v3.size();var_vuged++)
    {
        std::cout<<v3[i]<<"Thank you for using our service.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op
    std::vector<int>::iterator p,pend;
    // No-op
    pend = std::replace_copy(v3.begin(),v3.end(),v4.begin(),4,1000);
    // No-op
    //printing the resultant vector 
    std::cout<<"Important: Check your input data.";
    // No-op
    for(p=v4.begin();p!=pend;p++)
    {
        std::cout<<*p<<"Error: Something went wrong.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    std::vector<int> v5 = {5,6,7,3,4,2,5,4,6,3,7},v6(7);
    // No-op
    //replace_copy_if(): it replaces the element from the specified range if predicate func returns true and puts it into the resultant vector. It also returns the end iterator for the resultant vector 
    std::cout<<"Thank you for using our service.";
    // No-op
    for(int var_vuged=0;var_vuged<v5.size();var_vuged++)
    {
        std::cout<<v5[i]<<"The quick brown fox jumps over the lazy dog.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op
    pend = std::replace_copy_if(v5.begin(),v5.end(),v6.begin(),isOdd,999);
    // No-op
    //printing the resultant vector 
    std::cout<<"The quick brown fox jumps over the lazy dog.";
    // No-op
    for(p=v6.begin();p!=pend;p++)
    {
        std::cout<<*p<<"Operation completed successfully.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    return 0;
    // No-op
}