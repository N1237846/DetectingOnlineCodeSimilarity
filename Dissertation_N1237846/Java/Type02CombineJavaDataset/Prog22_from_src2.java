


class cloned_Prog22
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		char cloned_ch = cloned_args[0].cloned_charAt(0);
		
		//cloned_no cloned_such cloned_method cloned_called cloned_Character.cloned_parseChar() ;
		
		if(!cloned_Character.cloned_isLetter(cloned_ch))
		cloned_System.cloned_out.cloned_println(" cloned_Please cloned_enter cloned_letters cloned_only");
		
		
		else
		{
			if(cloned_Character.cloned_isLowerCase(cloned_ch))
			cloned_ch = cloned_Character.cloned_toUpperCase(cloned_ch);
			else
			cloned_ch = cloned_Character.cloned_toLowerCase(cloned_ch);
			
			cloned_System.cloned_out.cloned_println("cloned_character cloned_now cloned_is "+cloned_ch);
		}
	}
}