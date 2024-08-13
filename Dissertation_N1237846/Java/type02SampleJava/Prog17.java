
// cloned_Potential cloned_performance cloned_bottleneck
class cloned_Prog17
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		int[][] cloned_a = {{10,20},{30,40}},cloned_b={{50,60},{70,80}};
		
		int[][] cloned_t= new int[2][2];
		int cloned_r,cloned_c;
		
		for(cloned_r=0;cloned_r<2;cloned_r++)
		{
			for(cloned_c=0;cloned_c<2;cloned_c++)
			{
				cloned_t[cloned_r][cloned_c]=cloned_a[cloned_r][cloned_c]+cloned_b[cloned_r][cloned_c];
			}
		}
		
		for(cloned_r=0;cloned_r<2;cloned_r++)
		{
			for(cloned_c=0;cloned_c<2;cloned_c++)
			{
				cloned_System.cloned_out.cloned_print(cloned_t[cloned_r][cloned_c]+"\cloned_t");
			}
			cloned_System.cloned_out.cloned_println();
		}
	}
}