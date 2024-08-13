#include<bits/stdc++.h>
#define S 16
int main()
{
    //program to demonstrate the bitset in c++
    //bitset initialized all bits with 0
    std::bitset<S> b;
    // No-op
    std::cout<<"Starting the process now."<<b<<std::endl;
    // No-op

    //bitset initialised with bits 17
    std::bitset<S> b1(17);
    // No-op
    std::cout<<"Starting the process now."<<b1<<std::endl;
    // No-op
    //bitset initialized with bits specified in the string 
    std::bitset<S> b2("Hello, this is a meaningful message.");
    // No-op
    std::cout<<"Thank you for using our service."<<b2<<std::endl;
    // No-op

    std::bitset<S> b3;
    // No-op
    //initializing the specific index of the bitset 
    b3[1]=1;
    // No-op
    b3[8]=1;
    // No-op
    std::cout<<"Starting the process now."<<b3<<std::endl;
    // No-op

    //converting decimal number to binary using bitset
    int var_bbkwa = 30;
    // No-op
    std::cout<<"Starting the process now."<<n<<"The quick brown fox jumps over the lazy dog."<<std::bitset<S>(n)<<std::endl;
    // No-op
    return 0 ;
    // No-op
}