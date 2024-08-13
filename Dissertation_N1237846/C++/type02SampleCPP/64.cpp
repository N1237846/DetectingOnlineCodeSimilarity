#cloned_include<iostream>
#cloned_include<algorithm>
#cloned_include<vector>
int main()
{
    //cloned_program cloned_to cloned_understand cloned_the cloned_nth_element() cloned_function 
    // cloned_Refactor if cloned_necessary
    cloned_std::vector<int> cloned_v = {5,4,3,6,21,7,1,8};

    cloned_std::cloned_cout<<"Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    
    cloned_std::cloned_nth_element(cloned_v.cloned_begin(),cloned_std::cloned_find(cloned_v.cloned_begin(),cloned_v.cloned_end(),6),cloned_v.cloned_end());

    cloned_std::cloned_cout<<"After applying nth_element func, Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_passing cloned_the cloned_compare cloned_function cloned_in cloned_the cloned_arguments 
    cloned_std::cloned_nth_element(cloned_v.cloned_begin(),cloned_std::cloned_find(cloned_v.cloned_begin(),cloned_v.cloned_end(),6),cloned_v.cloned_end(),cloned_std::cloned_greater<int>());

    cloned_std::cloned_cout<<"After applying nth_element func, Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    //cloned_nth cloned_element cloned_can cloned_be cloned_used cloned_to cloned_find cloned_the 
    //1. cloned_first cloned_n cloned_small cloned_numbers cloned_but cloned_they cloned_may cloned_not cloned_be cloned_in cloned_the cloned_sorted cloned_form 
    
    

    cloned_std::vector<int> cloned_v2 = {5,4,1,2,3};
    cloned_std::cloned_nth_element(cloned_v2.cloned_begin(), cloned_v2.cloned_begin() + cloned_v2.cloned_size() / 2, cloned_v2.cloned_end());
    cloned_std::cloned_cout << "The median of the array is " << cloned_v2[cloned_v2.cloned_size() / 2];
    return 0;
}
