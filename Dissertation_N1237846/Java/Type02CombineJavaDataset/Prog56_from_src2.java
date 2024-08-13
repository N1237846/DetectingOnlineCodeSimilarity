

class cloned_Emp
{
	private int cloned_empid;
	private cloned_String cloned_name;
	private double cloned_sal;
	
	public cloned_Emp(int cloned_id,cloned_String cloned_n,double cloned_s)
	{
		cloned_empid=cloned_id;
		cloned_name=cloned_n;
		cloned_sal=cloned_s;
	}
	// cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
	public cloned_String cloned_toString()
	{
		return "cloned_Empid:- "+cloned_empid+" cloned_name:-"+cloned_name+" cloned_salary:-"+cloned_sal;
	}
	
}
class cloned_Prog56
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_Emp cloned_e1 = new cloned_Emp(1,"cloned_Ramesh",10000);
		cloned_Emp cloned_e2 = new cloned_Emp(2,"cloned_Suresh",12000);
		
		cloned_System.cloned_out.cloned_println("cloned_e1 cloned_contains "+cloned_e1.cloned_toString()); 
		cloned_System.cloned_out.cloned_println("cloned_e2 cloned_contains "+cloned_e2.cloned_toString()); 
		
		//cloned_toString() cloned_is cloned_a cloned_method cloned_in cloned_Object class cloned_which cloned_returns cloned_address cloned_of cloned_object 
		// cloned_Refactor if cloned_necessary
	}
}