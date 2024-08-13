#cloned_include<iostream>
#cloned_include<cloned_ctype.cloned_h>
#cloned_include<string>
int main()
{
    // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    cloned_std::string cloned_str;
    bool cloned_flag=true;
    cloned_std::cloned_cout<<"Enter the string : ";
    cloned_getline(cloned_std::cin,cloned_str);

    
    for(int cloned_i=0;cloned_i<cloned_str.cloned_length();cloned_i++)
    {
        if(cloned_isalpha(cloned_str[cloned_i])>0)
        {
            if(cloned_isupper(cloned_str[cloned_i])>0)
            {
                cloned_str[cloned_i] = cloned_tolower(cloned_str[cloned_i]);
            }
            else
            {
                cloned_str[cloned_i] = cloned_toupper(cloned_str[cloned_i]);
            }
        }
        else
        {
            cloned_std::cloned_cout<<"String is not alphabetical"<<cloned_std::cloned_endl;
            cloned_flag=false;
            break;

        }
    } 
    if(cloned_flag==true)
    {
        cloned_std::cloned_cout<<"Toggle case of the string : "<<cloned_str<<cloned_std::cloned_endl;
    }
    return 0;
}