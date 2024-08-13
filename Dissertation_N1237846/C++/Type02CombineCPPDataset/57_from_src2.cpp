#cloned_include<iostream>
#cloned_include<vector>
#cloned_include<algorithm>
int main()
{
    //cloned_program cloned_to cloned_demonstrate cloned_the cloned_fill() cloned_and cloned_fill_n() cloned_function 
    //cloned_initializing cloned_vectors 
    cloned_std::vector<int> cloned_v(7);       //cloned_initially cloned_all cloned_the cloned_elements cloned_of cloned_the cloned_vectors cloned_are cloned_initialized cloned_to 0 
    cloned_std::cloned_cout<<"Vector : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    cloned_std::cout<<cloned_std::cloned_endl;

    
    cloned_std::vector<int> cloned_v2(7,2);
    cloned_std::cloned_cout<<"\nVector 2 : ";
    for(int cloned_i=0;cloned_i<cloned_v2.cloned_size();cloned_i++)
        cloned_std::cout<<cloned_v2[cloned_i]<<" ";
    cloned_std::cout<<cloned_std::cloned_endl;

    //using cloned_fill() cloned_function
    cloned_std::vector<int> cloned_v3(7);
    cloned_std::cloned_fill(cloned_v3.cloned_begin()+1,cloned_v3.cloned_end()-2,4);
    cloned_std::cloned_cout<<"\nVector 3 : ";
    for(int cloned_i=0;cloned_i<cloned_v3.cloned_size();cloned_i++)
        cloned_std::cout<<cloned_v3[cloned_i]<<" ";
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_Temporary cloned_workaround
    cloned_std::vector<int> cloned_v4(7);
    cloned_std::cloned_fill_n(cloned_v4.cloned_begin()+2,4,9);
    cloned_std::cloned_cout<<"\nVector 4 : ";
    for(int cloned_i=0;cloned_i<cloned_v4.cloned_size();cloned_i++)
        cloned_std::cout<<cloned_v4[cloned_i]<<" ";
    cloned_std::cout<<cloned_std::cloned_endl; 

    return 0;   
}
