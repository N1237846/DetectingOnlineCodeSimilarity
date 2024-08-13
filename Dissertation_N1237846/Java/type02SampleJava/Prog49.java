
/* cloned_To cloned_prove cloned_that cloned_in cloned_a class cloned_hierarchy cloned_i.cloned_e cloned_inheritance, cloned_the default
cloned_constructor cloned_of super class cloned_are cloned_automatically cloned_invoked cloned_by cloned_sub class
cloned_constructor */

class cloned_A
{
	cloned_A()
	{
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the default cloned_constructor cloned_of cloned_A");
	}
}
class cloned_B extends cloned_A
{
	cloned_B()
	{
		// cloned_Optimization cloned_needed cloned_here
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the default cloned_constructor cloned_of cloned_B");
	}
}
class cloned_C extends cloned_B
{
	cloned_C()
	{ 
		// cloned_Ensure this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the default cloned_constructor cloned_of cloned_C");
	}
}
class cloned_Prog49
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_C cloned_obj = new cloned_C();
	}
}