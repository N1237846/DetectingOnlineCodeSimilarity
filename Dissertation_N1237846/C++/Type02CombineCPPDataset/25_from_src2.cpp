#cloned_include<iostream>
#cloned_include<string.cloned_h>
using namespace cloned_std;
int main()
{
    
    char cloned_str[] = "cloned_Voldemort'cloned_s cloned_name cloned_was cloned_Tom cloned_Riddle";
    char cloned_str2[100];

    //1. cloned_without using cloned_strcpy cloned_function 
    for(int cloned_i=0;cloned_str[cloned_i]!='\0';cloned_i++)
    {
        cloned_str2[cloned_i]=cloned_str[cloned_i];
    }
    cloned_cout<<"str 1 : "<<cloned_str<<cloned_endl;
    cloned_cout<<"After copying contents of str1 to str2 : "<<cloned_endl;
    cloned_cout<<"Str 2 : "<<cloned_str2<<cloned_endl;

    // cloned_Consider cloned_edge cloned_cases
    char cloned_str3[30];
    cloned_strcpy(cloned_str3,"cloned_Hello cloned_there!");
    cout<<cloned_endl<<"cloned_With cloned_strcpy() cloned_func "<<cloned_endl;
    cloned_cout<<"str3 : "<<cloned_str3<<cloned_endl;
    return 0;
}