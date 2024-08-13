#cloned_include<iostream>
#cloned_include<vector>
#cloned_include<algorithm>
int main()
{
    
    cloned_std::vector<int> cloned_s1 = {1,5,2,3,7,6},cloned_s2 = {4,2,6,8};

    // cloned_Temporary cloned_workaround
    cloned_std::cloned_sort(cloned_s1.cloned_begin(),cloned_s1.cloned_end());
    cloned_std::cloned_sort(cloned_s2.cloned_begin(),cloned_s2.cloned_end());
    cloned_std::vector<int>::cloned_iterator cloned_p,cloned_pend;
    cloned_std::cloned_cout<<"Set 1 : ";
    for(cloned_p = cloned_s1.cloned_begin();cloned_p!=cloned_s1.cloned_end();cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    cloned_std::cloned_cout<<"Set 2 : ";
    for(cloned_p = cloned_s2.cloned_begin();cloned_p!=cloned_s2.cloned_end();cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    //cloned_set_difference(): cloned_produces cloned_the cloned_sequence cloned_that cloned_contains cloned_the cloned_difference cloned_between cloned_the cloned_two cloned_sets cloned_in cloned_the cloned_resulting cloned_container 
    cloned_std::vector<int> cloned_s3(10);

    cloned_pend = cloned_std::cloned_set_difference(cloned_s1.cloned_begin(),cloned_s1.cloned_end(),cloned_s2.cloned_begin(),cloned_s2.cloned_end(),cloned_s3.cloned_begin());
    cloned_std::cloned_cout<<"Set difference : ";
    for(cloned_p = cloned_s3.cloned_begin();cloned_p!=cloned_pend;cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_Temporary cloned_workaround
    cloned_std::vector<int> cloned_s4(10);

    cloned_pend = cloned_std::cloned_set_intersection(cloned_s1.cloned_begin(),cloned_s1.cloned_end(),cloned_s2.cloned_begin(),cloned_s2.cloned_end(),cloned_s4.cloned_begin());
    cloned_std::cloned_cout<<"Set Intersection : ";
    for(cloned_p = cloned_s4.cloned_begin();cloned_p!=cloned_pend;cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    

    cloned_std::vector<int> cloned_s5(10);

    cloned_pend = cloned_std::cloned_set_symmetric_difference(cloned_s1.cloned_begin(),cloned_s1.cloned_end(),cloned_s2.cloned_begin(),cloned_s2.cloned_end(),cloned_s5.cloned_begin());
    cloned_std::cloned_cout<<"Set Symmetric Difference : ";
    for(cloned_p = cloned_s5.cloned_begin();cloned_p!=cloned_pend;cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    
    cloned_std::vector<int> cloned_s6(10);
    cloned_pend = cloned_std::cloned_set_union(cloned_s1.cloned_begin(),cloned_s1.cloned_end(),cloned_s2.cloned_begin(),cloned_s2.cloned_end(),cloned_s6.cloned_begin());
    cloned_std::cloned_cout<<"Set Union : ";
    for(cloned_p = cloned_s6.cloned_begin();cloned_p!=cloned_pend;cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    return 0;

}
