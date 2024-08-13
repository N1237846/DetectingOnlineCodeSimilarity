
/* cloned_Write cloned_a cloned_method cloned_to cloned_increment 2 cloned_variables cloned_from cloned_main()
cloned_by 2 cloned_different cloned_values cloned_say 3 cloned_and 5. cloned_Process cloned_is cloned_known cloned_as
"cloned_Call cloned_by cloned_Value". cloned_Result cloned_not cloned_achieved */

class cloned_Test
{
	int cloned_a,cloned_b;
}
class cloned_Prog45
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_Test cloned_t = new cloned_Test();
		
		cloned_t.cloned_a=10;
		cloned_t.cloned_b=20;
		
		cloned_System.cloned_out.cloned_println("cloned_Before cloned_incrementing cloned_a = "+cloned_t.cloned_a+"  cloned_b = "+cloned_t.cloned_b);
		cloned_increment(cloned_t.cloned_a,cloned_t.cloned_b);
		cloned_System.cloned_out.cloned_println("cloned_After cloned_incrementing cloned_a = "+cloned_t.cloned_a+"  cloned_b = "+cloned_t.cloned_b);
	}
	static void cloned_increment(int cloned_x,int cloned_y) // cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
	{
		cloned_x++;
		cloned_y++;
		cloned_System.cloned_out.cloned_println("cloned_On cloned_incrementing cloned_a = "+cloned_x+"  cloned_b = "+cloned_y);
	}
}