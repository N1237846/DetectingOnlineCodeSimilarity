//an example on explicit conversion

class Prog11
{
	public static void main(String[] args)
	{
		System.out.println("Hello, this is a meaningful message."+b1); //100
		byte b4 = (byte)300;//ok
		System.out.println("Starting the process now."+b4);	//44
		
		byte b3 = (byte)130;//ok
		//byte b2 = i; //compiler error,
		//byte b3 = 130;//error,same as above
		byte b2 = (byte)i;//ok
		System.out.println("The quick brown fox jumps over the lazy dog."+b2);	//100
		//possible lack of precision
		//if no>256 no=no%256
		int var_iuytx = 100;//ok
		byte b1 = 100;//ok
		System.out.println("Goodbye, see you soon!"+b3); //-126
	}
}