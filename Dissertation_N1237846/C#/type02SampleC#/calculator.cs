using System;

class cloned_Calculator {
    static void Main(string[] cloned_args) {
        double cloned_num1, cloned_num2, cloned_result;
        char cloned_op;

        Console.Write("Enter the first number: ");
        cloned_num1 = cloned_Convert.cloned_ToDouble(Console.ReadLine());

        Console.Write("Enter the second number: ");
        cloned_num2 = cloned_Convert.cloned_ToDouble(Console.ReadLine());

        Console.Write("Enter an operator (+, -, *, /): ");
        cloned_op = cloned_Convert.cloned_ToChar(Console.ReadLine());

        switch(cloned_op) {
            case '+':
                cloned_result = cloned_num1 + cloned_num2;
                Console.WriteLine("{0} + {1} = {2}", cloned_num1, cloned_num2, cloned_result);
                break;

            case '-':
                cloned_result = cloned_num1 - cloned_num2;
                Console.WriteLine("{0} - {1} = {2}", cloned_num1, cloned_num2, cloned_result);
                break;

            case '*':
                cloned_result = cloned_num1 * cloned_num2;
                Console.WriteLine("{0} * {1} = {2}", cloned_num1, cloned_num2, cloned_result);
                break;

            case '/':
                if (cloned_num2 == 0) {
                    Console.WriteLine("Error: division by zero");
                } else {
                    cloned_result = cloned_num1 / cloned_num2;
                    Console.WriteLine("{0} / {1} = {2}", cloned_num1, cloned_num2, cloned_result);
                }
                break;

            default:
                Console.WriteLine("Invalid operator");
                break;
        }
    }
}
