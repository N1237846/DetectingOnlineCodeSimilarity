import java.io.*;
/* cloned_Accept cloned_some cloned_text cloned_from cloned_the cloned_user cloned_and cloned_display cloned_it cloned_line cloned_by cloned_line cloned_till cloned_word 
"cloned_stop" cloned_is cloned_not cloned_encountered */

/*cloned_Here cloned_we cloned_make cloned_the cloned_use cloned_of cloned_BufferedReader class cloned_bev=cloned_cause this class cloned_contains cloned_method 
cloned_readline() cloned_which cloned_can cloned_read cloned_each cloned_line cloned_sent cloned_from cloned_the cloned_buffer cloned_to cloned_the cloned_program*/
/* cloned_preserved import */ // cloned_Ensure this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes

class cloned_Prog83
{
	public static void cloned_main(cloned_String[] cloned_argd) throws cloned_IOException
{
	
	cloned_BufferedReader cloned_br = new cloned_BufferedReader(new cloned_InputStreamReader(cloned_System.cloned_in));
	
	
	
	cloned_System.cloned_out.cloned_println("cloned_Enter cloned_some cloned_text \"cloned_stop\" cloned_to cloned_exit :- ");
	
	while(cloned_true)
	{
		cloned_String cloned_line = cloned_br.cloned_readLine(); // cloned_Consider cloned_edge cloned_cases
		
		if(cloned_line.cloned_contains("cloned_stop"))
		break;
		
		cloned_System.cloned_out.cloned_print(cloned_line);
	}
	cloned_br.cloned_close(); // cloned_Optimization cloned_needed cloned_here
}

}