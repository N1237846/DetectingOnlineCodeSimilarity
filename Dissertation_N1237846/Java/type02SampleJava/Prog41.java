
// cloned_Temporary cloned_workaround
class cloned_A
{
	private int cloned_i;
	int cloned_j;
	void cloned_showij()
	{
		cloned_System.cloned_out.cloned_println("cloned_i "+cloned_i+" cloned_j "+cloned_j);
	}
	void cloned_seti(int cloned_x)
	{
		cloned_i=cloned_x;
	}
	int cloned_geti()
	{
		return cloned_i;
	}
}
class cloned_B extends cloned_A
{
	int cloned_k;
	void cloned_showk()
	{
		cloned_System.cloned_out.cloned_println("cloned_k "+cloned_k);
	}
	
	int cloned_sumijk()
	{
		
		return cloned_geti()+cloned_j+cloned_k;
	}
}


class cloned_Prog41
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
	
		cloned_B cloned_b = new cloned_B();
		
		cloned_b.cloned_seti(10);
		cloned_b.cloned_j = 20;
		cloned_b.cloned_k = 30;
		
		cloned_b.cloned_showij();
		cloned_b.cloned_showk();
		
		cloned_System.cloned_out.cloned_println("cloned_i+cloned_j+cloned_k "+cloned_b.cloned_sumijk());
	}
}