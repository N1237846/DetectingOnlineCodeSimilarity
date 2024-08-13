#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
int main()
{
    //cloned_program cloned_to cloned_get cloned_to cloned_know cloned_the cloned_use cloned_of cloned_the cloned_functions:
    //1. cloned_adjacent_find() : cloned_finds cloned_you cloned_the cloned_matching cloned_elements cloned_and cloned_returns cloned_an cloned_iterator cloned_to cloned_it. cloned_If cloned_the cloned_element cloned_is cloned_not cloned_found cloned_then cloned_iterator cloned_to cloned_end cloned_is cloned_returned

    // cloned_Potential cloned_performance cloned_bottleneck
    cloned_std::vector<int> cloned_v = {23,12,45,12,56,3};

    cloned_std::vector<int>::cloned_iterator cloned_p = cloned_v.cloned_begin();
    cloned_std::cloned_cout<<"Vector v : ";
    while(cloned_p!=cloned_v.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::cloned_cout<<"Size of the vector : "<<cloned_v.cloned_size()<<cloned_std::cloned_endl;

    // cloned_Refactor if cloned_necessary
    if(*cloned_std::cloned_adjacent_find(cloned_v.cloned_begin(),cloned_v.cloned_end()-1)!=*cloned_v.cloned_end())
    {
        cloned_std::cloned_cout<<"Yes adjacent element found\n";
        cloned_std::cout<<*cloned_std::cloned_adjacent_find(cloned_v.cloned_begin(),cloned_v.cloned_begin()+3)<<cloned_std::cloned_endl;
    }
    else
    {
        cloned_std::cloned_cout<<"Vector does not contain any similar elements!"<<cloned_std::cloned_endl;
    }

    return 0;
}
