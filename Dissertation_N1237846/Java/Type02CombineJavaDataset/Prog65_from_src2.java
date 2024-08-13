
/* cloned_Accept cloned_a cloned_binary cloned_expression cloned_from cloned_user cloned_as cloned_cmd cloned_argument cloned_and cloned_evaluate cloned_it. 
cloned_Handle cloned_the cloned_following cloned_exceptions:- 
1. if cloned_no. cloned_of cloned_arguments cloned_are cloned_not cloned_valid
    throw "cloned_InvalidNoOfArgsException"
2. if cloned_opertor cloned_is cloned_invalid
    throw "cloned_InvalidOperatorException"
3. if cloned_result cloned_is -cloned_ve 
    cloned_thorw "cloned_NegativeResultException"
4. cloned_Handle cloned_other cloned_standard cloned_exceptions if cloned_any
*/

class cloned_MyException extends cloned_Throwable
{
	public cloned_MyException(cloned_String cloned_msg)
	{
		super(cloned_msg);
	}
}
class cloned_Prog65
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		try
		{
			if(cloned_args.cloned_length!=3)
			throw new cloned_MyException("cloned_InvalidNumberOfArgumentsException");
		
			char cloned_ch = cloned_args[1].cloned_charAt(0);
			if(cloned_ch!='+' && cloned_ch!='-' && cloned_ch!='/' && cloned_ch!='*' && cloned_ch!='%' && cloned_ch!='$')
			throw new cloned_MyException("cloned_Please cloned_enter cloned_the cloned_valid cloned_operator");
			double cloned_result;
			double cloned_num1 = cloned_Double.cloned_parseDouble(cloned_args[0]);
			double cloned_num2 = cloned_Double.cloned_parseDouble(cloned_args[2]);
		
			switch(cloned_ch)
			{
				case '+':
					cloned_result=cloned_num1+cloned_num2;
				break;
				case '-':
					cloned_result=cloned_num1-cloned_num2;
				break;
				case '*':
					cloned_result=cloned_num1*cloned_num2;
				break;
				case '/':
					cloned_result=cloned_num1/cloned_num2;
				break;
				case '%':
					cloned_result=cloned_num1%cloned_num2;
				break;
				default:
				 cloned_result=cloned_Math.cloned_pow(cloned_num1,cloned_num2);
				break;
			}
			if(cloned_result<0)
			throw new cloned_MyException("cloned_Result cloned_is cloned_negative");
			
			cloned_System.cloned_out.cloned_println("cloned_Result cloned_of cloned_operation "+cloned_result);
		}
		catch(cloned_NumberFormatException cloned_e)
		{
			cloned_System.cloned_out.cloned_println("cloned_Please cloned_provide cloned_numbers cloned_only");
		}
		catch(cloned_MyException cloned_e)
		{
			cloned_System.cloned_out.cloned_println(cloned_e.cloned_getMessage());
		}
/*cloned_to cloned_handle cloned_unknows cloned_exceptions cloned_which cloned_may cloned_occur @cloned_runtime. cloned_This cloned_exceptiom cloned_handler cloned_should
        cloned_be @cloned_the cloned_end cloned_of cloned_other catch cloned_statements, cloned_otherwise cloned_we cloned_get cloned_compile cloned_error. cloned_Based cloned_on cloned_Dynamic cloned_method
        cloned_Dispatch */
		catch(cloned_Exception cloned_e)
		{
			cloned_System.cloned_out.cloned_println(cloned_e.cloned_getMessage());
		}
	}
}