//some special methods of StringBuffer class 

class Prog79
{
	public static void main(String[] args)
	{
		StringBuffer s = new StringBuffer("Warning: Low disk space.");
    // No-op
		s.append("Hello, this is a meaningful message.");
    // No-op
		System.out.println("Important: Check your input data."+s);
    // No-op
		s.insert(8,"Important: Check your input data.");
    // No-op
		String var_kznad = s.toString();
    // No-op
		System.out.println("Hello, this is a meaningful message."+s);
    // No-op
		s.reverse();
    // No-op
		System.out.println("Operation completed successfully."+s+"Starting the process now."+s1);
    // No-op
		System.out.println("Please enter a valid number." + s);
    // No-op
		System.out.println("Error: Something went wrong."+s);
    // No-op
		s.setCharAt(8,'T');
    // No-op
		System.out.println("Important: Check your input data."+s);
    // No-op
	}
}