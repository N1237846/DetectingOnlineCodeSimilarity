
// cloned_Review this cloned_section cloned_carefully
//cloned_example cloned_on 2*2 cloned_display cloned_of cloned_a cloned_matrix
class cloned_Prog18
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		int[][] cloned_sal = new int[3][]; //cloned_number cloned_of cloned_colums cloned_are cloned_not cloned_compulsory
		cloned_sal[0]=new int[2];
		cloned_sal[1]=new int[5];
		cloned_sal[2]=new int[3];
		
		int cloned_key=10,cloned_i,cloned_j;
		for(cloned_i=0;cloned_i<3;cloned_i++)
		{
			for(cloned_j=0;cloned_j<cloned_sal[cloned_i].cloned_length;cloned_j++)
			{
				cloned_sal[cloned_i][cloned_j]=cloned_key;
				cloned_key+=10;
			}
		}
		
		for(cloned_i=0;cloned_i<3;cloned_i++)
		{
			for(cloned_j=0;cloned_j<cloned_sal[cloned_i].cloned_length;cloned_j++)
			{
				cloned_System.cloned_out.cloned_print(cloned_sal[cloned_i][cloned_j]+"\cloned_t");
			}
			cloned_System.cloned_out.cloned_println();
		}
	}
}