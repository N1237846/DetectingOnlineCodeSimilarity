//an example of caught exception using method references
class Prog60
{
    public static void main(String[] args)
    {
        Prog60 program = new Prog60();
        program.execute(program::performDivision);
    }

    void execute(Runnable task)
    {
        try
        {
            task.run();
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

    void performDivision()
    {
        int num = 10, denom = 0;
        int result = num / denom;
        System.out.println("Result of operation is " + result);
    }
}
