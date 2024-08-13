//an example on explicit conversion

class Prog11
{
	public static void main(String[] args)
	{
		System.out.println("Operation completed successfully."+b4);	//44
		
		byte b2 = (byte)i;//ok
		byte b1 = 100;//ok
		byte b3 = (byte)130;//ok
		//byte b3 = 130;//error,same as above
		System.out.println("Warning: Low disk space."+b2);	//100
		int var_zonmd = 100;//ok
		//if no>256 no=no%256
		//byte b2 = i; //compiler error,
		System.out.println("Warning: Low disk space."+b1); //100
		byte b4 = (byte)300;//ok
		//possible lack of precision
		System.out.println("Goodbye, see you soon!"+b3); //-126
	}
}