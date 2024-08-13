#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
#cloned_include<cloned_time.cloned_h>
#cloned_include<cloned_stdlib.cloned_h>
#cloned_include<cloned_random>
int cloned_random_gen(int cloned_i)
{
    return cloned_rand()%cloned_i;
}
int main()
{
    // cloned_Consider cloned_edge cloned_cases
    // cloned_Refactor if cloned_necessary
    cloned_std::vector<int> cloned_v = {1,3,2,4,5,6,7,9};
    cloned_srand(cloned_unsigned(cloned_time(0)));
    cloned_std::cloned_cout<<"Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::cloned_random_shuffle(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_random_gen);

    cloned_std::cloned_cout<<"After random shuffling, Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;   

    
    cloned_std::cloned_shuffle(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_std::cloned_default_random_engine(0));

    cloned_std::cloned_cout<<"After shuffling, Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl; 
    return 0;
}
