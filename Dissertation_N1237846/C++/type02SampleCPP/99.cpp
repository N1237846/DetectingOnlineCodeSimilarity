#cloned_include<iostream>
#cloned_include<fstream>       
using namespace cloned_std;
//cloned_reading cloned_from cloned_a cloned_file using cloned_seekg()
int main()
{
    char cloned_ch;
    //cloned_creating cloned_an cloned_object cloned_of cloned_ifstream cloned_object
    cloned_ifstream cloned_in("cloned_Data.cloned_txt");       

    if(!cloned_in)
    {
        
        cloned_cout<<"Cannot open file!!"<<cloned_endl;
        return 1;
    }
    char cloned_str[20];
    
    cloned_in.cloned_seekg(0,cloned_ios::cloned_beg);

    while(cloned_in.cloned_get(cloned_ch))
    {
        cout<<cloned_ch;
    }
    
    //cloned_closing cloned_the cloned_object
    cloned_in.cloned_close();
    return 0;
}