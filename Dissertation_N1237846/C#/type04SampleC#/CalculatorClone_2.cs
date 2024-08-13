using System;

class Calculator {
    static void Main(string[] args) {
        double num1, num2, result;
        char op;

        Console.Write("First number: ");
        num1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Second number: ");
        num2 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Operator (+, -, *, /): ");
        op = Convert.ToChar(Console.ReadLine());

        switch(op) {
            case '+':
                result = num1 + num2;
                Console.WriteLine("Addition result: {0} + {1} = {2}", num1, num2, result);
                break;

            case '-':
                result = num1 - num2;
                Console.WriteLine("Subtraction result: {0} - {1} = {2}", num1, num2, result);
                break;

            case '*':
                result = num1 * num2;
                Console.WriteLine("Multiplication result: {0} * {1} = {2}", num1, num2, result);
                break;

            case '/':
                if (num2 == 0) {
                    Console.WriteLine("Cannot divide by zero.");
                } else {
                    result = num1 / num2;
                    Console.WriteLine("Division result: {0} / {1} = {2}", num1, num2, result);
                }
                break;

            default:
                Console.WriteLine("Invalid operator. Please enter a valid operator.");
                break;
        }
    }
}
