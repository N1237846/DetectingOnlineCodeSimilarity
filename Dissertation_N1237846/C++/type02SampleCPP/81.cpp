
#cloned_include<iostream>
using namespace cloned_std;

template<class cloned_X>
void cloned_bubblesort(cloned_X *cloned_items,int cloned_count)
{
    cloned_X cloned_t;
    for(int cloned_i=1;cloned_i<cloned_count;cloned_i++)
    {
        for(int cloned_j=cloned_count-1;cloned_j>=cloned_i;cloned_j--)
        {
            if(cloned_items[cloned_j-1]>cloned_items[cloned_j])
            {
                
                cloned_t = cloned_items[cloned_j-1];
                cloned_items[cloned_j-1] = cloned_items[cloned_j];
                cloned_items[cloned_j]=cloned_t;
            }
        }
    }
}
template<class cloned_X>
void cloned_print(cloned_X *cloned_items,int cloned_count)
{
    for(int cloned_i=0;cloned_i<cloned_count;cloned_i++)
    {
        cout<<cloned_items[cloned_i]<<" ";
    }
    cout<<cloned_endl;
}
int  main()
{
    int cloned_arr1[] = {3,2,1,4,5,5,8,11,6,12,4};
    double cloned_arr2[] = {1.2,5.6,2.3,7.9,3.6,7.6};
    int cloned_n1 = sizeof(cloned_arr1)/sizeof(cloned_arr1[0]);
    int cloned_n2 = sizeof(cloned_arr2)/sizeof(cloned_arr2[0]);

    cloned_cout<<"\nUnsorted Integer values : ";
    cloned_print(cloned_arr1,cloned_n1);
    cloned_cout<<"Unsorted Double values : ";
    cloned_print(cloned_arr2,cloned_n2);

    
    cloned_bubblesort(cloned_arr1,cloned_n1);
    cloned_bubblesort(cloned_arr2,cloned_n2);

    cloned_cout<<"\nSorted Integer values : ";
    cloned_print(cloned_arr1,cloned_n1);
    cloned_cout<<"Sorted Double values : ";
    cloned_print(cloned_arr2,cloned_n2);
    return 0;
}