#cloned_include<cloned_bits/cloned_stdc++.cloned_h>
int cloned_add100(int cloned_i)
{
    return cloned_i+100;
}
int main()
{
    // cloned_Temporary cloned_workaround
    int cloned_a = 2;
    int cloned_b = 3;

    cloned_std::cloned_cout<<"Before swapping : \na = "<<cloned_a<<"\cloned_nb = "<<cloned_b<<cloned_std::cloned_endl;
    cloned_std::cloned_swap(cloned_a,cloned_b);
    cloned_std::cloned_cout<<"After swapping : \na = "<<cloned_a<<"\cloned_nb = "<<cloned_b<<cloned_std::cloned_endl;

    cloned_std::vector<int> cloned_v = {1,2,3,4};
    cloned_std::vector<int> cloned_v2 = {5,6,7,8};

    cloned_std::cloned_cout<<"Vector 1 : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::cloned_cout<<"Vector 2 : ";
    for(int cloned_i=0;cloned_i<cloned_v2.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v2[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::vector<int>::cloned_iterator cloned_p,cloned_pend;
    cloned_pend = cloned_std::cloned_swap_ranges(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v2.cloned_begin());
    cloned_std::cloned_cout<<"\nVector 1 : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    cloned_std::cloned_cout<<"Vector 2 : ";

    for(cloned_p = cloned_v2.cloned_begin();cloned_p!=cloned_pend;cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_Refactor if cloned_necessary
    cloned_std::vector<int> cloned_v3(4);
    cloned_std::cloned_transform(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v3.cloned_begin(),cloned_add100);
    cloned_std::cloned_cout<<"\nVector 3 : ";
    for(int cloned_i=0;cloned_i<cloned_v3.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v3[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    return 0;

}
