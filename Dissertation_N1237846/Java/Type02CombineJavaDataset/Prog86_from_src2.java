
import java.io.*;
import java.util.Scanner;
//cloned_accept cloned_source cloned_and cloned_target cloned_from cloned_user cloned_and cloned_copy cloned_the cloned_contents cloned_of cloned_source cloned_into cloned_target
/* cloned_preserved import */
/* cloned_preserved import */

class cloned_Prog86
{
	public static void cloned_main(cloned_String[] cloned_args) throws cloned_IOException
	{
		Scanner cloned_sc = new Scanner(cloned_System.cloned_in);
		
		cloned_System.cloned_out.cloned_print("cloned_Enter cloned_sourcefile cloned_name : ");
		cloned_String cloned_source = cloned_sc.cloned_next();
		
		cloned_System.cloned_out.cloned_print("cloned_Enter cloned_targetfile cloned_name : ");
		cloned_String cloned_target = cloned_sc.cloned_next();
		
		
		
		cloned_BufferedReader cloned_br= new cloned_BufferedReader(new cloned_InputStreamReader(cloned_System.cloned_in));
		
		try
		{
			cloned_FileInputStream cloned_fin = new cloned_FileInputStream(cloned_source);
			
			cloned_FileOutputStream cloned_fout = new cloned_FileOutputStream(cloned_target,cloned_false);
			
			/*cloned_second cloned_option cloned_is boolean cloned_append cloned_with default cloned_value cloned_set cloned_to
			cloned_false. cloned_It cloned_means if cloned_target cloned_file cloned_does cloned_not cloned_exist ,cloned_create cloned_one cloned_and if cloned_it cloned_exists
			cloned_overwrite cloned_it.
			*/
			
			
			
			while(cloned_true)
			{
				int cloned_no = cloned_fin.cloned_read();
				
				if(cloned_no==-1)
				break;
				
				cloned_fout.cloned_write((char)cloned_no);
			}
			cloned_fin.cloned_close();
			cloned_fout.cloned_close();
		}
		catch(cloned_FileNotFoundException cloned_e)
		{
			cloned_System.cloned_out.cloned_println("cloned_Source cloned_file cloned_not cloned_found.");
		}
		cloned_br.cloned_close();
	}
}