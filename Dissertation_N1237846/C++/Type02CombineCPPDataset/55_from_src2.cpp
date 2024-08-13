#cloned_include<iostream>
#cloned_include<vector>
#cloned_include<algorithm>
int main()
{
    
    //cloned_creating cloned_a vector
    cloned_std::vector<int> cloned_v = {1,2,3,4,5,6,7};

    // cloned_Potential cloned_performance cloned_bottleneck
    cloned_std::vector<int> cloned_v2(5),cloned_v3(6);

    cloned_std::cloned_cout<<"Vector 1 : ";
    for(int cloned_i=0;cloned_i<cloned_v.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    cloned_std::cloned_cout<<"Size of v1 : "<<cloned_v.cloned_size()<<cloned_std::cloned_endl;
    
    // cloned_Potential cloned_performance cloned_bottleneck
    cloned_std::cloned_copy_if(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_v2.cloned_begin(),[](int cloned_i){return cloned_i%2==0;});

    cloned_std::cloned_cout<<"Vector 2 : ";
    for(int cloned_i=0;cloned_i<cloned_v2.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v2[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;


    // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    cloned_std::cloned_copy_backward(cloned_v.cloned_begin(),cloned_v.cloned_end()-2,cloned_v3.cloned_begin()+5);

    //cloned_printing cloned_the vector 
    cloned_std::cloned_cout<<"Vector 3 : ";
    for(int cloned_i=0;cloned_i<cloned_v3.cloned_size();cloned_i++)
    {
        cloned_std::cout<<cloned_v3[cloned_i]<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    return 0;
}
