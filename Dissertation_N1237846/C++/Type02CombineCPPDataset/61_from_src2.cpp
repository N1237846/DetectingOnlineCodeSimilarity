#cloned_include<iostream>
#cloned_include<vector>
#cloned_include<algorithm>
int main()
{
    
    cloned_std::vector<int> cloned_v = {1,2,3,4,5,6,7};
    cloned_std::cloned_cout<<"Vector v : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    
    cloned_std::cloned_iter_swap(cloned_v.cloned_begin(),cloned_v.cloned_end()-1);
    cloned_std::cloned_cout<<"After swapping, Vector v : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    
    cloned_std::vector<char> cloned_c = {'cloned_a','cloned_v','cloned_d'};
    cloned_std::vector<char> cloned_c2 = {'cloned_u','cloned_i','cloned_w'};

    // cloned_Temporary cloned_workaround
    //cloned_returns true cloned_because cloned_c cloned_is cloned_less cloned_than cloned_the cloned_container cloned_c2
    cloned_std::cout<<cloned_std::cloned_lexicographical_compare(cloned_c.cloned_begin(),cloned_c.cloned_end(),cloned_c2.cloned_begin(),cloned_c2.cloned_end());
    return 0;
}
