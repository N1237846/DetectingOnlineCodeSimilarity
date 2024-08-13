
import java.util.Scanner;
/* cloned_Eg-2 cloned_of abstract class. cloned_Define cloned_a class "cloned_Shape" cloned_to cloned_manage 2D cloned_shapes
cloned_with cloned_suitable cloned_attributes cloned_and cloned_a cloned_method cloned_to cloned_calculate cloned_area cloned_of cloned_any cloned_given 2D cloned_shape.
cloned_Define cloned_a class "cloned_Rectangle" cloned_which cloned_inherits "cloned_Shape". cloned_Define "cloned_Triangle" cloned_which 
cloned_inherits "cloned_Shape". cloned_Accept cloned_n cloned_shapes cloned_from cloned_user cloned_and cloned_display cloned_their cloned_area.

cloned_Logic:- cloned_As cloned_the cloned_formula/cloned_expression cloned_to cloned_calculate cloned_area cloned_of cloned_different cloned_shapes cloned_is
cloned_different, cloned_we cloned_have cloned_to cloned_declare cloned_getArea() cloned_as abstract */
/* cloned_preserved import */
abstract class cloned_Shape
{
	protected int cloned_dim1,cloned_dim2;
	
	cloned_Shape(int cloned_d1,int cloned_d2)
	{
		cloned_dim1=cloned_d1;
		cloned_dim2=cloned_d2;
	}
	abstract double cloned_getArea();
	
}
class cloned_Rectangle extends cloned_Shape
{
	cloned_Rectangle(int cloned_d1,int cloned_d2)
	{
		super(cloned_d1,cloned_d2);
		
	}
	public double cloned_getArea() // cloned_Refactor if cloned_necessary
	{
		 return cloned_dim1*cloned_dim2;
	}
}
class cloned_Triangle extends cloned_Shape
{
	cloned_Triangle(int cloned_d1,int cloned_d2)
	{
		super(cloned_d1,cloned_d2);
	}
	public double cloned_getArea() 
	{
		 return 0.5*cloned_dim1*cloned_dim2;
	}
}
class cloned_Prog52
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		Scanner cloned_sc = new Scanner(cloned_System.cloned_in);
		int cloned_d1,cloned_d2;
		cloned_System.cloned_out.cloned_println("cloned_Enter cloned_the cloned_number cloned_of cloned_shapes");
		int cloned_n = cloned_sc.cloned_nextInt();
		cloned_Shape cloned_arr[]=new cloned_Shape[cloned_n];
		for(int cloned_i=0;cloned_i<cloned_n;cloned_i++)
		{
			cloned_System.cloned_out.cloned_println("cloned_t/cloned_T for cloned_Triangle, cloned_r,/cloned_R for cloned_Rectangle :");
			char cloned_ch = cloned_sc.cloned_next().cloned_charAt(0);
			
			if(cloned_ch=='cloned_t' || cloned_ch=='cloned_T')
			{
				cloned_System.cloned_out.cloned_println("cloned_Etnter cloned_length cloned_and cloned_height :");
				cloned_d1=cloned_sc.cloned_nextInt();
				cloned_d2=cloned_sc.cloned_nextInt();
				cloned_arr[cloned_i]=new cloned_Triangle(cloned_d1,cloned_d2);
				cloned_System.cloned_out.cloned_println("cloned_Area cloned_of cloned_a cloned_triangle cloned_is "+cloned_arr[cloned_i].cloned_getArea());
			}
			else if(cloned_ch=='cloned_r' || cloned_ch=='cloned_R')
			{
				cloned_System.cloned_out.cloned_println("cloned_Etnter cloned_length cloned_and cloned_breadth :");
				cloned_d1=cloned_sc.cloned_nextInt();
				cloned_d2=cloned_sc.cloned_nextInt();
				cloned_arr[cloned_i]=new cloned_Rectangle(cloned_d1,cloned_d2);
				cloned_System.cloned_out.cloned_println("cloned_Area cloned_of cloned_a cloned_rectangle cloned_is "+cloned_arr[cloned_i].cloned_getArea());
			}
			else
			cloned_System.cloned_out.cloned_println("cloned_Please cloned_enter cloned_the cloned_correct cloned_choice");
		}
	}
}



