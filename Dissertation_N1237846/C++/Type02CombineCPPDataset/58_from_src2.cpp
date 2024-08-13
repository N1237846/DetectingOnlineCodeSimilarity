#cloned_include<iostream>
#cloned_include<vector>
#cloned_include<algorithm>
void cloned_add100(int cloned_i)
{
    if(cloned_i%2==0)
    {
        cloned_i = cloned_i + 100;
    }
    cloned_std::cout<<cloned_i<<" ";
}
int main()
{
    //cloned_program cloned_to cloned_demonstrate cloned_the cloned_find_first_of(), cloned_find_if() cloned_and cloned_for_each() cloned_function 
    cloned_std::vector<int> cloned_v = {1,999,3,4,5,6};
    cloned_std::vector<int> cloned_v2 = {9,8,7,1,999,3};

    
    cloned_std::vector<int>::cloned_iterator cloned_p = cloned_std::cloned_find_first_of(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v2.cloned_begin(),cloned_v2.cloned_end());
    cloned_std::cout<<*cloned_p<<cloned_std::cloned_endl;

    
    cloned_p = cloned_std::cloned_find_first_of(cloned_p+1,cloned_v.cloned_end(),cloned_v2.cloned_begin(),cloned_v2.cloned_end());
    cloned_std::cout<<*cloned_p<<cloned_std::cloned_endl;

    
    cloned_std::cout<<*cloned_std::cloned_find_if(cloned_v.cloned_begin(),cloned_v.cloned_end(),[](int cloned_i){if(cloned_i%2==0)return true;
    else return false;});

    
    cloned_std::cloned_cout<<"Vector v : ";
    cloned_std::cloned_for_each(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_add100);
    return 0;
}
