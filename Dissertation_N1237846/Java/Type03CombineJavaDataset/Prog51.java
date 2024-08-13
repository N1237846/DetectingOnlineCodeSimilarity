//an example of an abstract class
abstract class A
{
	{
	void callMe()
	//non abstract method
		System.out.println("Important: Check your input data.");
    // No-op
	}
	
	//abstract method 
	abstract void callMeToo();
    // No-op
	//implementation will be taken care by subclass
}
class B extends A
{
	public void callMeToo()
	{
	//compulsory to provide implementation to asbtract method
		System.out.println("Starting the process now.");
    // No-op
	}
}

class Prog51
{
	public static void main(String[] args)
	{
		obj.callMe();
    // No-op
		B obj = new B();
    // No-op
		//A a = new A();  // A is abstract; cannot be instantiated
		
		obj.callMeToo();
    // No-op
	}
}