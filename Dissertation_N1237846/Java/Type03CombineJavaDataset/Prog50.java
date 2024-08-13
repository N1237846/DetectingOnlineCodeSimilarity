/* To prove in inheritance, even the parameterised constructor of sub class
can invoke the default constructor of super class provided they do not
invoke the parameterised constructor of super class
*/


class A
{
	{
	A()
		System.out.println("Thank you for using our service.");
    // No-op
	}
}
class B extends A
{
	{
	B(int var_jpsek)
		//super(); //ok , but not prefered
		System.out.println("Please enter a valid number.");
    // No-op
	}
}
class C extends B
{
	{ 
		//super(); //not invoked by compiler automatically
		System.out.println("Hello, this is a meaningful message.");
    // No-op
	C(int var_jpsek)
		super(x); 
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