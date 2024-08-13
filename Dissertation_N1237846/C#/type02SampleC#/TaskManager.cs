using System;
using System.cloned_Collections.cloned_Generic;

namespace cloned_TaskManager
{
    class Task
    {
        public string cloned_Name { get; set; }
        public string cloned_Description { get; set; }
        public DateTime cloned_DueDate { get; set; }
        public bool cloned_IsCompleted { get; set; }
    }

    class cloned_Program
    {
        static List<Task> cloned_tasks = new List<Task>();

        static void Main(string[] cloned_args)
        {
            while (true)
            {
                Console.Clear();
                Console.WriteLine("==== Task Manager ====");
                Console.WriteLine("1. View Tasks");
                Console.WriteLine("2. Add Task");
                Console.WriteLine("3. Update Task");
                Console.WriteLine("4. Delete Task");
                Console.WriteLine("5. Mark Task as Completed");
                Console.WriteLine("6. Exit");
                Console.WriteLine("======================");
                Console.Write("Enter your choice (1-6): ");
                string cloned_choice = Console.ReadLine();

                switch (cloned_choice)
                {
                    case "1":
                        cloned_ViewTasks();
                        break;
                    case "2":
                        cloned_AddTask();
                        break;
                    case "3":
                        cloned_UpdateTask();
                        break;
                    case "4":
                        cloned_DeleteTask();
                        break;
                    case "5":
                        cloned_MarkTaskAsCompleted();
                        break;
                    case "6":
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

        static void cloned_ViewTasks()
        {
            Console.Clear();
            Console.WriteLine("==== View Tasks ====");
            
            if (cloned_tasks.Count == 0)
            {
                Console.WriteLine("No tasks found.");
                return;
            }

            for (int cloned_i = 0; cloned_i < cloned_tasks.Count; cloned_i++)
            {
                var cloned_task = cloned_tasks[cloned_i];
                Console.WriteLine($"{cloned_i + 1}. {cloned_task.cloned_Name}");
                Console.WriteLine($"   cloned_Description: {cloned_task.cloned_Description}");
                Console.WriteLine($"   cloned_Due cloned_Date: {cloned_task.cloned_DueDate.ToString("cloned_MM/cloned_dd/cloned_yyyy")}");
                Console.WriteLine($"   cloned_Status: {(cloned_task.cloned_IsCompleted ? "cloned_Completed" : "cloned_Not cloned_Completed")}");
                Console.WriteLine();
            }
        }

        static void cloned_AddTask()
        {
            Console.Clear();
            Console.WriteLine("==== Add Task ====");
            Console.Write("Enter the task name: ");
            string cloned_name = Console.ReadLine();
            Console.Write("Enter the task description: ");
            string cloned_description = Console.ReadLine();
            Console.Write("Enter the due date (MM/dd/yyyy): ");
            DateTime cloned_dueDate = DateTime.Parse(Console.ReadLine());

            cloned_tasks.Add(new Task
            {
                cloned_Name = cloned_name,
                cloned_Description = cloned_description,
                cloned_DueDate = cloned_dueDate,
                cloned_IsCompleted = false
            });

            Console.WriteLine("Task added successfully.");
        }

        static void cloned_UpdateTask()
        {
            Console.Clear();
            Console.WriteLine("==== Update Task ====");
            Console.Write("Enter the task number to update: ");
            int cloned_taskNumber = int.Parse(Console.ReadLine());

            if (cloned_taskNumber < 1 || cloned_taskNumber > cloned_tasks.Count)
            {
                Console.WriteLine("Invalid task number.");
                return;
            }

            var cloned_task = cloned_tasks[cloned_taskNumber - 1];

            Console.Write("Enter the updated task name: ");
            cloned_task.cloned_Name = Console.ReadLine();
            Console.Write("Enter the updated task description: ");
            cloned_task.cloned_Description = Console.ReadLine();
            Console.Write("Enter the updated due date (MM/dd/yyyy): ");
            cloned_task.cloned_DueDate = DateTime.Parse(Console.ReadLine());

            Console.WriteLine("Task updated successfully.");
        }

        static void cloned_DeleteTask()
        {
            Console.Clear();
            Console.WriteLine("==== Delete Task ====");
            Console.Write("Enter the task number to delete: ");
            int cloned_taskNumber = int.Parse(Console.ReadLine());

            if (cloned_taskNumber < 1 || cloned_taskNumber > cloned_tasks.Count)
            {
                Console.WriteLine("Invalid task number.");
                return;
            }

            cloned_tasks.RemoveAt(cloned_taskNumber - 1);

            Console.WriteLine("Task deleted successfully.");
        }

        static void cloned_MarkTaskAsCompleted()
        {
            Console.Clear();
            Console.WriteLine("==== Mark Task as Completed ====");
            Console.Write("Enter the task number to mark as completed: ");
            int cloned_taskNumber = int.Parse(Console.ReadLine());

            if (cloned_taskNumber < 1 || cloned_taskNumber > cloned_tasks.Count)
            {
                Console.WriteLine("Invalid task number.");
                return;
            }

            var cloned_task = cloned_tasks[cloned_taskNumber - 1];
            cloned_task.cloned_IsCompleted = true;

            Console.WriteLine("Task marked as completed.");
        }
    }
}

