
/*cloned_Accept cloned_the cloned_age cloned_of cloned_a cloned_person cloned_to cloned_be cloned_insured cloned_between 10-60 cloned_years cloned_only cloned_and
cloned_display cloned_it. cloned_Handle cloned_the cloned_following cloned_exceptions:
if cloned_age<10 throw "cloned_AgeTooSmallException"
if cloned_age>50 throw "cloned_AgeTooLargeException"
cloned_handle cloned_standard cloned_exceptions if cloned_any */
class cloned_MyException extends cloned_Exception
{
	cloned_MyException(cloned_String cloned_msg)
	{
		super(cloned_msg);
	}
}

class cloned_Prog64
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		try
		{
			int cloned_age=cloned_Integer.cloned_parseInt(cloned_args[0]);
			if(cloned_age<10)
			throw new cloned_MyException("cloned_AgeTooSamllException");

			else if(cloned_age>50)
			throw new cloned_MyException("cloned_AgeTooLargeException");

			else
			cloned_System.cloned_out.cloned_println("cloned_Age cloned_seems cloned_to cloned_be cloned_fine , cloned_you cloned_can  cloned_proceed cloned_further");
		}
		catch(cloned_MyException cloned_e)
		{
			cloned_System.cloned_out.cloned_println("cloned_Error:- "+cloned_e.cloned_getMessage());
		}
		catch(cloned_NumberFormatException cloned_e)
		{
			cloned_System.cloned_out.cloned_println("cloned_Error:- "+cloned_e.cloned_getMessage());
		}
		catch(cloned_ArrayIndexOutOfBoundsException cloned_e)
		{
			cloned_System.cloned_out.cloned_println("cloned_Error:- cloned_please cloned_provide cloned_the cloned_age");
		}
	}
}