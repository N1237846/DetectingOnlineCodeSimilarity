using System;

class Calculator {
    static void Main(string[] args) {
        double num1, num2, result;
        char op;

        Console.Write("Input first number: ");
        num1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Input second number: ");
        num2 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Select an operator (+, -, *, /): ");
        op = Convert.ToChar(Console.ReadLine());

        switch(op) {
            case '+':
                result = num1 + num2;
                Console.WriteLine($"Addition: {num1} + {num2} = {result}");
                break;

            case '-':
                result = num1 - num2;
                Console.WriteLine($"Subtraction: {num1} - {num2} = {result}");
                break;

            case '*':
                result = num1 * num2;
                Console.WriteLine($"Multiplication: {num1} * {num2} = {result}");
                break;

            case '/':
                if (num2 == 0) {
                    Console.WriteLine("Error: Division by zero is not allowed.");
                } else {
                    result = num1 / num2;
                    Console.WriteLine($"Division: {num1} / {num2} = {result}");
                }
                break;

            default:
                Console.WriteLine("Invalid operator entered. Use +, -, *, or /.");
                break;
        }
    }
}
