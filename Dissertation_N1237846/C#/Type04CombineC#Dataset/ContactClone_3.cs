using System;
using System.Collections.Generic;

class Contact
{
    public string Name { get; set; }
    public string Email { get; set; }
    public string Phone { get; set; }

    public Contact(string name, string email, string phone)
    {
        Name = name;
        Email = email;
        Phone = phone;
    }
}

class ContactBook
{
    private List<Contact> contacts;

    public ContactBook()
    {
        contacts = new List<Contact>();
    }

    public void AddContact(Contact contact)
    {
        contacts.Add(contact);
        Console.WriteLine("Contact added successfully.");
    }

    private Contact FindContactRecursive(List<Contact> contacts, string name, int index)
    {
        if (index >= contacts.Count) return null;
        if (contacts[index].Name.Equals(name, StringComparison.OrdinalIgnoreCase))
            return contacts[index];
        return FindContactRecursive(contacts, name, index + 1);
    }

    public void SearchContact(string name)
    {
        Contact contact = FindContactRecursive(contacts, name, 0);
        if (contact != null)
        {
            Console.WriteLine("Contact found:");
            Console.WriteLine($"Name: {contact.Name}");
            Console.WriteLine($"Email: {contact.Email}");
            Console.WriteLine($"Phone: {contact.Phone}");
        }
        else
        {
            Console.WriteLine("Contact not found.");
        }
    }

    private void UpdateContactRecursive(List<Contact> contacts, string name, int index)
    {
        if (index >= contacts.Count) return;
        if (contacts[index].Name.Equals(name, StringComparison.OrdinalIgnoreCase))
        {
            Console.Write("Enter new email (leave blank to keep existing): ");
            string newEmail = Console.ReadLine();
            if (!string.IsNullOrWhiteSpace(newEmail)) contacts[index].Email = newEmail;

            Console.Write("Enter new phone number (leave blank to keep existing): ");
            string newPhone = Console.ReadLine();
            if (!string.IsNullOrWhiteSpace(newPhone)) contacts[index].Phone = newPhone;

            Console.WriteLine("Contact updated successfully.");
        }
        else
        {
            UpdateContactRecursive(contacts, name, index + 1);
        }
    }

    public void UpdateContact(string name)
    {
        UpdateContactRecursive(contacts, name, 0);
    }
}

class Program
{
    static void Main(string[] args)
    {
        ContactBook contactBook = new ContactBook();
        bool exit = false;

        while (!exit)
        {
            Console.WriteLine();
            Console.WriteLine("1. Add a contact");
            Console.WriteLine("2. Search for a contact");
            Console.WriteLine("3. Update a contact");
            Console.WriteLine("4. Exit");

            Console.Write("Enter your choice: ");
            int choice = int.Parse(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    Console.Write("Enter name: ");
                    string name = Console.ReadLine();
                    Console.Write("Enter email: ");
                    string email = Console.ReadLine();
                    Console.Write("Enter phone number: ");
                    string phone = Console.ReadLine();

                    Contact contact = new Contact(name, email, phone);
                    contactBook.AddContact(contact);
                    break;
                case 2:
                    Console.Write("Enter name to search: ");
                    string searchName = Console.ReadLine();
                    contactBook.SearchContact(searchName);
                    break;
                case 3:
                    Console.Write("Enter name to update: ");
                    string updateName = Console.ReadLine();
                    contactBook.UpdateContact(updateName);
                    break;
                case 4:
                    exit = true;
                    break;
                default:
                    Console.WriteLine("Invalid choice. Try again.");
                    break;
            }
        }
    }
}
