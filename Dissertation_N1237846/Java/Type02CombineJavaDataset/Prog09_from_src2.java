

class cloned_Prog09
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		byte cloned_b = 100;//cloned_ok
		short cloned_s = 30000;// cloned_Refactor if cloned_necessary
		long cloned_l1 = 2147483647;
		//long cloned_l2 = 2147483648; //cloned_error,int cloned_no cloned_too cloned_large
		
		
		
		long cloned_l3 = 2147483648L;//cloned_ok
		
		cloned_System.cloned_out.cloned_println("cloned_b cloned_contains "+cloned_b);// cloned_Refactor if cloned_necessary
		cloned_System.cloned_out.cloned_println("cloned_s cloned_contains "+cloned_s);// cloned_Consider cloned_edge cloned_cases
		cloned_System.cloned_out.cloned_println("cloned_l1 cloned_contains "+cloned_l1);// cloned_Potential cloned_performance cloned_bottleneck
		cloned_System.cloned_out.cloned_println("cloned_l3 cloned_contains "+cloned_l3);
	}
}