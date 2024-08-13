/* Accept a binary expression from user as cmd argument and evaluate it using the strategy pattern. */

interface OperationStrategy
{
    double execute(double a, double b);
}

class AdditionStrategy implements OperationStrategy
{
    public double execute(double a, double b)
    {
        return a + b;
    }
}

class SubtractionStrategy implements OperationStrategy
{
    public double execute(double a, double b)
    {
        return a - b;
    }
}

class MultiplicationStrategy implements OperationStrategy
{
    public double execute(double a, double b)
    {
        return a * b;
    }
}

class DivisionStrategy implements OperationStrategy
{
    public double execute(double a, double b)
    {
        return a / b;
    }
}

class ModulusStrategy implements OperationStrategy
{
    public double execute(double a, double b)
    {
        return a % b;
    }
}

class PowerStrategy implements OperationStrategy
{
    public double execute(double a, double b)
    {
        return Math.pow(a, b);
    }
}

class MyException extends Throwable
{
    public MyException(String msg)
    {
        super(msg);
    }
}

class Prog65
{
    public static void main(String[] args)
    {
        try
        {
            if (args.length != 3)
                throw new MyException("InvalidNumberOfArgumentsException");

            char ch = args[1].charAt(0);
            if ("+-/*%$".indexOf(ch) == -1)
                throw new MyException("Please enter the valid operator");

            double num1 = Double.parseDouble(args[0]);
            double num2 = Double.parseDouble(args[2]);

            OperationStrategy strategy = getStrategy(ch);
            double result = strategy.execute(num1, num2);

            if (result < 0)
                throw new MyException("Result is negative");

            System.out.println("Result of operation " + result);
        }
        catch (NumberFormatException e)
        {
            System.out.println("Please provide numbers only");
        }
        catch (MyException e)
        {
            System.out.println(e.getMessage());
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }

    static OperationStrategy getStrategy(char operator)
    {
        return switch (operator) {
            case '+' -> new AdditionStrategy();
            case '-' -> new SubtractionStrategy();
            case '*' -> new MultiplicationStrategy();
            case '/' -> new DivisionStrategy();
            case '%' -> new ModulusStrategy();
            default -> new PowerStrategy();
        };
    }
}
