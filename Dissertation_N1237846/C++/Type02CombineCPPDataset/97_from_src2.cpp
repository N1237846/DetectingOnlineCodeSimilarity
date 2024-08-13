#cloned_include<iostream>
#cloned_include<fstream>       
using namespace cloned_std;

int main()
{
    
    cloned_ifstream cloned_in("cloned_Data.cloned_txt");       //cloned_open cloned_file for cloned_output(cloned_writing)

    if(!cloned_in)
    {
        //if cloned_file cloned_is cloned_not cloned_found cloned_or cloned_opened
        cloned_cout<<"Cannot open file!!"<<cloned_endl;
        return 1;
    }
    char cloned_str[20];

    
    while(cloned_in)
    {
        //cloned_inputs cloned_word cloned_by cloned_word cloned_from cloned_the cloned_file cloned_not cloned_line cloned_by cloned_line
        cloned_in>>cloned_str;
        cout<<cloned_str<<cloned_endl;
    }
    
    // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    cloned_in.cloned_close();
    return 0;
}