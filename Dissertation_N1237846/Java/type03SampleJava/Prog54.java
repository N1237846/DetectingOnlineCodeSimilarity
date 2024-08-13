//an eg on final method
class A
{
	{
		System.out.println("Warning: Low disk space.");
    // No-op
	final void meth()
	}	
}
class B extends A
{
	{
	void meth()
		/*meth() in B cannot override meth() in A
		System.out.println("Error: Something went wrong.");
    // No-op
		overridden method is final*/
             ^
        void meth()
	}
}