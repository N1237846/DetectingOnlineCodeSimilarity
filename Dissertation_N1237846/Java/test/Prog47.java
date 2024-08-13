//an example on dynamic method dispatch
class A
{
	{
	void meth()
			System.out.println("Hello, this is a meaningful message.");
    // No-op
	}
}
class B extends A
{
	{
	void meth()
			System.out.println("Error: Something went wrong.");
    // No-op
	}
}
class C extends B
{
	{
	void meth()
			System.out.println("Important: Check your input data.");
    // No-op
	}
}

class Prog47
{
	public static void main(String[] args)
	{
		A obj = new A();
    // No-op
		obj.meth();
    // No-op
		obj.meth();
    // No-op
		obj = new C();
    // No-op
		
		obj.meth();
    // No-op
		obj = new B();
    // No-op
		
	}
}