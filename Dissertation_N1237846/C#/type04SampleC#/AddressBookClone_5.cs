using System;
using System.Collections.Generic;

interface IAction
{
    void Execute();
}

class ViewAction : IAction
{
    public void Execute()
    {
        Console.Clear();
        Console.WriteLine("Contacts:");

        if (AddressBook.contacts.Count == 0)
        {
            Console.WriteLine("No contacts found.");
        }
        else
        {
            for (int i = 0; i < AddressBook.contacts.Count; i++)
            {
                Console.WriteLine("{0}. {1} ({2})", i + 1, AddressBook.contacts[i].Name, AddressBook.contacts[i].Email);
            }
        }

        Console.WriteLine();
        Console.WriteLine("Press any key to continue...");
        Console.ReadKey();
    }
}

class AddAction : IAction
{
    public void Execute()
    {
        Console.Clear();
        Console.WriteLine("Add Contact");

        Console.Write("Name: ");
        string name = Console.ReadLine();

        Console.Write("Email: ");
        string email = Console.ReadLine();

        AddressBook.contacts.Add(new Contact(name, email));

        Console.WriteLine("Contact added successfully!");
        Console.WriteLine();
        Console.WriteLine("Press any key to continue...");
        Console.ReadKey();
    }
}

class EditAction : IAction
{
    public void Execute()
    {
        Console.Clear();
        Console.WriteLine("Edit Contact");

        Console.Write("Enter contact number to edit: ");
        int index = int.Parse(Console.ReadLine()) - 1;

        Console.Write("Name: ");
        string name = Console.ReadLine();

        Console.Write("Email: ");
        string email = Console.ReadLine();

        AddressBook.contacts[index] = new Contact(name, email);

        Console.WriteLine("Contact edited successfully!");
        Console.WriteLine();
        Console.WriteLine("Press any key to continue...");
        Console.ReadKey();
    }
}

class DeleteAction : IAction
{
    public void Execute()
    {
        Console.Clear();
        Console.WriteLine("Delete Contact");

        Console.Write("Enter contact number to delete: ");
        int index = int.Parse(Console.ReadLine()) - 1;

        AddressBook.contacts.RemoveAt(index);

        Console.WriteLine("Contact deleted successfully!");
        Console.WriteLine();
        Console.WriteLine("Press any key to continue...");
        Console.ReadKey();
    }
}

class AddressBook
{
    public static List<Contact> contacts = new List<Contact>();
    
    static void Main()
    {
        var actions = new Dictionary<string, IAction>
        {
            { "1", new ViewAction() },
            { "2", new AddAction() },
            { "3", new EditAction() },
            { "4", new DeleteAction() }
        };
        
        bool exit = false;
        while (!exit)
        {
            Console.Clear();
            Console.WriteLine("Address Book");
            Console.WriteLine("1. View Contacts");
            Console.WriteLine("2. Add Contact");
            Console.WriteLine("3. Edit Contact");
            Console.WriteLine("4. Delete Contact");
            Console.WriteLine("5. Exit");

            string choice = Console.ReadLine();
            if (choice == "5")
            {
                exit = true;
            }
            else if (actions.ContainsKey(choice))
            {
                actions[choice].Execute();
            }
            else
            {
                Console.WriteLine("Invalid choice. Please select a valid option.");
            }
        }
    }
}

class Contact
{
    public string Name { get; set; }
    public string Email { get; set; }

    public Contact(string name, string email)
    {
        Name = name;
        Email = email;
    }
}
