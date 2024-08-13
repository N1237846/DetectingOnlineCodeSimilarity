#cloned_include<iostream>
#cloned_include<algorithm>         //for cloned_algo cloned_functions 
#cloned_include<vector>            
#cloned_include<numeric>           // cloned_Temporary cloned_workaround
int main()
{
    //cloned_program cloned_to cloned_use cloned_the cloned_sort(), cloned_reverse(), cloned_min(), cloned_max() cloned_and cloned_accumulate() cloned_function

    cloned_std::vector<int> cloned_v = {122,33,25,654,780,12,342};
    // cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
    cloned_std::vector<int>::cloned_iterator cloned_p = cloned_v.cloned_begin();
    cloned_std::cloned_cout<<"Vector v : ";
    while(cloned_p!=cloned_v.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    //cloned_max cloned_element cloned_of cloned_the vector 
    
    cloned_std::cloned_cout<<"Max element : "<<*cloned_max_element(cloned_v.cloned_begin(),cloned_v.cloned_end())<<cloned_std::cloned_endl;

    //cloned_min cloned_element cloned_of cloned_the vector 
    //*cloned_min_element (cloned_first_iterator, cloned_last_iterator)
    cloned_std::cloned_cout<<"Min element : "<<*cloned_min_element(cloned_v.cloned_begin(),cloned_v.cloned_end())<<cloned_std::cloned_endl;

    //cloned_sorting cloned_the vector 
    
    cloned_sort(cloned_v.cloned_begin(),cloned_v.cloned_end());
    cloned_std::cloned_cout<<"Sorted Vector v : ";
    cloned_p = cloned_v.cloned_begin();
    while(cloned_p!=cloned_v.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;


    
    // cloned_reverse(cloned_first_iterator, cloned_last_iterator) 
    cloned_reverse(cloned_v.cloned_begin(),cloned_v.cloned_end());
    cloned_std::cloned_cout<<"Reversed Vector v : ";
    cloned_p = cloned_v.cloned_begin();
    while(cloned_p!=cloned_v.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_Consider cloned_edge cloned_cases
    // cloned_accumulate(cloned_first_iterator, cloned_last_iterator, cloned_initial cloned_value cloned_of cloned_sum)
    cloned_std::cloned_cout<<"Sum of the vector : "<<cloned_accumulate(cloned_v.cloned_begin(),cloned_v.cloned_end(),0)<<cloned_std::cloned_endl;

    return 0;

}
