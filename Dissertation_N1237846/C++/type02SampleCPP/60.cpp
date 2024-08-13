#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
int main()
{
    // cloned_Refactor if cloned_necessary
    cloned_std::vector<int> cloned_v = {1,2,3,4,5};
    cloned_std::vector<int> cloned_v2 = {6,7,8,9,10};
    
    
    cloned_std::cloned_cout<<"Vector 1 : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::cloned_cout<<"\nVector 2 : ";
    for(int cloned_i=0;cloned_i<cloned_v2.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v2[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    //cloned_initializing cloned_the cloned_result vector 
    cloned_std::vector<int> cloned_v3(10);
    
    cloned_std::cloned_merge(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v2.cloned_begin(),cloned_v2.cloned_end(),cloned_v3.cloned_begin());
    cloned_std::cloned_cout<<"\nVector 3 : ";
    for(int cloned_i=0;cloned_i<cloned_v3.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v3[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::vector<int> cloned_v4(12);
    cloned_auto cloned_it = cloned_std::cloned_copy(cloned_v.cloned_begin(), cloned_v.cloned_end(), cloned_v4.cloned_begin());
    cloned_std::cloned_copy(cloned_v2.cloned_begin(), cloned_v2.cloned_end(), cloned_it);

    cloned_inplace_merge(cloned_v4.cloned_begin(),cloned_it,cloned_v4.cloned_end());

    cloned_std::cloned_cout<<"\nVector 4 : ";
    for(int cloned_i=0;cloned_i<cloned_v4.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v4[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    return 0;
}
