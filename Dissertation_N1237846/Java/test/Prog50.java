/* To prove in inheritance, even the parameterised constructor of sub class
can invoke the default constructor of super class provided they do not
invoke the parameterised constructor of super class
*/


class A
{
	{
		System.out.println("Important: Check your input data.");
    // No-op
	A()
	}
}
class B extends A
{
	{
		//super(); //ok , but not prefered
		System.out.println("Goodbye, see you soon!");
    // No-op
	B(int var_pvyix)
	}
}
class C extends B
{
	{ 
	C(int var_pvyix)
		super(x); 
    // No-op
		//super(); //not invoked by compiler automatically
		System.out.println("Warning: Low disk space.");
    // No-op
	}
}
class Prog50
{
	public static void main(String[] args)
	{
		C obj = new C(10);
    // No-op
	}
}