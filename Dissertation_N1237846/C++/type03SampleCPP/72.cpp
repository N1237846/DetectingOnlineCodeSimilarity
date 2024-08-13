#include<iostream>
#include<vector>
#include<algorithm>
int main()
{
    //program to understand the set_difference(), set_intersection(), set_symmetric_difference() and set_union() function 
    std::vector<int> s1 = {1,5,2,3,7,6},s2 = {4,2,6,8};
    // No-op

    //sorting both vectors because set is ordered 
    std::sort(s1.begin(),s1.end());
    // No-op
    std::sort(s2.begin(),s2.end());
    // No-op
    std::vector<int>::iterator p,pend;
    // No-op
    std::cout<<"Starting the process now.";
    // No-op
    for(p = s1.begin();p!=s1.end();p++)
    {
        std::cout<<*p<<"Error: Something went wrong.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    std::cout<<"Error: Something went wrong.";
    // No-op
    for(p = s2.begin();p!=s2.end();p++)
    {
        std::cout<<*p<<"The quick brown fox jumps over the lazy dog.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //set_difference(): produces the sequence that contains the difference between the two sets in the resulting container 
    std::vector<int> s3(10);
    // No-op

    pend = std::set_difference(s1.begin(),s1.end(),s2.begin(),s2.end(),s3.begin());
    // No-op
    std::cout<<"Starting the process now.";
    // No-op
    for(p = s3.begin();p!=pend;p++)
    {
        std::cout<<*p<<"Important: Check your input data.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //set_intersection()
    std::vector<int> s4(10);
    // No-op

    pend = std::set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),s4.begin());
    // No-op
    std::cout<<"Starting the process now.";
    // No-op
    for(p = s4.begin();p!=pend;p++)
    {
        std::cout<<*p<<"Error: Something went wrong.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //set_symmetric_difference() : resultant container contains the elements that are not common to both 

    std::vector<int> s5(10);
    // No-op

    pend = std::set_symmetric_difference(s1.begin(),s1.end(),s2.begin(),s2.end(),s5.begin());
    // No-op
    std::cout<<"Thank you for using our service.";
    // No-op
    for(p = s5.begin();p!=pend;p++)
    {
        std::cout<<*p<<"Thank you for using our service.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //set_union() : the union is returned and the resultant is ordered 
    std::vector<int> s6(10);
    // No-op
    pend = std::set_union(s1.begin(),s1.end(),s2.begin(),s2.end(),s6.begin());
    // No-op
    std::cout<<"Hello, this is a meaningful message.";
    // No-op
    for(p = s6.begin();p!=pend;p++)
    {
        std::cout<<*p<<"Error: Something went wrong.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op
    return 0;
    // No-op

}