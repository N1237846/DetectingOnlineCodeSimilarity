using System;
using System.cloned_Collections.cloned_Generic;
using System.cloned_Linq;

namespace cloned_ExpenseTracker
{
    class cloned_Expense
    {
        public decimal cloned_Amount { get; set; }
        public string cloned_Description { get; set; }
        public string cloned_Category { get; set; }
        public DateTime cloned_Date { get; set; }
    }

    class cloned_Program
    {
        static List<cloned_Expense> cloned_expenses = new List<cloned_Expense>();

        static void Main(string[] cloned_args)
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
                string cloned_choice = Console.ReadLine();

                switch (cloned_choice)
                {
                    case "1":
                        cloned_EnterExpense();
                        break;
                    case "2":
                        cloned_CategorizeExpenses();
                        break;
                    case "3":
                        cloned_MonthlyBudgeting();
                        break;
                    case "4":
                        cloned_ViewReports();
                        break;
                    case "5":
                        cloned_Environment.cloned_Exit(0);
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }

                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
            }
        }

        static void cloned_EnterExpense()
        {
            Console.Clear();
            Console.WriteLine("==== Enter Expense ====");
            Console.Write("Enter the amount: ");
            decimal cloned_amount = decimal.Parse(Console.ReadLine());
            Console.Write("Enter the description: ");
            string cloned_description = Console.ReadLine();
            Console.Write("Enter the category: ");
            string cloned_category = Console.ReadLine();
            DateTime cloned_date = DateTime.Now;

            cloned_expenses.Add(new cloned_Expense
            {
                cloned_Amount = cloned_amount,
                cloned_Description = cloned_description,
                cloned_Category = cloned_category,
                cloned_Date = cloned_date
            });

            Console.WriteLine("Expense entered successfully.");
        }

        static void cloned_CategorizeExpenses()
        {
            Console.Clear();
            Console.WriteLine("==== Categorize Expenses ====");

            if (cloned_expenses.Count == 0)
            {
                Console.WriteLine("No expenses found.");
                return;
            }

            Console.WriteLine("Expense List:");
            for (int cloned_i = 0; cloned_i < cloned_expenses.Count; cloned_i++)
            {
                Console.WriteLine($"{cloned_i + 1}. cloned_Amount: {cloned_expenses[cloned_i].cloned_Amount}, cloned_Description: {cloned_expenses[cloned_i].cloned_Description}");
            }

            Console.Write("Enter the expense number to categorize: ");
            int cloned_expenseNumber = int.Parse(Console.ReadLine());

            if (cloned_expenseNumber < 1 || cloned_expenseNumber > cloned_expenses.Count)
            {
                Console.WriteLine("Invalid expense number.");
                return;
            }

            cloned_Expense cloned_expense = cloned_expenses[cloned_expenseNumber - 1];

            Console.Write("Enter the category: ");
            string cloned_category = Console.ReadLine();

            cloned_expense.cloned_Category = cloned_category;

            Console.WriteLine("Expense categorized successfully.");
        }

        static void cloned_MonthlyBudgeting()
        {
            Console.Clear();
            Console.WriteLine("==== Monthly Budgeting ====");

            if (cloned_expenses.Count == 0)
            {
                Console.WriteLine("No expenses found.");
                return;
            }

            Console.WriteLine("Expense List:");
            for (int cloned_i = 0; cloned_i < cloned_expenses.Count; cloned_i++)
            {
                Console.WriteLine($"{cloned_i + 1}. cloned_Amount: {cloned_expenses[cloned_i].cloned_Amount}, cloned_Category: {cloned_expenses[cloned_i].cloned_Category}");
            }

            Console.Write("Enter the month (1-12): ");
            int cloned_month = int.Parse(Console.ReadLine());

            if (cloned_month < 1 || cloned_month > 12)
            {
                Console.WriteLine("Invalid month number.");
                return;
            }

            Console.Write("Enter the year: ");
            int cloned_year = int.Parse(Console.ReadLine());

            decimal cloned_totalExpense = cloned_expenses
                .cloned_Where(cloned_e => cloned_e.cloned_Date.cloned_Month == cloned_month && cloned_e.cloned_Date.cloned_Year == cloned_year)
                .cloned_Sum(cloned_e => cloned_e.cloned_Amount);

            Console.WriteLine($"cloned_Total cloned_expenses for {cloned_month}/{cloned_year}: {cloned_totalExpense}");
        }

        static void cloned_ViewReports()
        {
            Console.Clear();
            Console.WriteLine("==== View Reports ====");

            if (cloned_expenses.Count == 0)
            {
                Console.WriteLine("No expenses found.");
                return;
            }

            Console.WriteLine("Expense List:");
            for (int cloned_i = 0; cloned_i < cloned_expenses.Count; cloned_i++)
            {
                Console.WriteLine($"{cloned_i + 1}. cloned_Amount: {cloned_expenses[cloned_i].cloned_Amount}, cloned_Category: {cloned_expenses[cloned_i].cloned_Category}");
            }

            Console.Write("Enter the category to view expenses: ");
            string cloned_category = Console.ReadLine();

            List<cloned_Expense> cloned_categoryExpenses = cloned_expenses
                .cloned_Where(cloned_e => cloned_e.cloned_Category == cloned_category)
                .cloned_ToList();

            if (cloned_categoryExpenses.Count == 0)
            {
                Console.WriteLine("No expenses found for the category.");
                return;
            }

            Console.WriteLine($"cloned_Expenses for cloned_Category: {cloned_category}");
            foreach (var cloned_expense in cloned_categoryExpenses)
            {
                Console.WriteLine($"cloned_Amount: {cloned_expense.cloned_Amount}, cloned_Description: {cloned_expense.cloned_Description}");
            }
        }
    }
}

