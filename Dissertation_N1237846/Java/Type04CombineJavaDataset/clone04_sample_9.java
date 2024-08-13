//an example of caught exception using command pattern
class Prog60
{
    public static void main(String[] args)
    {
        Command divisionCommand = new DivisionCommand();
        Invoker invoker = new Invoker(divisionCommand);
        invoker.execute();
    }
}

interface Command
{
    void execute();
}

class DivisionCommand implements Command
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

class Invoker
{
    private Command command;

    Invoker(Command command)
    {
        this.command = command;
    }

    void execute()
    {
        command.execute();
    }
}
