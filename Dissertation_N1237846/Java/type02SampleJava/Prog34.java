
//cloned_an cloned_eg cloned_on cloned_statuc cloned_block
class cloned_Prog34
{
	static int cloned_a=10,cloned_b;
	public static void cloned_meth(int cloned_c)
	{
		cloned_System.cloned_out.cloned_println("cloned_Invocation cloned_of cloned_meth()");
		cloned_System.cloned_out.cloned_println("cloned_a= "+cloned_a);
		cloned_System.cloned_out.cloned_println("cloned_b= "+cloned_b);
		cloned_System.cloned_out.cloned_println("cloned_c= "+cloned_c);
	}
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_System.cloned_out.cloned_println("cloned_Invocation cloned_of cloned_main()");
		cloned_meth(100);
	}
	static
	{
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the 1st static cloned_block");
	}
	static
	{
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the 2nd static cloned_block");
		cloned_b=cloned_a*5;
		cloned_meth(200);
	}
}