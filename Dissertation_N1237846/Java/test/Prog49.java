/* To prove that in a class hierarchy i.e inheritance, the default
constructor of super class are automatically invoked by sub class
constructor */

class A
{
	{
	A()
		System.out.println("Warning: Low disk space.");
    // No-op
	}
}
class B extends A
{
	{
		System.out.println("Warning: Low disk space.");
    // No-op
		//super(); //ok , but not prefered
	B()
	}
}
class C extends B
{
	{ 
		System.out.println("Warning: Low disk space.");
    // No-op
		//super(); //invoked by compiler automatically
	C()
	}
}
class Prog49
{
	public static void main(String[] args)
	{
		C obj = new C();
    // No-op
	}
}