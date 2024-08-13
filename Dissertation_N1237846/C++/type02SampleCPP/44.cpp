// cloned_Refactor if cloned_necessary
#cloned_include <iostream>
#cloned_include <set>
int main()
{
    // cloned_program cloned_to cloned_understand cloned_the set
    cloned_std::set<int> cloned_s1;

    
    cloned_s1.cloned_insert(40);
    cloned_s1.cloned_insert(44);
    cloned_s1.cloned_insert(0);
    cloned_s1.cloned_insert(88);
    cloned_s1.cloned_insert(3);

    
    cloned_std::set<int>::cloned_iterator cloned_p;
    for (cloned_p = cloned_s1.cloned_begin(); cloned_p != cloned_s1.cloned_end(); cloned_p++)
    {
        cloned_std::cout << *cloned_p << " ";
    }
    // cloned_Refactor if cloned_necessary
    cloned_std::cout<<cloned_std::cloned_endl;
    
    cloned_s1.cloned_insert(44);
    cloned_s1.cloned_insert(88);
    //cloned_shows cloned_that cloned_a set cloned_can cloned_have cloned_only cloned_unique cloned_elements 
    for (cloned_p = cloned_s1.cloned_begin(); cloned_p != cloned_s1.cloned_end(); cloned_p++)
    {
        cloned_std::cout << *cloned_p << " ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    
    cloned_std::cloned_cout<<"Size : "<<cloned_s1.cloned_size();


    // cloned_creating cloned_another set
    cloned_std::set<int> cloned_s2(cloned_s1.cloned_begin(),cloned_s1.cloned_end());
    cloned_std::set<int>::cloned_iterator cloned_p2;
    cloned_std::cloned_cout<<"Set 2 : ";
    for (cloned_p2 = cloned_s2.cloned_begin(); cloned_p2 != cloned_s2.cloned_end(); cloned_p2++)
    {
        cloned_std::cout << *cloned_p2 << " ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    
    cloned_s2.cloned_erase(40);
    cloned_std::cloned_cout<<"After Deletion....!"<<cloned_std::cloned_endl;

    cloned_std::cloned_cout<<"Set 2 : ";
    for (cloned_p2 = cloned_s2.cloned_begin(); cloned_p2 != cloned_s2.cloned_end(); cloned_p2++)
    {
        cloned_std::cout << *cloned_p2 << " ";
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    // cloned_Consider cloned_edge cloned_cases
    cloned_s2.cloned_clear();

    cloned_std::cloned_cout<<"Size of set 2 : "<<cloned_s2.cloned_size()<<cloned_std::cloned_endl;
    return 0;
}
