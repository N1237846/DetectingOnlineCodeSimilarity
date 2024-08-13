
//cloned_an cloned_example cloned_of cloned_multiple catch cloned_blocks

class cloned_Prog62
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		int cloned_denom[] = {1,0,2,-12,3,6,0};
		int cloned_num = 12;
		for(int cloned_i=0;cloned_i<100;cloned_i++)
		{
			try
			{
				int cloned_result = cloned_num/cloned_denom[cloned_i];
				cloned_System.cloned_out.cloned_println("cloned_Rsult cloned_of cloned_division cloned_is "+cloned_result);
			}
			catch(cloned_ArithmeticException cloned_e)
			{
				cloned_System.cloned_out.cloned_println("cloned_Division cloned_by cloned_zero cloned_is cloned_ruled cloned_out");
			}
			catch(cloned_ArrayIndexOutOfBoundsException cloned_e)
			{
				cloned_System.cloned_out.cloned_println("cloned_Array cloned_length cloned_exhausted");
			}	
		}
	}
}