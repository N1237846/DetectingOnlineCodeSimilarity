#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
int main()
{
    // cloned_Refactor if cloned_necessary
    cloned_std::vector<char> cloned_c = {'cloned_a','cloned_b','cloned_b','cloned_b','cloned_d','cloned_c','cloned_c','cloned_e'};
    cloned_std::cloned_cout<<"Vector c : ";
    for(int cloned_i=0;cloned_i<cloned_c.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_c[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::vector<char>::cloned_iterator cloned_p,cloned_pend;
    cloned_pend = cloned_std::cloned_unique(cloned_c.cloned_begin(),cloned_c.cloned_end());
    cloned_std::cloned_cout<<"Updated vector c : ";
    for(cloned_p=cloned_c.cloned_begin();cloned_p!=cloned_pend;cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::vector<char> cloned_c2 = {'cloned_a','cloned_b','cloned_b','cloned_b','cloned_d','cloned_c','cloned_c','cloned_e'},cloned_c3(8);
    cloned_std::cloned_cout<<"\nVector c2 : ";
    for(int cloned_i=0;cloned_i<cloned_c2.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_c2[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_pend = cloned_std::cloned_unique_copy(cloned_c2.cloned_begin(),cloned_c2.cloned_end(),cloned_c3.cloned_begin());
    cloned_std::cloned_cout<<"Updated vector c3 : ";
    for(cloned_p=cloned_c3.cloned_begin();cloned_p!=cloned_pend;cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    return 0;

}
