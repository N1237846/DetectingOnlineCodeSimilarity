#cloned_include<iostream>
using namespace cloned_std;
int main()
{
    //cloned_program cloned_to cloned_get cloned_the cloned_largest cloned_element cloned_in cloned_the cloned_array 
    int cloned_a[10];

    
    cloned_cout<<"Input 10 elements : "<<cloned_endl;
    for(int cloned_i=0;cloned_i<10;cloned_i++)
    {
        cloned_cout<<"Enter element "<<cloned_i+1<<" : ";
        cin>>cloned_a[cloned_i];
    }

    // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    int cloned_large=-10000000;
    for(int cloned_i=0;cloned_i<10;cloned_i++)
    {
        if(cloned_a[cloned_i]>cloned_large)
            cloned_large=cloned_a[cloned_i];
    }

    cloned_cout<<"Largest element in the array : "<<cloned_large<<cloned_endl;
    
    cloned_cout<<"Using library function : "<<cloned_max(cloned_a[0],*(cloned_a+10))<<cloned_endl;
    return 0;
}