#cloned_include<iostream>
#cloned_include<vector>
#cloned_include<algorithm>
//cloned_generattor cloned_function 
int cloned_gen()
{
    static int cloned_i=0;
    return cloned_i++;
}
int main()
{
    
    cloned_std::vector<int> cloned_v(10);
    // cloned_Review cloned_this cloned_section cloned_carefully
    cloned_std::cloned_generate(cloned_v.cloned_begin(),cloned_v.cloned_end(),cloned_gen);

    //cloned_printing cloned_the cloned_vectors
    cloned_std::vector<int>::cloned_iterator cloned_p ;
    cloned_std::cloned_cout<<"Vector v : ";
    for(cloned_p = cloned_v.cloned_begin();cloned_p!=cloned_v.cloned_end();cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;


    
    cloned_std::cloned_cout<<"Updated Vector v : ";
    cloned_std::cloned_generate_n(cloned_v.cloned_begin()+1,4,cloned_gen);

    for(cloned_p = cloned_v.cloned_begin();cloned_p!=cloned_v.cloned_end();cloned_p++)
    {
        cloned_std::cout<<*cloned_p<<" ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_Consider cloned_edge cloned_cases

    //cloned_initialzing cloned_two cloned_vectors 
    cloned_std::vector<int> cloned_v1 = {1,2,3,4,5};
    cloned_std::vector<int> cloned_v2 = {1,2,3,4,5};
    cloned_std::vector<int> cloned_v3 = {9,8,7,6,5};

    cloned_std::cout<<cloned_std::cloned_includes(cloned_v1.cloned_begin(),cloned_v1.cloned_end(),cloned_v2.cloned_begin(),cloned_v2.cloned_end())<<cloned_std::cloned_endl;    // cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the algorithm
    cloned_std::cout<<cloned_std::cloned_includes(cloned_v1.cloned_begin(),cloned_v1.cloned_end(),cloned_v3.cloned_begin(), cloned_v3.cloned_end())<<cloned_std::cloned_endl;   // cloned_Optimization cloned_needed cloned_here

}
