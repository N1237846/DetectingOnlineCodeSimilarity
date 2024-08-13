
#cloned_include<iostream>
#cloned_include<cloned_cmath>

void cloned_myfunc(int cloned_i)
{
    cloned_std::cloned_cout<<"Value of i : "<<cloned_i<<cloned_std::cloned_endl;
}

void cloned_myfunc(double cloned_i)
{
    double cloned_intpart;
    double cloned_fracpart;

    cloned_fracpart = cloned_modf(cloned_i,&cloned_intpart);
    cloned_std::cloned_cout<<"Fractional part : "<<cloned_fracpart<<cloned_std::cloned_endl;
    cloned_std::cloned_cout<<"Integer part : "<<cloned_intpart<<cloned_std::cloned_endl;
}

int main()
{
    cloned_myfunc(3);
    cloned_myfunc(1.234);
    return 0;
}

