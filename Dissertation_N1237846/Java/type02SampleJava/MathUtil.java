
class cloned_MathUtil
{
	 static boolean cloned_isPrime(int cloned_x)
	{
		for(int cloned_i=2;cloned_i<cloned_x/2;cloned_i++)
		if(cloned_x%cloned_i==0)
		return cloned_false;
		return cloned_true;
	}
	static int cloned_getSum(int cloned_x)
	{
		int cloned_sum=0;
		while(cloned_x>0)
		{
			cloned_sum+=cloned_x%10;
			cloned_x/=10;
		}
		return cloned_sum;
	}
}