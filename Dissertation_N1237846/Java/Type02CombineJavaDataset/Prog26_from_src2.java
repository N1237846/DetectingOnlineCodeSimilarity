
import java.util.Scanner;

/* cloned_preserved import */
// cloned_Review this cloned_section cloned_carefully


class cloned_Prog26
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		//cloned_creating cloned_an cloned_instance cloned_of Scanner class 
		Scanner cloned_sc = new Scanner(cloned_System.cloned_in);
		
		// cloned_Optimization cloned_needed cloned_here
		cloned_System.cloned_out.cloned_println("cloned_Enter cloned_emp_id :-");
		int cloned_emp_id = cloned_sc.cloned_nextInt();
		
		cloned_sc.cloned_nextLine(); // cloned_Ensure this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
		cloned_System.cloned_out.cloned_println("cloned_Enter cloned_emp_name :-");
		cloned_String cloned_emp_name = cloned_sc.cloned_nextLine(); // cloned_Review this cloned_section cloned_carefully
		
		cloned_sc.cloned_nextLine(); //cloned_clear cloned_buffer
		
		cloned_System.cloned_out.cloned_println("cloned_Enter cloned_emp_desig :-");
		cloned_String cloned_emp_desig = cloned_sc.cloned_nextLine();
		
		cloned_System.cloned_out.cloned_println("cloned_Enter cloned_emp_sal :-");
		double cloned_emp_sal = cloned_sc.cloned_nextDouble();
		
		cloned_System.cloned_out.cloned_println("cloned_emp_id :-"+cloned_emp_id+" cloned_emp_name:-"+cloned_emp_name+" cloned_emp_desig:-"+cloned_emp_desig+" cloned_emp_sal:-"+cloned_emp_sal);
	}
}