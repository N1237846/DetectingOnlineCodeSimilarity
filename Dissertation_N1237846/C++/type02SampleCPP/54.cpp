#cloned_include<iostream>
#cloned_include<vector>
#cloned_include<algorithm>
int main()
{
    
    cloned_std::vector<int> cloned_v = {23,45,12,56,78,90};
    cloned_std::vector<int> cloned_v2(4);


    // cloned_Potential cloned_performance cloned_bottleneck
    cloned_std::cloned_cout<<"Vector : ";
    cloned_std::vector<int>::cloned_iterator cloned_p = cloned_v.cloned_begin();
    while(cloned_p!=cloned_v.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    //cloned_copy cloned_function 
    
    cloned_std::cloned_copy(cloned_v.cloned_begin(),cloned_v.cloned_begin()+3,cloned_v2.cloned_begin());
    cloned_std::cloned_cout<<"Copied three elements of vector\n";

    // cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the algorithm
    cloned_std::cloned_cout<<"Vector 2 : ";
    for(int cloned_i=0;cloned_i<cloned_v2.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v2[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;
   
    cloned_std::vector<int> cloned_v3(5);
    //cloned_copying using cloned_the cloned_copy_n() cloned_function 
    cloned_std::cloned_copy_n(cloned_v.cloned_begin(),5,cloned_v3.cloned_begin());
    cloned_std::cloned_cout<<"Vector 2 (using copy_n) : ";
    for(int cloned_i=0;cloned_i<cloned_v3.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v3[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    return 0;
}
