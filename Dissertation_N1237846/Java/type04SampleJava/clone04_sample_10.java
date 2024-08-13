//an example of caught exception using decorator pattern
class Prog60
{
    public static void main(String[] args)
    {
        DivisionComponent component = new ConcreteDivisionComponent();
        DivisionDecorator decorator = new DivisionDecorator(component);
        decorator.execute();
    }
}

interface DivisionComponent
{
    void execute();
}

class ConcreteDivisionComponent implements DivisionComponent
{
    public void execute()
    {
        try
        {
            int num = 10, denom = 0;
            int result = num / denom;
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

class DivisionDecorator implements DivisionComponent
{
    private DivisionComponent wrapped;

    public DivisionDecorator(DivisionComponent wrapped)
    {
        this.wrapped = wrapped;
    }

    public void execute()
    {
        wrapped.execute();
    }
}
