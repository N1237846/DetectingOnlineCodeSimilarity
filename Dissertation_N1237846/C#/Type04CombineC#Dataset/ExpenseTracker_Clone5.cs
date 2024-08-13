using System;
using System.Collections.Generic;
using System.Linq;

namespace ExpenseTracker
{
    class Expense
    {
        public decimal Amount { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
        public DateTime Date { get; set; }
    }

    class Program
    {
        static List<Expense> expenses = new List<Expense>();

        static void Main(string[] args)
        {
            while (true)
            {
                Console.Clear();
                Console.WriteLine("==== Expense Tracker ====");
                Console.WriteLine("1. Enter Expense");
                Console.WriteLine("2. Categorize Expenses");
                Console.WriteLine("3. Monthly Budgeting");
                Console.WriteLine("4. View Reports");
                Console.WriteLine("5. Exit");
                Console.WriteLine("==========================");
                Console.Write("Enter your choice (1-5): ");
                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        EnterExpense();
                        break;
                    case "2":
                        CategorizeExpenses();
                        break;
                    case "3":
                        MonthlyBudgeting();
                        break;
                    case "4":
                        ViewReports();
                        break;
                    case "5":
                        Environment.Exit(0);
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }

                Console.WriteLine("
Press any key to continue...");
                Console.ReadKey();
            }
        }

        static void EnterExpense()
        {
            Console.Clear();
            Console.WriteLine("==== Enter Expense ====");
            Console.Write("Enter the amount: ");
            decimal amount = decimal.Parse(Console.ReadLine());
            Console.Write("Enter the description: ");
            string description = Console.ReadLine();
            Console.Write("Enter the category: ");
            string category = Console.ReadLine();
            DateTime date = DateTime.Now;

            expenses.Add(new Expense
            {
                Amount = amount,
                Description = description,
                Category = category,
                Date = date
            });

            Console.WriteLine("Expense entered successfully.");
        }

        static void CategorizeExpenses()
        {
            Console.Clear();
            Console.WriteLine("==== Categorize Expenses ====");

            if (!expenses.Any())
            {
                Console.WriteLine("No expenses found.");
                return;
            }

            Console.WriteLine("Expense List:");
            var expenseList = expenses
                .Select((e, i) => new { e, index = i + 1 })
                .ToList();

            expenseList.ForEach(e => Console.WriteLine($"{e.index}. Amount: {e.e.Amount}, Description: {e.e.Description}"));

            Console.Write("Enter the expense number to categorize: ");
            if (int.TryParse(Console.ReadLine(), out int expenseNumber) &&
                expenseNumber >= 1 && expenseNumber <= expenses.Count)
            {
                var expense = expenses[expenseNumber - 1];

                Console.Write("Enter the category: ");
                string category = Console.ReadLine();

                var updatedExpense = new Expense
                {
                    Amount = expense.Amount,
                    Description = expense.Description,
                    Category = category,
                    Date = expense.Date
                };

                expenses[expenseNumber - 1] = updatedExpense;

                Console.WriteLine("Expense categorized successfully.");
            }
            else
            {
                Console.WriteLine("Invalid expense number.");
            }
        }

        static void MonthlyBudgeting()
        {
            Console.Clear();
            Console.WriteLine("==== Monthly Budgeting ====");

            if (!expenses.Any())
            {
                Console.WriteLine("No expenses found.");
                return;
            }

            Console.WriteLine("Expense List:");
            var expenseList = expenses
                .Select((e, i) => new { e, index = i + 1 })
                .ToList();

            expenseList.ForEach(e => Console.WriteLine($"{e.index}. Amount: {e.e.Amount}, Category: {e.e.Category}"));

            Console.Write("Enter the month (1-12): ");
            if (int.TryParse(Console.ReadLine(), out int month) &&
                month >= 1 && month <= 12)
            {
                Console.Write("Enter the year: ");
                if (int.TryParse(Console.ReadLine(), out int year))
                {
                    var totalExpense = expenses
                        .Where(e => e.Date.Month == month && e.Date.Year == year)
                        .Sum(e => e.Amount);

                    Console.WriteLine($"Total expenses for {month}/{year}: {totalExpense}");
                }
                else
                {
                    Console.WriteLine("Invalid year.");
                }
            }
            else
            {
                Console.WriteLine("Invalid month number.");
            }
        }

        static void ViewReports()
        {
            Console.Clear();
            Console.WriteLine("==== View Reports ====");

            if (!expenses.Any())
            {
                Console.WriteLine("No expenses found.");
                return;
            }

            Console.WriteLine("Expense List:");
            var expenseList = expenses
                .Select((e, i) => new { e, index = i + 1 })
                .ToList();

            expenseList.ForEach(e => Console.WriteLine($"{e.index}. Amount: {e.e.Amount}, Category: {e.e.Category}"));

            Console.Write("Enter the category to view expenses: ");
            string category = Console.ReadLine();

            var categoryExpenses = expenses
                .Where(e => e.Category == category)
                .ToList();

            if (categoryExpenses.Any())
            {
                Console.WriteLine($"Expenses for Category: {category}");
                categoryExpenses
                    .Select(e => $"Amount: {e.Amount}, Description: {e.Description}")
                    .ToList()
                    .ForEach(Console.WriteLine);
            }
            else
            {
                Console.WriteLine("No expenses found for the category.");
            }
        }
    }
}
