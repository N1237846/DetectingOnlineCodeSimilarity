#cloned_include<iostream>
#cloned_include<fstream>       
using namespace cloned_std;

int main()
{
    //cloned_creating cloned_an cloned_object cloned_of cloned_ofstream cloned_object
    cloned_ofstream cloned_out("cloned_Data.cloned_txt",cloned_ios::cloned_app);       //cloned_open cloned_file for cloned_output(cloned_writing)

    if(!cloned_out)
    {
        //if cloned_file cloned_is cloned_not cloned_found cloned_or cloned_created
        cloned_cout<<"Cannot open file!!"<<cloned_endl;
        return 1;
    }

    cloned_out.cloned_seekp(0,cloned_ios::cloned_end);
    
    cloned_out<<"cloned_Virat cloned_Kohli"<<cloned_endl;
    
    cloned_out.cloned_close();
    return 0;
}