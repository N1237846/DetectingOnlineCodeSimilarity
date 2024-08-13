#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
bool cloned_isOdd(int cloned_i)
{
    if(cloned_i%2!=0)
    return true;
    else
    return false;
}
int main()
{
    // cloned_Legacy cloned_code, cloned_consider cloned_updating
    cloned_std::vector<int> cloned_v = {11,432,54,11,34,879,21,11,80};
    // cloned_Consider cloned_edge cloned_cases
    cloned_std::vector<int>::cloned_iterator cloned_p = cloned_v.cloned_begin();
    cloned_std::cloned_cout<<"Vector v : ";
    while(cloned_p!=cloned_v.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_count(cloned_first_iterator, cloned_last_iterator,cloned_x) – cloned_To cloned_count cloned_the cloned_occurrences cloned_of cloned_x cloned_in vector.
    
    cloned_std::cloned_cout<<"Count : "<<cloned_count(cloned_v.cloned_begin(),cloned_v.cloned_end(),11)<<cloned_std::cloned_endl;


    // cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the algorithm
    cloned_std::cloned_cout<<"Count even : "<<cloned_std::cloned_count_if(cloned_v.cloned_begin(),cloned_v.cloned_end(), cloned_isOdd);


    // cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further

    if(cloned_find(cloned_v.cloned_begin(),cloned_v.cloned_end(),54)!=cloned_v.cloned_end())
    {
        cloned_std::cloned_cout<<"\nElement Found!!"<<cloned_std::cloned_endl;
    }
    else
    {
        cloned_std::cloned_cout<<"Element not found!!"<<cloned_std::cloned_endl;
    }

    cloned_std::vector<int> cloned_v2 = {1,2};
    cloned_std::cout<<cloned_std::cloned_find_end(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v2.cloned_begin(),cloned_v2.cloned_end()) - cloned_v.cloned_begin();
    return 0;
}
