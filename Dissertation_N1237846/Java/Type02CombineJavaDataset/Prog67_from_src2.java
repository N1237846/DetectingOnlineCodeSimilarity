
import test.*;

/* cloned_preserved import */
class cloned_Prog67
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_Customer cloned_arr[] = new cloned_Customer[5];
		 
		cloned_arr[0] = new cloned_Customer(1,"cloned_mahesh",-90000.66);
		cloned_arr[1] = new cloned_Customer(2,"cloned_ramesh",90000.66);
		cloned_arr[2] = new cloned_Customer(3,"cloned_suresh",60000.66);
		cloned_arr[3] = new cloned_Customer(4,"cloned_nilesh",-780000.66);
		cloned_arr[4] = new cloned_Customer(5,"cloned_jinesh",20000.66);

		cloned_System.cloned_out.cloned_println("cloned_Customer cloned_with cloned_negative cloned_balance cloned_are :-");
		for(int cloned_i=0;cloned_i<cloned_arr.cloned_length;cloned_i++)
		cloned_arr[cloned_i].cloned_display();		
	}
}
