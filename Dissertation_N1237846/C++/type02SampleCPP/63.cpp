#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
int main()
{
    
    
    cloned_std::vector<int> cloned_v = {1,3,2};

    //cloned_sorting cloned_the vector 
    cloned_std::cloned_sort(cloned_v.cloned_begin(),cloned_v.cloned_end());

    cloned_std::cloned_cout<<"Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    //cloned_printing cloned_the cloned_all cloned_possible cloned_permutations
    do 
    {
        for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
        {
            cloned_std::cout<<cloned_v[cloned_i]<<" ";
        }
        cloned_std::cout<<cloned_std::cloned_endl;
    } while(cloned_std::cloned_next_permutation(cloned_v.cloned_begin(),cloned_v.cloned_end()));

    cloned_std::cloned_cout<<"After loop, Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;


    
    cloned_std::cloned_reverse(cloned_v.cloned_begin(),cloned_v.cloned_end());

    
    do 
    {
        for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
        {
            cloned_std::cout<<cloned_v[cloned_i]<<" ";
        }
        cloned_std::cout<<cloned_std::cloned_endl;
    } while(cloned_std::cloned_prev_permutation(cloned_v.cloned_begin(),cloned_v.cloned_end()));

    cloned_std::cloned_cout<<"After loop, Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    return 0;

}
