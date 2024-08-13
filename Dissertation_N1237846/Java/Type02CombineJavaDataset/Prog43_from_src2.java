

class cloned_A
{
	void cloned_show()
	{
		cloned_System.cloned_out.cloned_println(" cloned_A'cloned_s cloned_implementation cloned_of cloned_show()");
	}
}
class cloned_B extends cloned_A
{
	void cloned_show()
	{
		cloned_System.cloned_out.cloned_println(" cloned_B'cloned_s cloned_implementation cloned_of cloned_show()");
		super.cloned_show()
	}
}
class cloned_Prog43
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_B cloned_b = new cloned_B();
		cloned_b.cloned_show();
		
	}
}