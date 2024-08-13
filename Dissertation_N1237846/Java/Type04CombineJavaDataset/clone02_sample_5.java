/* Accept a binary expression from user as cmd argument and evaluate it using streams for validation and calculation. */

import java.util.stream.Stream;

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
            if (Stream.of('+', '-', '*', '/', '%', '$').noneMatch(op -> op == ch))
                throw new MyException("Please enter the valid operator");

            double num1 = Double.parseDouble(args[0]);
            double num2 = Double.parseDouble(args[2]);

            double result = calculate(ch, num1, num2);
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

    static double calculate(char operator, double num1, double num2)
    {
        return Stream.of(new Object[][] {
                {'+', (BiFunction<Double, Double, Double>) Double::sum},
                {'-', (BiFunction<Double, Double, Double>) (a, b) -> a - b},
                {'*', (BiFunction<Double, Double, Double>) (a, b) -> a * b},
                {'/', (BiFunction<Double, Double, Double>) (a, b) -> a / b},
                {'%', (BiFunction<Double, Double, Double>) (a, b) -> a % b},
                {'$', (BiFunction<Double, Double, Double>) Math::pow}
        }).filter(op -> (char) op[0] == operator)
          .map(op -> ((BiFunction<Double, Double, Double>) op[1]).apply(num1, num2))
          .findFirst()
          .orElse(0.0);
    }
}
