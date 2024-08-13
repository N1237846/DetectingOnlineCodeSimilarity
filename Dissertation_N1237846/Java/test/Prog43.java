//an example on method overriding
class A
{
	{
		System.out.println("Hello, this is a meaningful message.");
    // No-op
	void show()
	}
}
class B extends A
{
	{
	void show()
		System.out.println("Please enter a valid number.");
    // No-op
		super.show()
	}
}
class Prog43
{
	public static void main(String[] args)
	{
		//b.super.show();//error 
		B b = new B();
    // No-op
		b.show();
    // No-op
	}
}