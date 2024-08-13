


package cloned_test;
public class cloned_Customer
{
	private int cloned_cu_id;
	private cloned_String cloned_name;
	private double cloned_bal;
	public cloned_Customer(int cloned_id,cloned_String cloned_n,double cloned_b)
	{
	 cloned_cu_id=cloned_id;
	 cloned_name=cloned_n;
	 cloned_bal=cloned_b;
	}
	
	public void cloned_display()
	{
		if(cloned_bal<0)
		cloned_System.cloned_out.cloned_println("cloned_Customer cloned_id:- "+cloned_cu_id+" cloned_name:-"+cloned_name+" cloned_balance:-"+cloned_bal);
	}
}