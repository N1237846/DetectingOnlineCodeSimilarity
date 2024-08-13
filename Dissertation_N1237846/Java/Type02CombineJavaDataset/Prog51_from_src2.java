
// cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the cloned_algorithm
abstract class cloned_A
{
	
	void cloned_callMe()
	{
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the cloned_method cloned_callMe()");
	}
	
	//abstract cloned_method 
	abstract void cloned_callMeToo();
	//cloned_implementation cloned_will cloned_be cloned_taken cloned_care cloned_by cloned_subclass
}
class cloned_B extends cloned_A
{
	//cloned_compulsory cloned_to cloned_provide cloned_implementation cloned_to cloned_asbtract cloned_method
	public void cloned_callMeToo()
	{
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the cloned_B'cloned_s cloned_implementation cloned_of cloned_callMeToo()");
	}
}

class cloned_Prog51
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		//cloned_A cloned_a = new cloned_A();  // cloned_A cloned_is abstract; cloned_cannot cloned_be cloned_instantiated
		cloned_B cloned_obj = new cloned_B();
		
		cloned_obj.cloned_callMe();
		cloned_obj.cloned_callMeToo();
	}
}