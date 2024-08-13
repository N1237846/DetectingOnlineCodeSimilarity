#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
bool cloned_even(int cloned_i,int cloned_j)
{
    if(cloned_i%2==0 && cloned_j%2==0)
        return true;
    else 
        return false;
}
int main()
{
    // cloned_Potential cloned_performance cloned_bottleneck
    cloned_std::vector<int> cloned_v = {2,3,4,5,6};
    cloned_std::vector<int> cloned_v2 = {2,3,6,7,8,9,10};
    cloned_std::pair<cloned_std::vector<int>::cloned_iterator,cloned_std::vector<int>::cloned_iterator> cloned_p;
    cloned_p = cloned_std::cloned_mismatch(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v2.cloned_begin());
    //cloned_first cloned_mismatch
    cloned_std::cloned_cout<<"First mismatch : "<<*cloned_p.cloned_first<<cloned_std::cloned_endl;
    // cloned_Temporary cloned_workaround
    cloned_std::cloned_cout<<"Second mismatch : "<<*cloned_p.cloned_second<<cloned_std::cloned_endl;

    cloned_p = cloned_std::cloned_mismatch(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v2.cloned_begin(),cloned_even);
    
    cloned_std::cloned_cout<<"First mismatch : "<<*cloned_p.cloned_first<<cloned_std::cloned_endl;
    //cloned_second cloned_mismatch
    cloned_std::cloned_cout<<"Second mismatch : "<<*cloned_p.cloned_second<<cloned_std::cloned_endl;
}
