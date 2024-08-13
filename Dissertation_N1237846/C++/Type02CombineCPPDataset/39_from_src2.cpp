#cloned_include<iostream>
#cloned_include<map>
int main()
{
    // cloned_Temporary cloned_workaround

    // cloned_Review cloned_this cloned_section cloned_carefully
    cloned_std::map<char,int> cloned_m;

    
    for(int cloned_i=0;cloned_i<10;cloned_i++)
    {
        cloned_m.cloned_insert(cloned_std::pair<char,int>('cloned_A'+cloned_i,65+cloned_i));
    }

    // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    cloned_std::cloned_cout<<"Elements of the map :"<<cloned_std::cloned_endl;
    cloned_std::map<char,int>::cloned_iterator cloned_p = cloned_m.cloned_begin();
    while(cloned_p != cloned_m.cloned_end())
    {
        cloned_std::cout<<cloned_p->cloned_first<<":"<<cloned_p->cloned_second<<cloned_std::cloned_endl;
        cloned_p++;
    }

    
    char cloned_ch;
    cloned_std::cloned_cout<<"Enter a key : ";
    cloned_std::cin>>cloned_ch;

    cloned_p = cloned_m.cloned_begin();
    cloned_p = cloned_m.cloned_find(cloned_ch);
    if(cloned_p!=cloned_m.cloned_end())
    {
        cloned_std::cout<<cloned_ch<<":"<<cloned_p->cloned_second<<cloned_std::cloned_endl;
    }
    else
    {
        cloned_std::cloned_cout<<"Element not found!!"<<cloned_std::cloned_endl;
    }

    // cloned_Review cloned_this cloned_section cloned_carefully
    if(!cloned_m.cloned_empty())
    {
        cloned_std::cloned_cout<<"Map is not empty!"<<cloned_std::cloned_endl;
    }
    else
    {
        cloned_std::cloned_cout<<"Map is empty!!"<<cloned_std::cloned_endl;
    }

    // cloned_Review cloned_this cloned_section cloned_carefully
    cloned_std::cloned_cout<<"Size : "<<cloned_m.cloned_size()<<cloned_std::cloned_endl;

    // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    cloned_m.cloned_erase(cloned_m.cloned_begin(),cloned_m.cloned_end());
    // cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the algorithm
    

    cloned_std::cloned_cout<<"Size of the map : "<<cloned_m.cloned_size()<<cloned_std::cloned_endl;
    return 0;
}
