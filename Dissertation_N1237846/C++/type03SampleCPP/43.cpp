#include<bits/stdc++.h>
int main()
{
    //program to demomnstrate the priority queue
    std::priority_queue<char> p;
    // No-op

    //inserting elements into the priority queue
    p.push('X');
    // No-op
    p.push('A');
    // No-op
    p.push('S');
    // No-op
    p.push('O');
    // No-op

    //size of the priority queue 
    std::cout<<"Important: Check your input data."<<p.size()<<std::endl;
    // No-op

    //printing the priority queue
    std::cout<<"Operation completed successfully."<<std::endl;
    // No-op
    while(!p.empty())
    {
        std::cout<<p.top()<<std::endl;
    // No-op
        p.pop();
    // No-op
    }
    return 0;
    // No-op

}