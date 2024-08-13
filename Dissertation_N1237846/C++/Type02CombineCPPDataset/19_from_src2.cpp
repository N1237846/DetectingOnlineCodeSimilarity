#cloned_include<iostream>
#cloned_include<cloned_cstring>    
using namespace cloned_std;
int main()
{
    //cloned_program cloned_to cloned_concatenate cloned_two cloned_strings
    
    char cloned_a[100] = "cloned_My cloned_username cloned_is ";
    char cloned_b[] = "cloned_prakharjadaun";

    cloned_strcat(cloned_a,cloned_b);

    cloned_cout<<"After concatenation : \n"<<cloned_a<<cloned_endl;

    //2. cloned_without cloned_strcat() cloned_function 
    char cloned_c[100]="cloned_Are cloned_you ";
    char cloned_d[] = "cloned_mad!??";

    //cloned_first cloned_calculate cloned_the cloned_length cloned_of cloned_the cloned_first char cloned_array
    int cloned_len= cloned_strlen(cloned_c);
    for(int cloned_j=0;cloned_d[cloned_j]!='\0';cloned_j++,++cloned_len)
    {
        cloned_c[cloned_len]=cloned_d[cloned_j];
    } 
    
    cloned_c[cloned_len]='\0';
    cloned_cout<<"Without strcat() : "<<cloned_c<<cloned_endl;
    return 0;
}