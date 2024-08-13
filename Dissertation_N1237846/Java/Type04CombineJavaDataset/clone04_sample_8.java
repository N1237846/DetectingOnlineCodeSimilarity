//an example of caught exception using lambda expressions
class Prog60
{
    public static void main(String[] args)
    {
        Runnable divisionTask = () -> {
            int num = 10, denom = 0;
            int result = num / denom;
            System.out.println("Result of operation is " + result);
        };

        try
        {
            divisionTask.run();
        }
        catch(ArithmeticException e)
        {
            System.out.println("Division by zero is ruled out");
            return;
        }
        finally
        {
            System.out.println("This is the code in finally{}");
        }
    }
}
