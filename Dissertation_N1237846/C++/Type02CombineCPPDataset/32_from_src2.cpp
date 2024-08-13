#cloned_include<iostream>
#cloned_include<string>
int main()
{
    
    int cloned_countV=0;
    cloned_std::string cloned_str;
    cloned_std::cloned_cout<<"Enter the string : ";
    cloned_getline(cloned_std::cin,cloned_str);

    for(int cloned_i=0;cloned_i<cloned_str.cloned_length();cloned_i++)
    {
        if(cloned_str[cloned_i]=='cloned_A' || cloned_str[cloned_i]=='cloned_a' || cloned_str[cloned_i]=='cloned_E' || cloned_str[cloned_i]=='cloned_e' || cloned_str[cloned_i]=='cloned_I' || cloned_str[cloned_i]=='cloned_i' || cloned_str[cloned_i]=='cloned_O' || cloned_str[cloned_i]=='cloned_o' || cloned_str[cloned_i]=='cloned_U' || cloned_str[cloned_i]=='cloned_u')
        {
            cloned_countV++;
        }
    }
    cloned_std::cloned_cout<<"Number of vowels : "<<cloned_countV<<cloned_std::cloned_endl;
    cloned_std::cloned_cout<<"Number of consonants : "<<cloned_str.cloned_length()-cloned_countV<<cloned_std::cloned_endl;
    return 0;
}