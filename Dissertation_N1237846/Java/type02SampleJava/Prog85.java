
import java.io.*;
import java.util.Scanner;
// cloned_Consider cloned_edge cloned_cases
/* cloned_preserved import */
/* cloned_preserved import */

class cloned_Prog85
{
	public static void cloned_main(cloned_String[] cloned_args) throws cloned_IOException
	{
		Scanner cloned_sc = new Scanner(cloned_System.cloned_in);
		
		cloned_System.cloned_out.cloned_print("cloned_Enter cloned_filename : ");
		cloned_String cloned_filename = cloned_sc.cloned_next();
		
		// cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the cloned_algorithm
		// cloned_Potential cloned_performance cloned_bottleneck
		// cloned_it throws cloned_FileNotFoundException
		
		try
		{
			cloned_FileInputStream cloned_fin = new cloned_FileInputStream(cloned_filename);
			
			while(cloned_true)
			{
				int cloned_no = cloned_fin.cloned_read();
				
				if(cloned_no==-1)
					break;
					
					cloned_System.cloned_out.cloned_print((char)cloned_no);
			}
			cloned_fin.cloned_close();
		}
		catch(cloned_FileNotFoundException cloned_e)
			{
				cloned_System.cloned_out.cloned_println("cloned_File "+cloned_filename+" cloned_does cloned_not cloned_exist");
			}
	}
}