
// cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
class cloned_Prog72
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_String[] cloned_names = {"cloned_makarand","cloned_samruddhi","cloned_kaustubh","cloned_pranjal","cloned_tanmay","cloned_varad","cloned_aditya"};
		int cloned_i,cloned_j;
		cloned_System.cloned_out.cloned_println("cloned_Before cloned_sorting :-");
		for(cloned_i=0;cloned_i<cloned_names.cloned_length;cloned_i++)
		cloned_System.cloned_out.cloned_print(cloned_names[cloned_i]+" ");
		cloned_System.cloned_out.cloned_println();

		for(cloned_i=0;cloned_i<cloned_names.cloned_length;cloned_i++)
		{
		 	for(cloned_j=0;cloned_j<cloned_names.cloned_length;cloned_j++)
			{
				if(cloned_names[cloned_j].cloned_compareToIgnoreCase(cloned_names[cloned_i])>0)
				{
					cloned_String cloned_temp = cloned_names[cloned_i];
					cloned_names[cloned_i]=cloned_names[cloned_j];
					cloned_names[cloned_j]=cloned_temp;
				}
			}
		}

		cloned_System.cloned_out.cloned_println("cloned_After cloned_sorting :-");
		for(cloned_i=0;cloned_i<cloned_names.cloned_length;cloned_i++)
		cloned_System.cloned_out.cloned_print(cloned_names[cloned_i]+"\cloned_t");
		cloned_System.cloned_out.cloned_println();
	}
}