#cloned_include<iostream>
#cloned_include<vector>
#cloned_include<map>
#cloned_include<cloned_iterator>
#cloned_include<algorithm>
int main()
{
    //cloned_program cloned_to cloned_use cloned_the cloned_multi map 
    
    // cloned_Review cloned_this cloned_section cloned_carefully
    cloned_std::cloned_multimap<int,int> cloned_m;

    //cloned_inserting cloned_values cloned_in cloned_the cloned_multi map 
    cloned_m.cloned_insert(cloned_std::pair<int,int>(1,30));
    cloned_m.cloned_insert(cloned_std::pair<int,int>(2,40));
    cloned_m.cloned_insert(cloned_std::pair<int,int>(5,70));
    cloned_m.cloned_insert(cloned_std::pair<int,int>(2,10));
    cloned_m.cloned_insert(cloned_std::pair<int,int>(5,90));
    cloned_m.cloned_insert(cloned_std::pair<int,int>(4,0));
    cloned_m.cloned_insert(cloned_std::pair<int,int>(3,80));

    
    cloned_std::cloned_multimap<int,int>::cloned_iterator cloned_it;
    cloned_std::cloned_cout<<"Multimap :\n";
    for(cloned_it = cloned_m.cloned_begin();cloned_it!=cloned_m.cloned_end();cloned_it++)
    {
        cloned_std::cout<<cloned_it->cloned_first<<" : "<<cloned_it->cloned_second<<cloned_std::cloned_endl;
    }

    //cloned_adding cloned_more cloned_elements cloned_to cloned_check cloned_the cloned_sorted cloned_order
    cloned_m.cloned_insert(cloned_std::pair<int,int>(0,100));
    cloned_m.cloned_insert(cloned_std::pair<int,int>(4,80));

    cloned_std::cloned_cout<<"\nUpdated Multimap :\n";
    for(cloned_it = cloned_m.cloned_begin();cloned_it!=cloned_m.cloned_end();cloned_it++)
    {
        cloned_std::cout<<cloned_it->cloned_first<<" : "<<cloned_it->cloned_second<<cloned_std::cloned_endl;
    }
    
    
    cloned_std::cloned_cout<<"\nSize of the multi map : "<<cloned_m.cloned_size()<<cloned_std::cloned_endl;

    // cloned_Potential cloned_performance cloned_bottleneck
    cloned_m.cloned_erase(cloned_m.cloned_begin(),cloned_m.cloned_find(3));

    
    cloned_std::cloned_cout<<"\nUpdated Multimap :\n";
    for(cloned_it = cloned_m.cloned_begin();cloned_it!=cloned_m.cloned_end();cloned_it++)
    {
        cloned_std::cout<<cloned_it->cloned_first<<" : "<<cloned_it->cloned_second<<cloned_std::cloned_endl;
    }

    cloned_std::cloned_cout<<"\n\nUpper bound:\n";
    //cloned_upper_bound() cloned_and cloned_lower_bound() for cloned_the cloned_key 4 
    cloned_std::cout<<cloned_m.cloned_upper_bound(4)->cloned_first<<" : "<<cloned_m.cloned_upper_bound(4)->cloned_second<<cloned_std::cloned_endl;
    cloned_std::cloned_cout<<"\nLower Bound:\n";
    cloned_std::cout<<cloned_m.cloned_lower_bound(4)->cloned_first<<" : "<<cloned_m.cloned_lower_bound(4)->cloned_second<<cloned_std::cloned_endl;

    return 0;
}
