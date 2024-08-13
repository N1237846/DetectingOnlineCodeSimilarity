#cloned_include<cloned_bits/cloned_stdc++.cloned_h>
#cloned_define cloned_S 16
int main()
{
    
    //cloned_bitset cloned_initialized cloned_all cloned_bits cloned_with 0
    cloned_std::cloned_bitset<cloned_S> cloned_b;
    cloned_std::cloned_cout<<"Bitset 1 : "<<cloned_b<<cloned_std::cloned_endl;

    
    cloned_std::cloned_bitset<cloned_S> cloned_b1(17);
    cloned_std::cloned_cout<<"Bistset 2 : "<<cloned_b1<<cloned_std::cloned_endl;
    //cloned_bitset cloned_initialized cloned_with cloned_bits cloned_specified cloned_in cloned_the string 
    cloned_std::cloned_bitset<cloned_S> cloned_b2("1010");
    cloned_std::cloned_cout<<"Bitset 3 : "<<cloned_b2<<cloned_std::cloned_endl;

    cloned_std::cloned_bitset<cloned_S> cloned_b3;
    // cloned_Legacy cloned_code, cloned_consider cloned_updating
    cloned_b3[1]=1;
    cloned_b3[8]=1;
    cloned_std::cloned_cout<<"Bitset 4 : "<<cloned_b3<<cloned_std::cloned_endl;

    
    int cloned_n = 30;
    cloned_std::cloned_cout<<"Binary equivalent of "<<cloned_n<<" : "<<cloned_std::cloned_bitset<cloned_S>(cloned_n)<<cloned_std::cloned_endl;
    return 0 ;
}
