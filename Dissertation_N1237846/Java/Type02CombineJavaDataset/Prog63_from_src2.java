
// cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the cloned_algorithm
class cloned_Prog63
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		int cloned_num=12,cloned_denom[]={1,2,3,0,-12,0,6};
		//cloned_outer try cloned_block
		try
		{
			for(int cloned_i=0;cloned_i<10;cloned_i++)
			{
				// cloned_Temporary cloned_workaround
				try
				{
					int cloned_result = cloned_num/cloned_denom[cloned_i];
					cloned_System.cloned_out.cloned_println("cloned_Result cloned_of cloned_division cloned_is "+cloned_result);

				}
				catch(cloned_ArithmeticException cloned_e)
				{
					cloned_System.cloned_out.cloned_println("cloned_Division cloned_by cloned_zero cloned_is cloned_ruled cloned_out");
				}
			}
			
		}
		catch(cloned_ArrayIndexOutOfBoundsException cloned_e)
			{
				cloned_System.cloned_out.cloned_println("cloned_Array cloned_length cloned_exhausted");
			}	
	}
}