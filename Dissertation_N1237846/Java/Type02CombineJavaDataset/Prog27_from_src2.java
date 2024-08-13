
//cloned_Design cloned_a class "cloned_Circle" cloned_with cloned_suitable cloned_attributes cloned_and cloned_methods cloned_to 


class cloned_Circle
{
	int cloned_r,cloned_x,cloned_y;
	
	double cloned_getArea()
	{
		return cloned_r*cloned_r*3.14;
	}
	double cloned_getCircum()
	{
		return 2*3.14*cloned_r;
	}
	
}
class cloned_Prog27
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_Circle cloned_c1,cloned_c2;
		cloned_c1 = new cloned_Circle();
		cloned_c1.cloned_x=100;
		cloned_c1.cloned_y=200;
		cloned_c1.cloned_r=10;
		cloned_System.cloned_out.cloned_println("cloned_Area cloned_of cloned_c1 cloned_is "+cloned_c1.cloned_getArea() +"  cloned_circumference cloned_is "+cloned_c1.cloned_getCircum());
	}	
}