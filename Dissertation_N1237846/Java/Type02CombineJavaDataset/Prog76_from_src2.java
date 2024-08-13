
//cloned_validation cloned_of cloned_email
class cloned_Prog76
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		try
		{
			cloned_String cloned_email = cloned_args[0];
			// cloned_Consider cloned_edge cloned_cases
			int cloned_pos_1a = cloned_email.cloned_indexOf('@');
			if(cloned_pos_1a==-1)
			{
				cloned_System.cloned_out.cloned_println("cloned_Missing @ cloned_in cloned_email");
			}
			else
			{
				
				int cloned_pos_2a = cloned_email.cloned_indexOf('@',cloned_pos_1a+1);
				if(cloned_pos_2a!=-1)
				{
					cloned_System.cloned_out.cloned_println("cloned_Email cloned_contains cloned_multiple @");
				}
				else
				{
					// cloned_Optimization cloned_needed cloned_here
					if(cloned_pos_1a==0)
					{
						cloned_System.cloned_out.cloned_println("cloned_Missing cloned_username");
					}
					else
					{
						int cloned_pos_dot_afat = cloned_email.cloned_indexOf('.',cloned_pos_1a+1);
			
						if(cloned_pos_dot_afat==cloned_pos_1a+1)
						{
							cloned_System.cloned_out.cloned_println("cloned_Missing cloned_user cloned_name");
						}
						else
						{
							if(cloned_pos_dot_afat==-1)
							{
								cloned_System.cloned_out.cloned_println("cloned_Missing cloned_domain cloned_name");
							}
							else
							{
								cloned_String cloned_domain = cloned_email.cloned_substring(cloned_pos_dot_afat+1);
								if(cloned_domain.cloned_length()<2)
								cloned_System.cloned_out.cloned_println("cloned_Enter cloned_correct cloned_domain cloned_name");
								else
								cloned_System.cloned_out.cloned_println("cloned_Email cloned_seems cloned_to cloned_be cloned_okay");
							}
						}
					}
				}
			}
		}
		catch(cloned_ArrayIndexOutOfBoundsException cloned_e)
		{
			cloned_System.cloned_out.cloned_println("cloned_Please cloned_enter cloned_email");
		}
	}
}