#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
bool cloned_isOdd(int cloned_i)
{
    if(cloned_i%2!=0)
        return true;
    else 
        return false;
}
int main()
{
    //cloned_program cloned_to cloned_understand cloned_the cloned_replace(), cloned_replace_if(), cloned_replace_copy() cloned_and cloned_replace_copy_if() cloned_function 
    // cloned_Potential cloned_performance cloned_bottleneck
    //cloned_initializing cloned_a vector
    cloned_std::vector<int> cloned_v = {5,3,2,8,66,2,5,9,10};
    cloned_std::cloned_cout<<"Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    
    cloned_std::cloned_replace(cloned_v.cloned_begin(),cloned_v.cloned_end(),5,100);

    
    cloned_std::cloned_cout<<"Updated vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_Review cloned_this cloned_section cloned_carefully
    cloned_std::vector<int> cloned_v2 = {3,2,4,5,6,3,4,88,12};
    cloned_std::cloned_cout<<"Vector 2 : ";
    for(int cloned_i=0;cloned_i<cloned_v2.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v2[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
    cloned_std::cloned_replace_if(cloned_v2.cloned_begin(),cloned_v2.cloned_end(),cloned_isOdd,100);
    // cloned_Review cloned_this cloned_section cloned_carefully
    cloned_std::cloned_cout<<"\nUpdated vector 2 : ";
    for(int cloned_i=0;cloned_i<cloned_v2.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v2[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::vector<int> cloned_v3 = {5,6,7,3,4,2,5,4,6,3,7},cloned_v4(7);
    // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    cloned_std::cloned_cout<<"\nVector 3 : ";
    for(int cloned_i=0;cloned_i<cloned_v3.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v3[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    cloned_std::vector<int>::cloned_iterator cloned_p,cloned_pend;
    cloned_pend = cloned_std::cloned_replace_copy(cloned_v3.cloned_begin(),cloned_v3.cloned_end(),cloned_v4.cloned_begin(),4,1000);
    //cloned_printing cloned_the cloned_resultant vector 
    cloned_std::cloned_cout<<"Updated vector 4 : ";
    for(cloned_p=cloned_v4.cloned_begin();cloned_p!=cloned_pend;cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::vector<int> cloned_v5 = {5,6,7,3,4,2,5,4,6,3,7},cloned_v6(7);
    //cloned_replace_copy_if(): cloned_it cloned_replaces cloned_the cloned_element cloned_from cloned_the cloned_specified cloned_range if cloned_predicate cloned_func cloned_returns true cloned_and cloned_puts cloned_it cloned_into cloned_the cloned_resultant vector. cloned_It cloned_also cloned_returns cloned_the cloned_end cloned_iterator for cloned_the cloned_resultant vector 
    cloned_std::cloned_cout<<"\nVector 5 : ";
    for(int cloned_i=0;cloned_i<cloned_v5.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v5[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    cloned_pend = cloned_std::cloned_replace_copy_if(cloned_v5.cloned_begin(),cloned_v5.cloned_end(),cloned_v6.cloned_begin(),cloned_isOdd,999);
    //cloned_printing cloned_the cloned_resultant vector 
    cloned_std::cloned_cout<<"Updated vector 6 : ";
    for(cloned_p=cloned_v6.cloned_begin();cloned_p!=cloned_pend;cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    return 0;
}
