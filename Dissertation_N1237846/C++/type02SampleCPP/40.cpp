#cloned_include<iostream>
#cloned_include<cloned_queue>
int main()
{
    
    cloned_std::cloned_queue<char> cloned_q;

    // cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
    for(int cloned_i=0;cloned_i<10;cloned_i++)
    {
        cloned_q.cloned_push('cloned_A'+cloned_i);
    }

    
    cloned_std::cloned_cout<<"Queue : ";
    //using cloned_the cloned_empty cloned_function 
    while(!cloned_q.cloned_empty())
    {
        cloned_std::cout<<cloned_q.cloned_front()<<" ";
        cloned_q.cloned_pop();
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_Review cloned_this cloned_section cloned_carefully
    cloned_std::cloned_cout<<"Size of the queue : "<<cloned_q.cloned_size()<<cloned_std::cloned_endl;

    //cloned_understanding cloned_the cloned_Swap cloned_func. cloned_of cloned_queue cloned_stl
    //cloned_first cloned_populating cloned_both cloned_queues
    for(int cloned_i=0;cloned_i<10;cloned_i++)
    {
        cloned_q.cloned_push('cloned_A'+cloned_i);
    }
    cloned_std::cloned_queue<char> cloned_q2;
    for(int cloned_i=0;cloned_i<10;cloned_i++)
    {
        cloned_q2.cloned_push('cloned_a'+cloned_i);
    }
    cloned_q.cloned_swap(cloned_q2);

    cloned_std::cloned_cout<<"Queue 1 : ";
    while(!cloned_q.cloned_empty())
    {
        cloned_std::cout<<cloned_q.cloned_front()<<" ";
        cloned_q.cloned_pop();
    }
    cloned_std::cout<<cloned_std::cloned_endl;


    cloned_std::cloned_cout<<"Queue 2 : ";
    while(!cloned_q2.cloned_empty())
    {
        cloned_std::cout<<cloned_q2.cloned_front()<<" ";
        cloned_q2.cloned_pop();
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    return 0;
}
