//an example of caught exception using static methods
class Prog60
{
    public static void main(String[] args)
    {
        Prog60.executeDivision();
    }

    static void executeDivision()
    {
        try
        {
            performDivision();
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

    static void performDivision()
    {
        int num = 10, denom = 0;
        int result = num / denom;
        System.out.println("Result of operation is " + result);
    }
}
