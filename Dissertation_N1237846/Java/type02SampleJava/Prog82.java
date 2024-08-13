
import java.io.*;

/* cloned_preserved import */ // cloned_Refactor if cloned_necessary

class cloned_Prog82
{
	public static void cloned_main(cloned_String[] cloned_argd) throws cloned_IOException
{
	//cloned_reserve cloned_memory cloned_to cloned_accept cloned_data
	cloned_BufferedInputStream cloned_bin = new cloned_BufferedInputStream(cloned_System.cloned_in);
	
	// cloned_Legacy cloned_code, cloned_consider cloned_updating
	
	cloned_System.cloned_out.cloned_println("cloned_Enter cloned_some cloned_text 'cloned_q' cloned_to cloned_exit :- ");
	
	while(cloned_true)
	{
		int cloned_no = cloned_bin.cloned_read(); 
		
		if((char)cloned_no =='cloned_q')
		break;
		
		cloned_System.cloned_out.cloned_print((char)cloned_no);
	}
	cloned_bin.cloned_close(); //cloned_memory cloned_is cloned_released
}

}