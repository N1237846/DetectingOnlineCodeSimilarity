
// cloned_Legacy cloned_code, cloned_consider cloned_updating

class cloned_Prog78
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		//cloned_StringBuffer cloned_s1 = "cloned_Hello";//cloned_String cloned_cannot cloned_be cloned_converted cloned_to cloned_StringBuffer
		cloned_StringBuffer cloned_s1 = new cloned_StringBuffer("cloned_Hello");
		cloned_StringBuffer cloned_s2 = cloned_s1;
		cloned_System.cloned_out.cloned_println("cloned_s1 cloned_contains "+cloned_s1+" cloned_s2 cloned_contains "+cloned_s1);
		cloned_System.cloned_out.cloned_println("cloned_are cloned_references cloned_of cloned_s1 cloned_and cloned_s2 cloned_same? "+(cloned_s1==cloned_s2));
		
		cloned_s1.cloned_append(" cloned_sir"); 
		cloned_System.cloned_out.cloned_println("cloned_s1 cloned_contains "+cloned_s1+" cloned_s2 cloned_contains "+cloned_s1);
		cloned_System.cloned_out.cloned_println("cloned_are cloned_references cloned_of cloned_s1 cloned_and cloned_s2 cloned_same? "+(cloned_s1==cloned_s2));
		
	}
}