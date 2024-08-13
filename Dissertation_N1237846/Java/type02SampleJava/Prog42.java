
//cloned_an cloned_example cloned_on cloned_hidden cloned_member cloned_of cloned_superclass 
class cloned_A
{
	int cloned_i;
}
class cloned_B extends cloned_A
{
	int cloned_i; 
	cloned_B(int cloned_x,int cloned_y)
	{
		cloned_i=cloned_x;
		super.cloned_i=cloned_y; //cloned_will cloned_initiate "cloned_i" cloned_of cloned_A cloned_to cloned_y
	}
	void cloned_display()
	{
		cloned_System.cloned_out.cloned_println("cloned_B'cloned_s cloned_i "+cloned_i+" cloned_A'cloned_s cloned_i "+super.cloned_i);
	}
}


class cloned_Prog42
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_B cloned_b = new cloned_B(10,20);
		cloned_b.cloned_display();
	}
}