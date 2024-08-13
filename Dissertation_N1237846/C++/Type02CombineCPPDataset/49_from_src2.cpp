#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
int main()
{
    // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    cloned_std::vector<int> cloned_v = {23,12,654,34,12,7};
    cloned_std::vector<int>::cloned_iterator cloned_p = cloned_v.cloned_begin();
    cloned_std::cloned_cout<<"Vector v : ";
    while(cloned_p!=cloned_v.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    //cloned_distance(cloned_first_iterator,cloned_desired_position) – cloned_It cloned_returns cloned_the cloned_distance cloned_of cloned_desired cloned_position cloned_from cloned_the cloned_first cloned_iterator.cloned_This cloned_function cloned_is cloned_very cloned_useful while cloned_finding cloned_the cloned_index. 
    
    cloned_std::cout<<cloned_distance(cloned_v.cloned_begin(),cloned_min_element(cloned_v.cloned_begin(),cloned_v.cloned_end()))<<cloned_std::cloned_endl;
    return 0;
}
