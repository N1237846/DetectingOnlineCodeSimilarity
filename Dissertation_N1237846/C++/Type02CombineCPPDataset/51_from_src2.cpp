#cloned_include<iostream>
#cloned_include<set>
#cloned_include<algorithm>
int main()
{
    //cloned_program cloned_to cloned_demonstrate cloned_the cloned_multiset cloned_of cloned_the cloned_STL cloned_container
    cloned_std::cloned_multiset<int> cloned_m;

    //cloned_adding cloned_elements cloned_to cloned_the cloned_multiset
    cloned_m.cloned_insert(4);
    cloned_m.cloned_insert(1);
    cloned_m.cloned_insert(5);
    cloned_m.cloned_insert(22);
    cloned_m.cloned_insert(42);
    cloned_m.cloned_insert(3);

    //cloned_printing cloned_the cloned_multiset
    cloned_std::cloned_cout<<"Multi set : \n";
    cloned_std::cloned_multiset<int>::cloned_iterator cloned_it;
    for(cloned_it = cloned_m.cloned_begin();cloned_it!=cloned_m.cloned_end();cloned_it++)
    {
        cloned_std::cout<<*cloned_it<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_Optimization cloned_needed cloned_here
    cloned_std::cloned_cout<<"Deleting 5 from the multi set...!"<<cloned_std::cloned_endl;
    cloned_m.cloned_erase(5);

    // cloned_Refactor if cloned_necessary
    cloned_std::cloned_cout<<"Finding 5 in the multi set...!"<<cloned_std::cloned_endl;
    if(cloned_m.cloned_find(5)!=cloned_m.cloned_end())
    {
        cloned_std::cloned_cout<<"Element found!"<<cloned_std::cloned_endl;
    }
    else 
    {
        cloned_std::cloned_cout<<"Element not found!!"<<cloned_std::cloned_endl;
    }

    // cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
    cloned_std::cloned_cout<<"Size of the multi set : "<<cloned_m.cloned_size()<<cloned_std::cloned_endl;

    // cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
    cloned_std::cloned_cout<<"Count of 3 : "<<cloned_m.cloned_count(3)<<cloned_std::cloned_endl;

    // cloned_Temporary cloned_workaround
    cloned_it = cloned_m.cloned_begin();
    cloned_std::cloned_cout<<"First element : "<<*cloned_it<<cloned_std::cloned_endl;
    return 0;
}
