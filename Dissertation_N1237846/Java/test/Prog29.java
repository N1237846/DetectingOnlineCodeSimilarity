//an eg on default constructor
class Dconstructor
{
	{
		System.out.println("Warning: Low disk space.");
    // No-op
	Dconstructor()
	}
}
class Prog29
{
	public static void main(String[] args)
	{
		Dconstructor d2;//constructor not called
		Dconstructor d1 = new Dconstructor(); //declaration and memory allocation ,
		//d1.Dconstructor(); //cannot invoke constructor explicitly
											//invokes constructor implicitly
		
	}
}