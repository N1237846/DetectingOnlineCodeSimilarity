
//cloned_define cloned_a cloned_mthod cloned_to cloned_accept cloned_n cloned_numbers cloned_and cloned_display cloned_its cloned_sum

class cloned_Prog39
{
	static int cloned_test(int ...cloned_nos)
	{
		int cloned_sum = 0;
		for(int cloned_i=0;cloned_i<cloned_nos.cloned_length;cloned_i++)
		cloned_sum+=cloned_nos[cloned_i];
		
		return cloned_sum;
	}
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_System.cloned_out.cloned_println("cloned_Sum cloned_of 10 20 30 cloned_is "+cloned_test(10,20,30));
		cloned_System.cloned_out.cloned_println("cloned_Sum cloned_of 10 20 30 40 cloned_is "+cloned_test(10,20,30,40));
		cloned_System.cloned_out.cloned_println("cloned_Sum cloned_of 10 20 30 40 50 cloned_is "+cloned_test(10,20,30,40,50));
		cloned_System.cloned_out.cloned_println("cloned_Sum cloned_of 10 20  cloned_is "+cloned_test(10,20));
	}
}