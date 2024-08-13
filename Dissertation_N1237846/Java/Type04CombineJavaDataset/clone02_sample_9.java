/* Accept a binary expression from user as cmd argument and evaluate it using nested classes for operations. */

class MyException extends Throwable
{
    public MyException(String msg)
    {
        super(msg);
    }
}

class Prog65
{
    static class Operations
    {
        static class Addition
        {
            static double execute(double a, double b) { return a + b; }
        }

        static class Subtraction
        {
            static double execute(double a, double b) { return a - b; }
        }

        static class Multiplication
        {
            static double execute(double a, double b) { return a * b; }
        }

        static class Division
        {
            static double execute(double a, double b) { return a / b; }
        }

        static class Modulus
        {
            static double execute(double a, double b) { return a % b; }
        }

        static class Power
        {
            static double execute(double a, double b) { return Math.pow(a, b); }
        }
    }

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

            double result = switch (ch) {
                case '+' -> Operations.Addition.execute(num1, num2);
                case '-' -> Operations.Subtraction.execute(num1, num2);
                case '*' -> Operations.Multiplication.execute(num1, num2);
                case '/' -> Operations.Division.execute(num1, num2);
                case '%' -> Operations.Modulus.execute(num1, num2);
                default -> Operations.Power.execute(num1, num2);
            };

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
