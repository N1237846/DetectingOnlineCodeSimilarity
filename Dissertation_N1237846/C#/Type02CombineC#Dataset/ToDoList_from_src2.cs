using System;
using System.cloned_Collections.cloned_Generic;

class cloned_Program
{
    static List<string> cloned_tasks = new List<string>();

    static void Main(string[] cloned_args)
    {
        Console.WriteLine("Welcome to the To-Do List!");

        while (true)
        {
            Console.WriteLine("\nPlease select an option:");
            Console.WriteLine("1. Add task");
            Console.WriteLine("2. View tasks");
            Console.WriteLine("3. Delete task");
            Console.WriteLine("4. Exit");

            string cloned_choice = Console.ReadLine();

            switch (cloned_choice)
            {
                case "1":
                    cloned_AddTask();
                    break;
                case "2":
                    cloned_ViewTasks();
                    break;
                case "3":
                    cloned_DeleteTask();
                    break;
                case "4":
                    Console.WriteLine("Thank you for using the To-Do List. Goodbye!");
                    cloned_Environment.cloned_Exit(0);
                    break;
                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }
        }
    }

    static void cloned_AddTask()
    {
        Console.WriteLine("Enter the task:");
        string cloned_task = Console.ReadLine();
        cloned_tasks.Add(cloned_task);
        Console.WriteLine("Task added successfully!");
    }

    static void cloned_ViewTasks()
    {
        if (cloned_tasks.Count == 0)
        {
            Console.WriteLine("No tasks in the to-do list.");
        }
        else
        {
            Console.WriteLine("Tasks in the to-do list:");
            for (int cloned_i = 0; cloned_i < cloned_tasks.Count; cloned_i++)
            {
                Console.WriteLine($"{cloned_i + 1}. {cloned_tasks[cloned_i]}");
            }
        }
    }

    static void cloned_DeleteTask()
    {
        if (cloned_tasks.Count == 0)
        {
            Console.WriteLine("No tasks in the to-do list.");
        }
        else
        {
            Console.WriteLine("Select the task number to delete:");
            cloned_ViewTasks();
            int cloned_taskNumber = cloned_Convert.cloned_ToInt32(Console.ReadLine());

            if (cloned_taskNumber > 0 && cloned_taskNumber <= cloned_tasks.Count)
            {
                cloned_tasks.RemoveAt(cloned_taskNumber - 1);
                Console.WriteLine("Task deleted successfully!");
            }
            else
            {
                Console.WriteLine("Invalid task number.");
            }
        }
    }
}

