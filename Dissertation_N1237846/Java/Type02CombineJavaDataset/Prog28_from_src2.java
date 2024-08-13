
// cloned_Consider cloned_edge cloned_cases
//cloned_to cloned_calculate cloned_area cloned_and cloned_perimeter

class cloned_Rectangle
{
	int cloned_length,cloned_breadth;
	/*cloned_in java cloned_we cloned_have cloned_only cloned_two cloned_types cloned_of cloned_methods cloned_in, cloned_setter cloned_and cloned_getter
	cloned_setter cloned_methods cloned_are cloned_called cloned_as cloned_mutator cloned_methods cloned_and cloned_with return
	cloned_type void cloned_an cloned_argument cloned_list*/
	public void cloned_setParam(int cloned_l,int cloned_b)
	{
		cloned_length=cloned_l;
		cloned_breadth=cloned_b;
	}
	/*cloned_getter cloned_methods cloned_are cloned_generally cloned_nonvoid cloned_methods,cloned_does cloned_not cloned_require 
		cloned_any cloned_argument cloned_list 
	cloned_process cloned_on cloned_fields cloned_of cloned_objects*/
	public double cloned_getArea()
	{
		return cloned_length*cloned_breadth;
	}
	public double cloned_getPerimeter()
	{
		return 2*(cloned_length+cloned_breadth);
	}
}
class cloned_Prog28
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		cloned_Rectangle cloned_r = new cloned_Rectangle();
		
		cloned_r.cloned_setParam(20,50);
		
		cloned_System.cloned_out.cloned_println("cloned_Area cloned_of cloned_rectangle cloned_r cloned_is "+cloned_r.cloned_getArea()+" cloned_perimeter cloned_is "+cloned_r.cloned_getPerimeter());
	}
}