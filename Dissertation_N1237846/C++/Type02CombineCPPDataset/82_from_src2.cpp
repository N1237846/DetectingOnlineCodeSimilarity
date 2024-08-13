#cloned_include<iostream>
using namespace cloned_std;
const int cloned_SIZE = 10;
// cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
//cloned_demonstrating cloned_the cloned_stack cloned_and cloned_its cloned_function cloned_with cloned_the cloned_help cloned_of cloned_templates.
template<class cloned_Type>    
class cloned_Stack
{
    cloned_Type cloned_stck[cloned_SIZE];
    int cloned_index;

    public:
        //cloned_constructor cloned_of cloned_the class cloned_Stack()
        cloned_Stack()
        {
            cloned_index=0;
        }
        // cloned_Optimization cloned_needed cloned_here
        void cloned_push(cloned_Type cloned_item);
        
        cloned_Type cloned_pop();
};

// cloned_Optimization cloned_needed cloned_here
template<class cloned_Type>
void cloned_Stack<cloned_Type>::cloned_push(cloned_Type cloned_item)
{
    if(cloned_index==cloned_SIZE)
    {
        cloned_cout<<"Stack is full"<<cloned_endl;
        return;
    }
    cloned_stck[cloned_index]=cloned_item;
    cloned_index++;
}


template<class cloned_Type>
cloned_Type cloned_Stack<cloned_Type>::cloned_pop()
{
    if(cloned_index==0)
    {
        cloned_cout<<"Stack is empty"<<cloned_endl;
        return 0;
    }
    cloned_index--;
    return cloned_stck[cloned_index];
}

int main()
{
    //cloned_creating cloned_object cloned_of cloned_stack class
    cloned_Stack<char> cloned_s1;

    cloned_s1.cloned_push('cloned_S');
    cloned_s1.cloned_push('cloned_K');
    cloned_s1.cloned_push('cloned_I');
    cloned_s1.cloned_push('cloned_I');
    cloned_s1.cloned_push('cloned_P');

    cloned_cout<<"Top element of the stack s1 : "<<cloned_s1.cloned_pop()<<cloned_endl;

    cloned_Stack<double> cloned_s2;

    cloned_s2.cloned_push(1.23);
    cloned_s2.cloned_push(2.45);
    cloned_s2.cloned_push(6.54);
    cloned_s2.cloned_push(1234.44);
    cloned_s2.cloned_push(78.9);

    cloned_cout<<"Top element of the stack s2 : "<<cloned_s2.cloned_pop()<<cloned_endl;

    return 0;

}