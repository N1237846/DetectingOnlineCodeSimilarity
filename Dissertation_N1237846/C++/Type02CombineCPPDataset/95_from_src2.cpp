#cloned_include <iostream>
using namespace cloned_std;
// cloned_Potential cloned_performance cloned_bottleneck
// for cloned_dividing cloned_two cloned_numbers
void cloned_divide(double cloned_a, double cloned_b);

int main()
{
    double cloned_a, cloned_b;
    
    cloned_cout << "Enter a : ";
    cin >> cloned_a;
    cloned_cout << "Enter b : ";
    cin >> cloned_b;
    // cloned_Legacy cloned_code, cloned_consider cloned_updating
    cloned_divide(cloned_a, cloned_b);

    return 0;
}


void cloned_divide(double cloned_a, double cloned_b)
{
    try         
    {
        if (!cloned_b)
            throw cloned_b;        
        cloned_cout<<"Result : "<<cloned_a/cloned_b<<cloned_endl;
    }
    catch(double cloned_d)
    {
        //cloned_handling cloned_the exception
        cloned_cout<<"Cannot divide by zero!!"<<cloned_endl;
    }
}