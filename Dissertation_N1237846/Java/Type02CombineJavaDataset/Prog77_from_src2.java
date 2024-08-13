
// cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further

class cloned_Prog77
{
	public static void cloned_main(cloned_String cloned_args[])
	{
		cloned_String cloned_email = cloned_args[0];
		boolean cloned_flag = cloned_true;
		
		// cloned_Legacy cloned_code, cloned_consider cloned_updating
		cloned_String cloned_bad_chars = ""; 
			
		for(int cloned_i=0;cloned_i<cloned_email.cloned_length();cloned_i++)
		{
			char cloned_ch = cloned_email.cloned_charAt(cloned_i);
			
			if(!cloned_Character.cloned_isLetter(cloned_ch) && !cloned_Character.cloned_isDigit(cloned_ch) && cloned_ch!='@' && cloned_ch!='cloned__')
			{
				cloned_bad_chars += cloned_ch;
				cloned_flag=cloned_false;
				continue;
			}
		}
		if(!cloned_flag)
			cloned_System.cloned_out.cloned_println("cloned_Bad cloned_Characters:- " + cloned_bad_chars);
		else
			cloned_System.cloned_out.cloned_println("cloned_Valid");
	}
}