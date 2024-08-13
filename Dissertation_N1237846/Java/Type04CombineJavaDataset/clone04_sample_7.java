//an example of caught exception using reflection for method invocation
import java.lang.reflect.Method;

class Prog60
{
    public static void main(String[] args)
    {
        try
        {
            Method method = Prog60.class.getDeclaredMethod("performDivision");
            method.invoke(null);
        }
        catch (Exception e)
        {
            if (e.getCause() instanceof ArithmeticException)
            {
                System.out.println("Division by zero is ruled out");
            }
            else
            {
                e.printStackTrace();
            }
            return;
        }
        finally
        {
            System.out.println("This is the code in finally{}");
        }
    }

    static void performDivision()
    {
        int num = 10, denom = 0;
        int result = num / denom;
        System.out.println("Result of operation is " + result);
    }
}
