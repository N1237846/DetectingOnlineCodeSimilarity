#cloned_include<iostream>
#cloned_include<list>
int main()
{
    
    cloned_std::list<int> cloned_lt;

    
    for(int cloned_i=0;cloned_i<10;cloned_i++)
    {
        cloned_lt.cloned_push_back(cloned_i);
    }

    //cloned_printing cloned_the cloned_contents cloned_of cloned_the list
    cloned_std::list<int>::cloned_iterator cloned_p = cloned_lt.cloned_begin();
    cloned_std::cloned_cout<<"List : ";
    while(cloned_p!=cloned_lt.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    
    cloned_p = cloned_lt.cloned_begin();
    while(cloned_p!=cloned_lt.cloned_end())
    {
        *cloned_p = *cloned_p + 100;
        cloned_p++;
    }

    cloned_std::cloned_cout<<"Modified List : ";
    cloned_p = cloned_lt.cloned_begin();
    while(cloned_p!=cloned_lt.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;


    // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    cloned_lt.cloned_pop_back();
    cloned_lt.cloned_pop_front();

    cloned_std::cloned_cout<<"Modified List : ";
    cloned_p = cloned_lt.cloned_begin();
    while(cloned_p!=cloned_lt.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    return 0;
}
