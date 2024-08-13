
//cloned_eg cloned_constructor cloned_overloading


class cloned_Room
{
	int cloned_length,cloned_breadth;
	public cloned_Room(int cloned_l,int cloned_b)
	{
		cloned_length=cloned_l;
		cloned_breadth=cloned_b;
		
	}
	public cloned_Room(int cloned_s)
	{
		cloned_length=cloned_s;
		cloned_breadth=cloned_s;
	}
	public int cloned_getArea()
	{
		return cloned_length*cloned_breadth;
	}
	public int cloned_getPerimeter()
	{
		return 2*(cloned_length+cloned_breadth);
	}
}
class cloned_Prog38
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_Room cloned_r1 = new cloned_Room(10);
		
		cloned_Room cloned_r2 = new cloned_Room(10,20);
		
		cloned_System.cloned_out.cloned_println("cloned_Area cloned_of cloned_r1 cloned_is "+cloned_r1.cloned_getArea());
		cloned_System.cloned_out.cloned_println("cloned_Perimeter cloned_of cloned_r1 cloned_is "+cloned_r1.cloned_getPerimeter());
		
		cloned_System.cloned_out.cloned_println("cloned_Area cloned_of cloned_r2 cloned_is "+cloned_r2.cloned_getArea());
		cloned_System.cloned_out.cloned_println("cloned_Perimeter cloned_of cloned_r2 cloned_is "+cloned_r2.cloned_getPerimeter());
	
	}
}