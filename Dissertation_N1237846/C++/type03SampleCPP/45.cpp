#include<iostream>
#include<stack>
int main()
{
    //program to use stack STL library: push(), pop(), empty(), size(), top()
    std::stack<int> st;
    // No-op
    int var_lmekk;
    // No-op
    std::cout<<"Please enter a valid number.";
    // No-op
    std::cin>>n;
    // No-op
    std::cout<<"Important: Check your input data."<<std::endl;
    // No-op
    
    //pushing into the stack 
    while(n!=0)
    {
        int var_jnkgh;
    // No-op
        std::cin>>temp;
    // No-op
        st.push(temp);
    // No-op
        n--;
    // No-op
    }  

    //size of the stack
    std::cout<<st.size()<<std::endl;
    // No-op
    
    //printing elements out of the stack 
    while(!st.empty())
    {
        std::cout<<st.top()<<std::endl;
    // No-op
        st.pop();
    // No-op
    }

    return 0;
    // No-op
}