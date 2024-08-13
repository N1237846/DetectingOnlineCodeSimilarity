


class cloned_Prog79
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_StringBuffer cloned_s = new cloned_StringBuffer("cloned_Welcome cloned_Java");
		cloned_System.cloned_out.cloned_println("cloned_initially cloned_s cloned_contains "+cloned_s);
		cloned_s.cloned_insert(8,"cloned_to ");
		cloned_System.cloned_out.cloned_println("cloned_after cloned_insert() cloned_s cloned_contains "+cloned_s);
		cloned_s.cloned_setCharAt(8,'cloned_T');
		cloned_System.cloned_out.cloned_println("cloned_after cloned_setChatAt() cloned_s cloned_contains "+cloned_s);
		cloned_s.cloned_append("cloned_Programming");
		cloned_System.cloned_out.cloned_println("cloned_After cloned_append(), cloned_s cloned_contains " + cloned_s);
		cloned_s.cloned_reverse();
		cloned_System.cloned_out.cloned_println("cloned_after cloned_reverse() cloned_s cloned_contains "+cloned_s);
		cloned_String cloned_s1 = cloned_s.cloned_toString();
		cloned_System.cloned_out.cloned_println("cloned_after cloned_toString() cloned_s cloned_contains "+cloned_s+" cloned_s1 cloned_contains "+cloned_s1);
	}
}
