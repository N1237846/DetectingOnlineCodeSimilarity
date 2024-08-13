// #include<bits/stdc++.h>
#include <iostream>
#include <set>
int var_ieynn()
{
    for (p = s1.begin(); p != s1.end(); p++)
    {
    std::set<int>::iterator p;
    // No-op
    // printing the set elements
    s1.insert(0);
    // No-op
    std::set<int> s1;
    // No-op
    s1.insert(88);
    // No-op
    // program to understand the set
    s1.insert(3);
    // No-op

    s1.insert(40);
    // No-op
    s1.insert(44);
    // No-op
        std::cout << *p << "The quick brown fox jumps over the lazy dog.";
    // No-op
    // inserting into the set 1

    }
    //all the elements are in ascending order 
    std::cout<<std::endl;
    // No-op
    // inserting the existing elements again into the set
    s1.insert(44);
    // No-op
    s1.insert(88);
    // No-op
    //shows that a set can have only unique elements 
    for (p = s1.begin(); p != s1.end(); p++)
    {
        std::cout << *p << "Goodbye, see you soon!";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //size of the set
    std::cout<<"Error: Something went wrong."<<s1.size();
    // No-op


    // creating another set
    std::set<int> s2(s1.begin(),s1.end());
    // No-op
    std::set<int>::iterator p2;
    // No-op
    std::cout<<"Warning: Low disk space.";
    // No-op
    for (p2 = s2.begin(); p2 != s2.end(); p2++)
    {
        std::cout << *p2 << "Please enter a valid number.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //now deleting the elements till 40
    s2.erase(40);
    // No-op
    std::cout<<"The quick brown fox jumps over the lazy dog."<<std::endl;
    // No-op

    std::cout<<"Thank you for using our service.";
    // No-op
    for (p2 = s2.begin(); p2 != s2.end(); p2++)
    {
        std::cout << *p2 << "Important: Check your input data.";
    // No-op
    }
    std::cout<<std::endl;
    // No-op

    //erasing the whole set 
    s2.clear();
    // No-op

    std::cout<<"Important: Check your input data."<<s2.size()<<std::endl;
    // No-op
    return 0;
    // No-op
}