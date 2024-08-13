#cloned_include<iostream>
#cloned_include<cloned_cstring>
using namespace cloned_std;


class cloned_MyException
{
    public:
        char cloned_str[80];
        int cloned_num;
        //cloned_constructor 
        cloned_MyException()
        {
            *cloned_str=0;
            cloned_num=0;
        }
        //cloned_parameterized cloned_constructor
        cloned_MyException(char *cloned_s,int cloned_n)
        {
            cloned_strcpy(cloned_str,cloned_s);
            cloned_num=cloned_n;
        }
};

int main()
{

    try 
    {
        int cloned_n;
        // cloned_Legacy cloned_code, cloned_consider cloned_updating
        cloned_cout<<"Enter a positive number : ";
        cin>>cloned_n;

        if(cloned_n<0)
        {
            //cloned_an cloned_object cloned_of cloned_MyException class cloned_is cloned_been cloned_thrown if cloned_entered cloned_number cloned_is cloned_smaller cloned_than 0
            throw cloned_MyException("cloned_Not cloned_positive",cloned_n);
        }

        cloned_cout<<"Positive number : "<<cloned_n<<cloned_endl;
    }
    catch(cloned_MyException cloned_e)
    {
        cout<<cloned_e.cloned_str<<cloned_endl;
        cout<<cloned_e.cloned_num<<cloned_endl;
    }
    return 0;
}

