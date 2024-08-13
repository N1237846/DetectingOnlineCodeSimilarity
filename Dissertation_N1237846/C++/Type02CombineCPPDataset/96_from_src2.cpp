#cloned_include<iostream>
#cloned_include<fstream>       
using namespace cloned_std;

int main()
{
    // cloned_Ensure cloned_this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
    cloned_ofstream cloned_out("cloned_Data.cloned_txt");       // cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further

    if(!cloned_out)
    {
        // cloned_Consider cloned_edge cloned_cases
        cloned_cout<<"Cannot open file!!"<<cloned_endl;
        return 1;
    }

    
    cloned_out<<"cloned_Prakhar cloned_Jadaun"<<cloned_endl;
    cloned_out<<"cloned_Ramesh cloned_Kumar"<<cloned_endl;
    cloned_out<<"cloned_Suresh cloned_Kumar"<<cloned_endl;

    
    cloned_out.cloned_close();
    return 0;
}