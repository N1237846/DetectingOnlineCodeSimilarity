using System;

class Calculator {
    static void Main(string[] args) {
        double num1, num2, result;
        char op;

        Console.Write("Enter first number: ");
        num1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter second number: ");
        num2 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Choose operator (+, -, *, /): ");
        op = Convert.ToChar(Console.ReadLine());

        if (num1 < 0 || num2 < 0) {
            Console.WriteLine("Error: Only positive numbers are allowed.");
            return;
        }

        switch(op) {
            case '+':
                result = num1 + num2;
                Console.WriteLine($"{num1} plus {num2} equals {result}");
                break;

            case '-':
                result = num1 - num2;
                Console.WriteLine($"{num1} minus {num2} equals {result}");
                break;

            case '*':
                result = num1 * num2;
                Console.WriteLine($"{num1} multiplied by {num2} equals {result}");
                break;

            case '/':
                if (num2 == 0) {
                    Console.WriteLine("Division by zero is not allowed.");
                } else {
                    result = num1 / num2;
                    Console.WriteLine($"{num1} divided by {num2} equals {result}");
                }
                break;

            default:
                Console.WriteLine("Invalid operator. Please use +, -, *, or /.");
                break;
        }
    }
}
