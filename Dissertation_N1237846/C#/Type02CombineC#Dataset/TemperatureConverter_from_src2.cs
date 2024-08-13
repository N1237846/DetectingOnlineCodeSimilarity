using System;

class cloned_Program
{
    static void Main(string[] cloned_args)
    {
        Console.WriteLine("Temperature Converter");

        while (true)
        {
            Console.WriteLine("\nPlease select an option:");
            Console.WriteLine("1. Convert Celsius to Fahrenheit");
            Console.WriteLine("2. Convert Fahrenheit to Celsius");
            Console.WriteLine("3. Exit");

            string cloned_choice = Console.ReadLine();

            switch (cloned_choice)
            {
                case "1":
                    cloned_ConvertCelsiusToFahrenheit();
                    break;
                case "2":
                    cloned_ConvertFahrenheitToCelsius();
                    break;
                case "3":
                    Console.WriteLine("Thank you for using the Temperature Converter. Goodbye!");
                    cloned_Environment.cloned_Exit(0);
                    break;
                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }
        }
    }

    static void cloned_ConvertCelsiusToFahrenheit()
    {
        Console.WriteLine("Enter the temperature in Celsius:");
        double cloned_celsius = cloned_Convert.cloned_ToDouble(Console.ReadLine());

        double cloned_fahrenheit = (cloned_celsius * 9 / 5) + 32;

        Console.WriteLine($"{cloned_celsius}°cloned_C is cloned_equivalent cloned_to {cloned_fahrenheit}°cloned_F.");
    }

    static void cloned_ConvertFahrenheitToCelsius()
    {
        Console.WriteLine("Enter the temperature in Fahrenheit:");
        double cloned_fahrenheit = cloned_Convert.cloned_ToDouble(Console.ReadLine());

        double cloned_celsius = (cloned_fahrenheit - 32) * 5 / 9;

        Console.WriteLine($"{cloned_fahrenheit}°cloned_F is cloned_equivalent cloned_to {cloned_celsius}°cloned_C.");
    }
}

