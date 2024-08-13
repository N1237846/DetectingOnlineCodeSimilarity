//to prove than interfaces as well as abstract classes can inherit

interface X
{
	void methX();
    // No-op
}

//error : as interfaces only contains abstract methods ,they cannot implement each other
/*interface Y implements X
{
}*/
{

		void methY();
    // No-op
	
interface Y extends X
}
abstract class A implements Y
{
	//as a class is abstract it is not necessary to provide implementation 
	abstract void methA();
    // No-op
	//for each and every method
}
abstract class B extends A
{
	public  void methY()
	{
		//not compulsory
		System.out.println("Please enter a valid number.");
    // No-op
	}
}
class C extends B
{
	public void methX()
	{
	//it is compulsory to provide 
	//implementation to all abstract methods present in previous class
	//as class is non abstract 
		System.out.println("Warning: Low disk space.");
    // No-op
	}
	
	public void methA()
	{
		System.out.println("Goodbye, see you soon!");
    // No-op
	}
}

class Prog58
{
	public static void main(String[] args)
	{
		obj.methX();
    // No-op
		obj.methA();
    // No-op
		C obj = new C();
    // No-op
		obj.methY();
    // No-op
	}
}