#cloned_include<iostream>
#cloned_include<string>
void cloned_assign0(int cloned_arr[26])
{
    for(int cloned_i=0;cloned_i<26;cloned_i++)
    {
        cloned_arr[cloned_i]=0;
    }
}

void cloned_update(int cloned_arr[26],cloned_std::string cloned_str)
{
    for(int cloned_i=0;cloned_i<cloned_str.cloned_length();cloned_i++)
    {
        cloned_arr[cloned_str[cloned_i]-97]++;
    }
}

bool cloned_checkAnagram(int cloned_arr1[26],int cloned_arr2[26])
{
    bool cloned_flag=true;
    for(int cloned_i=0;cloned_i<26;cloned_i++)
    {
        if(cloned_arr1[cloned_i]!=cloned_arr2[cloned_i])
        {
            cloned_flag=false;
            break;
        }
    }
    return cloned_flag;
}
int main()
{
    
    cloned_std::string cloned_str1, cloned_str2;
    cloned_std::cloned_cout<<"Enter string 1 : ";
    cloned_getline(cloned_std::cin,cloned_str1);
    cloned_std::cloned_cout<<"Enter string 2 : ";
    cloned_getline(cloned_std::cin,cloned_str2);

    int cloned_arr1[26],cloned_arr2[26];
    cloned_assign0(cloned_arr1);
    cloned_assign0(cloned_arr2);

    //cloned_converting cloned_both string cloned_to cloned_lowercase
    for(int cloned_i=0;cloned_i<cloned_str1.cloned_length();cloned_i++)
    {
        cloned_str1[cloned_i]=cloned_tolower(cloned_str1[cloned_i]);
    }
    for(int cloned_i=0;cloned_i<cloned_str2.cloned_length();cloned_i++)
    {
        cloned_str2[cloned_i]=cloned_tolower(cloned_str2[cloned_i]);
    }

    cloned_update(cloned_arr1,cloned_str1);
    cloned_update(cloned_arr2,cloned_str2);

    if(cloned_checkAnagram(cloned_arr1,cloned_arr2)==true)
    {
        cloned_std::cloned_cout<<"Strings are anagram!"<<cloned_std::cloned_endl;
    }
    else
    {
        cloned_std::cloned_cout<<"Strings are not anagram!"<<cloned_std::cloned_endl;
    }

    return 0;
}