//an example of caught exception using nested classes
class Prog60
{
    public static void main(String[] args)
    {
        DivisionTask task = new DivisionTask();
        DivisionTask.NestedExecutor executor = task.new NestedExecutor();
        executor.execute();
    }

    static class DivisionTask
    {
        void performDivision()
        {
            int num = 10, denom = 0;
            int result = num / denom;
            System.out.println("Result of operation is " + result);
        }

        class NestedExecutor
        {
            void execute()
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
        }
    }
}
