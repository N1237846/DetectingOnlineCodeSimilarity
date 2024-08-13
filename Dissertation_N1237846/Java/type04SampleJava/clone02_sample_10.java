/* Accept a binary expression from user as cmd argument and evaluate it using reflection for operation execution. */

import java.lang.reflect.Method;

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

            String methodName = getMethodName(ch);
            Method method = Prog65.class.getDeclaredMethod(methodName, double.class, double.class);
            double result = (double) method.invoke(null, num1, num2);

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

    static String getMethodName(char operator)
    {
        return switch (operator) {
            case '+' -> "add";
            case '-' -> "subtract";
            case '*' -> "multiply";
            case '/' -> "divide";
            case '%' -> "modulus";
            default -> "power";
        };
    }

    static double add(double a, double b) { return a + b; }
    static double subtract(double a, double b) { return a - b; }
    static double multiply(double a, double b) { return a * b; }
    static double divide(double a, double b) { return a / b; }
    static double modulus(double a, double b) { return a % b; }
    static double power(double a, double b) { return Math.pow(a, b); }
}
