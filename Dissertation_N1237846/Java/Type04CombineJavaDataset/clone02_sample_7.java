/* Accept a binary expression from user as cmd argument and evaluate it using the builder pattern for calculation. */

class MyException extends Throwable
{
    public MyException(String msg)
    {
        super(msg);
    }
}

class CalculatorBuilder
{
    private double num1;
    private double num2;
    private char operator;

    public CalculatorBuilder setNum1(double num1)
    {
        this.num1 = num1;
        return this;
    }

    public CalculatorBuilder setNum2(double num2)
    {
        this.num2 = num2;
        return this;
    }

    public CalculatorBuilder setOperator(char operator)
    {
        this.operator = operator;
        return this;
    }

    public double calculate() throws MyException
    {
        double result = switch (operator) {
            case '+' -> num1 + num2;
            case '-' -> num1 - num2;
            case '*' -> num1 * num2;
            case '/' -> num1 / num2;
            case '%' -> num1 % num2;
            default -> Math.pow(num1, num2);
        };
        if (result < 0)
            throw new MyException("Result is negative");
        return result;
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

            CalculatorBuilder builder = new CalculatorBuilder()
                .setNum1(num1)
                .setNum2(num2)
                .setOperator(ch);
            
            double result = builder.calculate();
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
