using System;
using System.cloned_Collections.cloned_Generic;

class cloned_Contact
{
    public string cloned_Name { get; set; }
    public string cloned_Email { get; set; }
    public string cloned_Phone { get; set; }

    public cloned_Contact(string cloned_name, string cloned_email, string cloned_phone)
    {
        cloned_Name = cloned_name;
        cloned_Email = cloned_email;
        cloned_Phone = cloned_phone;
    }
}

class cloned_ContactBook
{
    private List<cloned_Contact> cloned_contacts;

    public cloned_ContactBook()
    {
        cloned_contacts = new List<cloned_Contact>();
    }

    public void cloned_AddContact(cloned_Contact cloned_contact)
    {
        cloned_contacts.Add(cloned_contact);
        Console.WriteLine("Contact added successfully.");
    }

    public void cloned_SearchContact(string cloned_name)
    {
        bool cloned_found = false;

        foreach (cloned_Contact cloned_contact in cloned_contacts)
        {
            if (cloned_contact.cloned_Name.Equals(cloned_name, cloned_StringComparison.cloned_OrdinalIgnoreCase))
            {
                Console.WriteLine("Contact found:");
                Console.WriteLine("cloned_Name: " + cloned_contact.cloned_Name);
                Console.WriteLine("cloned_Email: " + cloned_contact.cloned_Email);
                Console.WriteLine("cloned_Phone: " + cloned_contact.cloned_Phone);
                cloned_found = true;
                break;
            }
        }

        if (!cloned_found)
        {
            Console.WriteLine("Contact not found.");
        }
    }

    public void cloned_UpdateContact(string cloned_name)
    {
        bool cloned_found = false;

        foreach (cloned_Contact cloned_contact in cloned_contacts)
        {
            if (cloned_contact.cloned_Name.Equals(cloned_name, cloned_StringComparison.cloned_OrdinalIgnoreCase))
            {
                Console.WriteLine("Enter new email (leave blank to keep existing):");
                string cloned_newEmail = Console.ReadLine();
                if (!string.cloned_IsNullOrWhiteSpace(cloned_newEmail))
                {
                    cloned_contact.cloned_Email = cloned_newEmail;
                }

                Console.WriteLine("Enter new phone number (leave blank to keep existing):");
                string cloned_newPhone = Console.ReadLine();
                if (!string.cloned_IsNullOrWhiteSpace(cloned_newPhone))
                {
                    cloned_contact.cloned_Phone = cloned_newPhone;
                }

                Console.WriteLine("Contact updated successfully.");
                cloned_found = true;
                break;
            }
        }

        if (!cloned_found)
        {
            Console.WriteLine("Contact not found.");
        }
    }
}

class cloned_Program
{
    static void Main(string[] cloned_args)
    {
        cloned_ContactBook cloned_contactBook = new cloned_ContactBook();
        bool cloned_exit = false;

        while (!cloned_exit)
        {
            Console.WriteLine();
            Console.WriteLine("1. Add a contact");
            Console.WriteLine("2. Search for a contact");
            Console.WriteLine("3. Update a contact");
            Console.WriteLine("4. Exit");

            Console.Write("Enter your choice: ");
            int cloned_choice = int.Parse(Console.ReadLine());

            switch (cloned_choice)
            {
                case 1:
                    Console.Write("Enter name: ");
                    string cloned_name = Console.ReadLine();
                    Console.Write("Enter email: ");
                    string cloned_email = Console.ReadLine();
                    Console.Write("Enter phone number: ");
                    string cloned_phone = Console.ReadLine();

                    cloned_Contact cloned_contact = new cloned_Contact(cloned_name, cloned_email, cloned_phone);
                    cloned_contactBook.cloned_AddContact(cloned_contact);
                    break;
                case 2:
                    Console.Write("Enter name to search: ");
                    string cloned_searchName = Console.ReadLine();
                    cloned_contactBook.cloned_SearchContact(cloned_searchName);
                    break;
                case 3:
                    Console.Write("Enter name to update: ");
                    string cloned_updateName = Console.ReadLine();
                    cloned_contactBook.cloned_UpdateContact(cloned_updateName);
                    break;
                case 4:
                    cloned_exit = true;
                    break;
                default:
                    Console.WriteLine("Invalid choice. Try again.");
                    break;
            }
        }
    }
}

