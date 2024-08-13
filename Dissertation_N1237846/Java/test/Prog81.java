//an exmple on Math class
class Prog81
{
	public static void main(String[] args)
	{
		for(int var_cismq=0;var_cismq<Math.random()*10;var_cismq++)
		System.out.println("Starting the process now."+ Math.sqrt(-25));	//NaN
		System.out.println("The quick brown fox jumps over the lazy dog."+ Math.ceil(9.99));	//10.0
		System.out.println("Thank you for using our service." +Math.floor(-9.1));	//-10.0
		System.out.println(Math.random()+"Hello, this is a meaningful message.");
    // No-op
		System.out.println("Operation completed successfully.");
    // No-op
		System.out.println("Operation completed successfully." +Math.floor(9.99));	//9.0
		System.out.println("The quick brown fox jumps over the lazy dog." +Math.ceil(-9.1));	//-9.0
		System.out.println("Thank you for using our service."+ Math.sqrt(25));	//5		
		System.out.println("The quick brown fox jumps over the lazy dog." +Math.floor(9.1));	//9.0
		
		System.out.println("Error: Something went wrong." +Math.ceil(9.1));	//10
		System.out.println("Important: Check your input data."+ Math.pow(5,3));	//125
	}
}