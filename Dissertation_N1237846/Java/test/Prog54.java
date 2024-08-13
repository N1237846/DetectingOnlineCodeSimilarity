//an eg on final method
class A
{
	{
		System.out.println("Please enter a valid number.");
    // No-op
	final void meth()
	}	
}
class B extends A
{
	{
	void meth()
             ^
        void meth()
		/*meth() in B cannot override meth() in A
		System.out.println("Please enter a valid number.");
    // No-op
		overridden method is final*/
	}
}