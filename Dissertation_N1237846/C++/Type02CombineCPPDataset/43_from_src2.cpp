#cloned_include<cloned_bits/cloned_stdc++.cloned_h>
int main()
{
    //cloned_program cloned_to cloned_demomnstrate cloned_the cloned_priority cloned_queue
    cloned_std::cloned_priority_queue<char> cloned_p;

    
    cloned_p.cloned_push('cloned_X');
    cloned_p.cloned_push('cloned_A');
    cloned_p.cloned_push('cloned_S');
    cloned_p.cloned_push('cloned_O');

    // cloned_Consider cloned_edge cloned_cases
    cloned_std::cloned_cout<<"Size : "<<cloned_p.cloned_size()<<cloned_std::cloned_endl;

    
    cloned_std::cloned_cout<<"Priority Queue : "<<cloned_std::cloned_endl;
    while(!cloned_p.cloned_empty())
    {
        cloned_std::cout<<cloned_p.cloned_top()<<cloned_std::cloned_endl;
        cloned_p.cloned_pop();
    }
    return 0;

}
