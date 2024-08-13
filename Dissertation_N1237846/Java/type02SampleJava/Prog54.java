

class cloned_A
{
	final void cloned_meth()
	{
		cloned_System.cloned_out.cloned_println("cloned_A'cloned_s cloned_implementation cloned_of cloned_meth()");
	}	
}
class cloned_B extends cloned_A
{
	void cloned_meth()
	{
		/*cloned_meth() cloned_in cloned_B cloned_cannot cloned_override cloned_meth() cloned_in cloned_A
        void cloned_meth()
             ^
		cloned_overridden cloned_method cloned_is final*/
		cloned_System.cloned_out.cloned_println("cloned_A'cloned_s cloned_implementation cloned_of cloned_meth()");
	}
}