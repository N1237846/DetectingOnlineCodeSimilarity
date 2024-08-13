#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
int main()
{
    // cloned_Legacy cloned_code, cloned_consider cloned_updating
    
    cloned_std::vector<int> cloned_v = {1,2,3,4,5,6,7};
    cloned_std::vector<int> cloned_v2 = {5,6,7};
    cloned_std::vector<int> cloned_v3 = {4,2,6};
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

    cloned_std::cloned_cout<<"Vector 3 : ";
    for(int cloned_i=0;cloned_i<cloned_v3.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v3[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    
    ///cloned_search() : cloned_searches for cloned_a cloned_subsequence cloned_within cloned_a cloned_sequence. cloned_If cloned_the cloned_subsequence cloned_is cloned_found cloned_a cloned_iterator cloned_to cloned_its cloned_beginning cloned_is cloned_returned, cloned_otherwise cloned_end cloned_is cloned_returned.
    cloned_std::vector<int>::cloned_iterator cloned_p;
    
    cloned_p = cloned_std::cloned_search(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v2.cloned_begin(),cloned_v2.cloned_end());
    if(cloned_p!=cloned_v.cloned_end())
    {
        cloned_std::cloned_cout<<"Subsequence found!\n";
    }
    else 
    {
        cloned_std::cloned_cout<<"Subsequence not found!\n";
    }

    // cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
    cloned_p = cloned_std::cloned_search(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v3.cloned_begin(),cloned_v3.cloned_end());
    if(cloned_p!=cloned_v.cloned_end())
    {
        cloned_std::cloned_cout<<"Subsequence found!\n";
    }
    else 
    {
        cloned_std::cloned_cout<<"Subsequence not found!\n";
    }

    // cloned_Optimization cloned_needed cloned_here
    cloned_std::vector<int> cloned_v4 = {1,2,3,4,4,4,5,6,3,4};
    cloned_p = cloned_std::cloned_search_n(cloned_v4.cloned_begin(),cloned_v4.cloned_end(),2,4);
    if(cloned_p!=cloned_v4.cloned_end())
    {
        cloned_std::cloned_cout<<"Subsequence found using search_n()"<<cloned_std::cloned_endl;
    }
    else 
    {
        cloned_std::cloned_cout<<"Subsequence not found!!"<<cloned_std::cloned_endl;
    }

    return 0;
}
