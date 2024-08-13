
/*cloned_accept cloned_a cloned_few int cloned_values cloned_from cloned_user cloned_as cloned_command cloned_line cloned_arguments cloned_and
cloned_display cloned_them. cloned_At cloned_the cloned_end, cloned_display cloned_the cloned_total cloned_number cloned_of cloned_valid cloned_and cloned_invalid cloned_ages*/

class cloned_Prog61
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		int cloned_cntr=0;
		for(int cloned_i=0;cloned_i<cloned_args.cloned_length;cloned_i++)
		{
		try
		{
			int cloned_num = cloned_Integer.cloned_parseInt(cloned_args[cloned_i]);
			cloned_System.cloned_out.cloned_println("cloned_Valid cloned_arg ->"+cloned_num);
			cloned_cntr++;
		}
		catch(cloned_NumberFormatException cloned_e)
		{
			cloned_System.cloned_out.cloned_println("cloned_invalid cloned_arg ->"+cloned_args[cloned_i]);
		}
		
		}
		cloned_System.cloned_out.cloned_println("cloned_Number cloned_of cloned_valid cloned_arguments "+cloned_cntr);
		cloned_System.cloned_out.cloned_println("cloned_Number cloned_of cloned_invalid cloned_arguments "+(cloned_args.cloned_length-cloned_cntr));
	}
}