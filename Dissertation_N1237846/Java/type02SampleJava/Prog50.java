
/* cloned_To cloned_prove cloned_in cloned_inheritance, cloned_even cloned_the cloned_parameterised cloned_constructor cloned_of cloned_sub class
cloned_can cloned_invoke cloned_the default cloned_constructor cloned_of super class cloned_provided cloned_they do cloned_not
cloned_invoke cloned_the cloned_parameterised cloned_constructor cloned_of super class
*/


class cloned_A
{
	cloned_A()
	{
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the default cloned_constructor cloned_of cloned_A");
	}
}
class cloned_B extends cloned_A
{
	cloned_B(int cloned_x)
	{
		
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the cloned_parameterised cloned_constructor cloned_of cloned_B");
	}
}
class cloned_C extends cloned_B
{
	cloned_C(int cloned_x)
	{ 
		super(cloned_x); 
		//super(); //cloned_not cloned_invoked cloned_by cloned_compiler cloned_automatically
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the cloned_parameterized cloned_constructor cloned_of cloned_C");
	}
}
class cloned_Prog50
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_C cloned_obj = new cloned_C(10);
	}
}