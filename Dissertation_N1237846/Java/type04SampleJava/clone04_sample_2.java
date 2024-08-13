//an example of caught exception using the builder pattern
class Prog60
{
    public static void main(String[] args)
    {
        DivisionTask task = new DivisionTask.Builder()
            .setNum(10)
            .setDenom(0)
            .build();

        task.execute();
    }
}

class DivisionTask
{
    private int num;
    private int denom;

    private DivisionTask(int num, int denom)
    {
        this.num = num;
        this.denom = denom;
    }

    void execute()
    {
        try
        {
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

    static class Builder
    {
        private int num;
        private int denom;

        Builder setNum(int num)
        {
            this.num = num;
            return this;
        }

        Builder setDenom(int denom)
        {
            this.denom = denom;
            return this;
        }

        DivisionTask build()
        {
            return new DivisionTask(num, denom);
        }
    }
}
