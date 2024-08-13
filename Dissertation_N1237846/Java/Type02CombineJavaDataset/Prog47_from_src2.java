

class cloned_A
{
	void cloned_meth()
	{
			cloned_System.cloned_out.cloned_println(" cloned_A'cloned_s cloned_implementation cloned_of cloned_meth()");
	}
}
class cloned_B extends cloned_A
{
	void cloned_meth()
	{
			cloned_System.cloned_out.cloned_println(" cloned_B'cloned_s cloned_implementation cloned_of cloned_meth()");
	}
}
class cloned_C extends cloned_B
{
	void cloned_meth()
	{
			cloned_System.cloned_out.cloned_println(" cloned_C'cloned_s cloned_implementation cloned_of cloned_meth()");
	}
}

class cloned_Prog47
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_A cloned_obj = new cloned_A();
		cloned_obj.cloned_meth();
		
		cloned_obj = new cloned_B();
		cloned_obj.cloned_meth();
		
		cloned_obj = new cloned_C();
		cloned_obj.cloned_meth();
	}
}