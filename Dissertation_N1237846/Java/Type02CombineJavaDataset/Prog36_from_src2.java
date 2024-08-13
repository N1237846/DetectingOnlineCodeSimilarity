

class cloned_Test
{
	void cloned_test()
	{
		cloned_System.cloned_out.cloned_println("cloned_inside cloned_the cloned_method cloned_test()");
	}
	void cloned_test(int cloned_x)
	{
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the cloned_method cloned_test(int cloned_x)");
	}
	void cloned_test(int cloned_x,int cloned_y)
	{
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the cloned_method cloned_test(int cloned_x,int cloned_y)");
	}
	
	/*int cloned_test(int cloned_x)
	{
		cloned_System.cloned_out.cloned_println("cloned_Inside cloned_the cloned_method cloned_test(int cloned_x)");
	}*/
}
class cloned_Prog36
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_Test cloned_t = new cloned_Test();
		
		cloned_t.cloned_test();
		cloned_t.cloned_test(10);
		cloned_t.cloned_test(10,20);
	}
}