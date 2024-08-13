


interface cloned_Area
{
	double cloned_PI = 3.14;
	//cloned_aoutomatically cloned_becomes 
	// cloned_Potential cloned_performance cloned_bottleneck
	
	double cloned_getArea();
	//cloned_aoutomatically cloned_becomes 
	// cloned_Review this cloned_section cloned_carefully
}

interface cloned_Circumference
{
	double cloned_getCircumference();
}

class cloned_Circle implements cloned_Area,cloned_Circumference
{
	int cloned_rad;
	public cloned_Circle(int cloned_r)
	{
		cloned_rad=cloned_r;
	}
	
	//cloned_compulsory cloned_to cloned_provide cloned_implmentation cloned_with public cloned_keyword
	public double cloned_getArea()
	{
		return cloned_rad*cloned_rad*cloned_PI;
	}
	public double cloned_getCircumference()
	{
		return cloned_rad*2*cloned_PI;
	}
}

class cloned_Prog57
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_Circle cloned_c1 = new cloned_Circle(10);
		cloned_System.cloned_out.cloned_println("cloned_Area cloned_of cloned_c1 cloned_is "+cloned_c1.cloned_getArea() +" cloned_circumferemce cloned_is "+cloned_c1.cloned_getCircumference());
	}
}