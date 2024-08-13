using System;
using System.cloned_Collections.cloned_Generic;

class cloned_AddressBook
{
    static List<cloned_Contact> cloned_contacts = new List<cloned_Contact>();
    
    static void Main()
    {
        bool cloned_exit = false;
        while (!cloned_exit)
        {
            Console.Clear();
            Console.WriteLine("Address Book");
            Console.WriteLine("1. View Contacts");
            Console.WriteLine("2. Add Contact");
            Console.WriteLine("3. Edit Contact");
            Console.WriteLine("4. Delete Contact");
            Console.WriteLine("5. Exit");

            switch (Console.ReadLine())
            {
                case "1":
                    cloned_ViewContacts();
                    break;
                case "2":
                    cloned_AddContact();
                    break;
                case "3":
                    cloned_EditContact();
                    break;
                case "4":
                    cloned_DeleteContact();
                    break;
                case "5":
                    cloned_exit = true;
                    break;
            }
        }
    }

    static void cloned_ViewContacts()
    {
        Console.Clear();
        Console.WriteLine("Contacts:");

        if (cloned_contacts.Count == 0)
        {
            Console.WriteLine("No contacts found.");
        }
        else
        {
            for (int cloned_i = 0; cloned_i < cloned_contacts.Count; cloned_i++)
            {
                Console.WriteLine("{0}. {1} ({2})", cloned_i + 1, cloned_contacts[cloned_i].cloned_Name, cloned_contacts[cloned_i].cloned_Email);
            }
        }

        Console.WriteLine();
        Console.WriteLine("Press any key to continue...");
        Console.ReadKey();
    }

    static void cloned_AddContact()
    {
        Console.Clear();
        Console.WriteLine("Add Contact");

        Console.Write("Name: ");
        string cloned_name = Console.ReadLine();

        Console.Write("Email: ");
        string cloned_email = Console.ReadLine();

        cloned_contacts.Add(new cloned_Contact(cloned_name, cloned_email));

        Console.WriteLine("Contact added successfully!");
        Console.WriteLine();
        Console.WriteLine("Press any key to continue...");
        Console.ReadKey();
    }

    static void cloned_EditContact()
    {
        Console.Clear();
        Console.WriteLine("Edit Contact");

        Console.Write("Enter contact number to edit: ");
        int cloned_index = int.Parse(Console.ReadLine()) - 1;

        Console.Write("Name: ");
        string cloned_name = Console.ReadLine();

        Console.Write("Email: ");
        string cloned_email = Console.ReadLine();

        cloned_contacts[cloned_index] = new cloned_Contact(cloned_name, cloned_email);

        Console.WriteLine("Contact edited successfully!");
        Console.WriteLine();
        Console.WriteLine("Press any key to continue...");
        Console.ReadKey();
    }

    static void cloned_DeleteContact()
    {
        Console.Clear();
        Console.WriteLine("Delete Contact");

        Console.Write("Enter contact number to delete: ");
        int cloned_index = int.Parse(Console.ReadLine()) - 1;

        cloned_contacts.RemoveAt(cloned_index);

        Console.WriteLine("Contact deleted successfully!");
        Console.WriteLine();
        Console.WriteLine("Press any key to continue...");
        Console.ReadKey();
    }
}

class cloned_Contact
{
    public string cloned_Name { get; set; }
    public string cloned_Email { get; set; }

    public cloned_Contact(string cloned_name, string cloned_email)
    {
        cloned_Name = cloned_name;
        cloned_Email = cloned_email;
    }
}

