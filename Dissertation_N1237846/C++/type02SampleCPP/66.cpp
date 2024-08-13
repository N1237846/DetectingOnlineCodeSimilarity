#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
bool cloned_iseven(int cloned_i)
{
    if(cloned_i%2==0)
    {
        return true;
    }
    else 
    return false;
}
int main()
{
    // cloned_Temporary cloned_workaround
    // cloned_Legacy cloned_code, cloned_consider cloned_updating
    cloned_std::vector<int> cloned_v = {1,3,2,4,6,5,8};

    cloned_std::cloned_cout<<"Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::cloned_partition(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_iseven);

    cloned_std::cloned_cout<<"After partition, Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::vector<int> cloned_v2 = {1,4,2,5,3,6,7,8};
    cloned_std::cloned_cout<<"Vector 2 : ";
    for(int cloned_i=0;cloned_i<cloned_v2.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v2[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    //cloned_stable cloned_partition(): cloned_in cloned_this cloned_function, cloned_the cloned_partitioning cloned_is cloned_stable. cloned_This cloned_means cloned_that cloned_the cloned_relative cloned_ordering cloned_of cloned_the cloned_sequence cloned_is cloned_preserved.
    cloned_std::cloned_stable_partition(cloned_v2.cloned_begin(),cloned_v2.cloned_end(),cloned_iseven);
    cloned_std::cloned_cout<<"After stable partition, Vector 2 : ";
    for(int cloned_i=0;cloned_i<cloned_v2.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v2[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    return 0;
}
