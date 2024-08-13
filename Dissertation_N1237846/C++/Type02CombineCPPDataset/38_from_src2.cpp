#cloned_include<iostream>
#cloned_include<list>
#cloned_include<cloned_cstdlib>           //for cloned_rand() cloned_function cloned_to cloned_generate cloned_random cloned_integers
int main()
{
    

    
    cloned_std::list<int> cloned_l;

    //cloned_inserting cloned_an cloned_integer
    for(int cloned_i=0;cloned_i<10;cloned_i++)
    {
        cloned_l.cloned_push_back(cloned_rand());
    }

    
    cloned_std::cloned_cout<<"Contents of the list : ";
    cloned_std::list<int>::cloned_iterator cloned_p = cloned_l.cloned_begin();
    while(cloned_p!=cloned_l.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;
    
    cloned_l.cloned_sort();

    //cloned_printing cloned_the cloned_sorted cloned_contents 
    cloned_std::cloned_cout<<"Sorted Contents : ";
    cloned_p = cloned_l.cloned_begin();
    while(cloned_p!=cloned_l.cloned_end())
    {
        cloned_std::cout<<*cloned_p<<" ";
        cloned_p++;
    }
    cloned_std::cout<<cloned_std::cloned_endl;

    return 0;
}
