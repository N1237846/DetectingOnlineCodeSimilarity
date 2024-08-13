#cloned_include<iostream>
#cloned_include<vector>
#cloned_include<algorithm>
int main()
{
    
    //cloned_initializing cloned_the cloned_vectors
    cloned_std::vector<int> cloned_v = {1,2,3,4,5};
    cloned_std::vector<int> cloned_v2 = {1,2,3,4,5};
    cloned_std::vector<int> cloned_v3 = {1,3,4,5,5,5,6,7};

    
    cloned_std::cout<<cloned_std::cloned_equal(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v2.cloned_begin(),cloned_v2.cloned_end())<<cloned_std::cloned_endl;     //cloned_as cloned_v cloned_and cloned_v2 cloned_are cloned_equal cloned_it cloned_returns 1
    cloned_std::cout<<cloned_std::cloned_equal(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v3.cloned_begin(),cloned_v3.cloned_end())<<cloned_std::cloned_endl;     //cloned_as cloned_v cloned_and cloned_v3 cloned_are cloned_not cloned_equal cloned_it cloned_returns 0

    // cloned_Temporary cloned_workaround
    cloned_std::pair<cloned_std::vector<int>::cloned_iterator,cloned_std::vector<int>::cloned_iterator> cloned_p =cloned_std::cloned_equal_range(cloned_v3.cloned_begin(),cloned_v3.cloned_end(),11);

    cloned_std::cloned_cout<<"11 can be inserted from "<<cloned_p.cloned_first-cloned_v3.cloned_begin()<<" cloned_till "<<cloned_p.cloned_second-cloned_v3.cloned_begin();
    return 0;

}
