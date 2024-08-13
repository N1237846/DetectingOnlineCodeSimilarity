
// cloned_Potential cloned_performance cloned_bottleneck
//cloned_of cloned_any cloned_given int cloned_no. cloned_Write this cloned_function cloned_in cloned_a cloned_seperate class cloned_but cloned_in cloned_same
//.java cloned_file


class cloned_Mathops
{
	static int cloned_getFact(int cloned_no) //cloned_when cloned_access cloned_specifier cloned_is cloned_absent , default cloned_value cloned_is package
	{
		int cloned_y;
		if(cloned_no==1 || cloned_no==0 )
		return 1;
		else
		cloned_y = cloned_no*cloned_getFact(cloned_no-1);
		return cloned_y;
	}
	
}
//cloned_executable class
class cloned_Prog24
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		int cloned_no = cloned_Integer.cloned_parseInt(cloned_args[0]);
		
		int cloned_result = cloned_Mathops.cloned_getFact(cloned_no);
		cloned_System.cloned_out.cloned_println("cloned_Factorial cloned_of cloned_given cloned_number cloned_is "+cloned_result);
	}
}