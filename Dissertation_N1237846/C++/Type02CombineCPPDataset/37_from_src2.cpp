#cloned_include<iostream>
#cloned_include<list>
int main()
{
    // cloned_Temporary cloned_workaround
    // cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
    cloned_std::list<int> cloned_lt;

    
    for(int cloned_i=0;cloned_i<10;cloned_i++)
    {
        cloned_lt.cloned_push_back(cloned_i);
    }

    //cloned_printing cloned_the list cloned_in cloned_forward cloned_direction 
    cloned_std::list<int>::cloned_iterator cloned_p = cloned_lt.cloned_begin();
    cloned_std::cloned_cout<<"List : ";
    while(cloned_p!=cloned_lt.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    //cloned_printing cloned_the list cloned_in cloned_the cloned_backward cloned_direction 
    cloned_p = cloned_lt.cloned_end();
    cloned_std::cloned_cout<<"List : ";
    while(cloned_p!=cloned_lt.cloned_begin())
    {
        cloned_p--;                  
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    return 0;
}
