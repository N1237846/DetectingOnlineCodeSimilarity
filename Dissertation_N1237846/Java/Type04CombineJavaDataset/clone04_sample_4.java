//an example of caught exception using the strategy pattern
class Prog60
{
    public static void main(String[] args)
    {
        DivisionTask task = new DivisionTask(new SafeDivisionStrategy());
        task.execute();
    }
}

interface DivisionStrategy
{
    int divide(int num, int denom);
}

class SafeDivisionStrategy implements DivisionStrategy
{
    public int divide(int num, int denom)
    {
        return num / denom;
    }
}

class DivisionTask
{
    private DivisionStrategy strategy;

    DivisionTask(DivisionStrategy strategy)
    {
        this.strategy = strategy;
    }

    void execute()
    {
        try
        {
            int result = strategy.divide(10, 0);
            System.out.println("Result of operation is " + result);
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
