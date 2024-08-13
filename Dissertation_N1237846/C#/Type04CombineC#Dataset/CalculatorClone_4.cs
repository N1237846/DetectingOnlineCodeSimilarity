using System;

class Calculator {
    static void Main(string[] args) {
        double num1, num2, result;
        char op;

        Console.Write("Enter number 1: ");
        num1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter number 2: ");
        num2 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter operator (+, -, *, /): ");
        op = Convert.ToChar(Console.ReadLine());

        switch(op) {
            case '+':
                result = num1 + num2;
                Console.WriteLine($"Sum of {num1} and {num2} is {result}");
                break;

            case '-':
                result = num1 - num2;
                Console.WriteLine($"Difference between {num1} and {num2} is {result}");
                break;

            case '*':
                result = num1 * num2;
                Console.WriteLine($"Product of {num1} and {num2} is {result}");
                break;

            case '/':
                if (num2 == 0) {
                    Console.WriteLine("Error: Cannot divide by zero.");
                } else {
                    result = num1 / num2;
                    Console.WriteLine($"Quotient of {num1} divided by {num2} is {result}");
                }
                break;

            default:
                Console.WriteLine("Invalid operator. Please input a correct operator.");
                break;
        }
    }
}
