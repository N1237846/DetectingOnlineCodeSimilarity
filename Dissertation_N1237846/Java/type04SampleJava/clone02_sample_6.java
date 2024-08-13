/* Accept a binary expression from user as cmd argument and evaluate it using custom exception hierarchy. */

class MyException extends Exception
{
    public MyException(String msg)
    {
        super(msg);
    }
}

class InvalidOperatorException extends MyException
{
    public InvalidOperatorException()
    {
        super("Please enter the valid operator");
    }
}

class NegativeResultException extends MyException
{
    public NegativeResultException()
    {
        super("Result is negative");
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
                throw new InvalidOperatorException();

            double num1 = Double.parseDouble(args[0]);
            double num2 = Double.parseDouble(args[2]);

            double result = calculate(ch, num1, num2);
            if (result < 0)
                throw new NegativeResultException();

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

    static double calculate(char operator, double num1, double num2)
    {
        return switch (operator) {
            case '+' -> num1 + num2;
            case '-' -> num1 - num2;
            case '*' -> num1 * num2;
            case '/' -> num1 / num2;
            case '%' -> num1 % num2;
            default -> Math.pow(num1, num2);
        };
    }
}
