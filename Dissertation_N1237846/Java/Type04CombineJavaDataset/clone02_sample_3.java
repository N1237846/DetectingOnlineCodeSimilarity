/* Accept a binary expression from user as cmd argument and evaluate it using ternary operators and inline conditionals. */

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
            if (!"+-/*%$".contains(String.valueOf(ch)))
                throw new MyException("Please enter the valid operator");

            double num1 = Double.parseDouble(args[0]);
            double num2 = Double.parseDouble(args[2]);

            double result = (ch == '+') ? num1 + num2 :
                            (ch == '-') ? num1 - num2 :
                            (ch == '*') ? num1 * num2 :
                            (ch == '/') ? num1 / num2 :
                            (ch == '%') ? num1 % num2 :
                            Math.pow(num1, num2);

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
}
