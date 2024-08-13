#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
int main()
{
    
    
    cloned_std::vector<int> cloned_v = {1,2,3,4,5,6,7};
    cloned_std::cloned_cout<<"Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    
    cloned_std::cloned_rotate(cloned_v.cloned_begin(),(cloned_v.cloned_begin()+cloned_v.cloned_size()/2),cloned_v.cloned_end());
    cloned_std::cloned_cout<<"updated Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    //cloned_rotate_copy() : cloned_copies cloned_the cloned_range cloned_specified cloned_by cloned_start cloned_and cloned_end cloned_and cloned_stores cloned_the cloned_result cloned_in cloned_the cloned_resulting cloned_container 
    cloned_std::vector<int> cloned_v2(7);

    cloned_std::cloned_rotate_copy(cloned_v.cloned_begin(),(cloned_v.cloned_begin()+cloned_v.cloned_size()/2),cloned_v.cloned_end(),cloned_v2.cloned_begin());
    cloned_std::cloned_cout<<"updated Vector 2 : ";
    for(int cloned_i=0;cloned_i<cloned_v2.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v2[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    return 0;
}
