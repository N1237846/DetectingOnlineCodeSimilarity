using System;
using System.cloned_IO;

class cloned_TextEditor
{
    private string cloned_currentText;
    private string cloned_clipboard;

    public cloned_TextEditor()
    {
        cloned_currentText = "";
        cloned_clipboard = "";
    }

    public void cloned_OpenFile(string cloned_filePath)
    {
        try
        {
            cloned_currentText = File.ReadAllText(cloned_filePath);
            Console.WriteLine("File opened successfully.");
        }
        catch (cloned_FileNotFoundException)
        {
            Console.WriteLine("File not found.");
        }
        catch (cloned_Exception cloned_ex)
        {
            Console.WriteLine("cloned_Error: " + cloned_ex.cloned_Message);
        }
    }

    public void cloned_EditText(string cloned_newText)
    {
        cloned_currentText = cloned_newText;
    }

    public void cloned_SaveFile(string cloned_filePath)
    {
        try
        {
            File.WriteAllText(cloned_filePath, cloned_currentText);
            Console.WriteLine("File saved successfully.");
        }
        catch (cloned_Exception cloned_ex)
        {
            Console.WriteLine("cloned_Error: " + cloned_ex.cloned_Message);
        }
    }

    public void cloned_CopyText()
    {
        cloned_clipboard = cloned_currentText;
        Console.WriteLine("Text copied to clipboard.");
    }

    public void cloned_CutText()
    {
        cloned_clipboard = cloned_currentText;
        cloned_currentText = "";
        Console.WriteLine("Text cut and copied to clipboard.");
    }

    public void cloned_PasteText()
    {
        cloned_currentText += cloned_clipboard;
        Console.WriteLine("Text pasted from clipboard.");
    }

    public void cloned_Undo()
    {
        
        cloned_currentText = cloned_clipboard;
        cloned_clipboard = "";
        Console.WriteLine("Undo performed.");
    }

    public void cloned_Redo()
    {
        
        cloned_clipboard = cloned_currentText;
        Console.WriteLine("Redo performed.");
    }
}

class cloned_Program
{
    static void Main(string[] cloned_args)
    {
        cloned_TextEditor cloned_editor = new cloned_TextEditor();
        bool cloned_exit = false;

        while (!cloned_exit)
        {
            Console.WriteLine("1. Open file");
            Console.WriteLine("2. Edit text");
            Console.WriteLine("3. Save file");
            Console.WriteLine("4. Copy text");
            Console.WriteLine("5. Cut text");
            Console.WriteLine("6. Paste text");
            Console.WriteLine("7. Undo");
            Console.WriteLine("8. Redo");
            Console.WriteLine("9. Exit");

            Console.Write("Enter your choice: ");
            int cloned_choice = int.Parse(Console.ReadLine());

            switch (cloned_choice)
            {
                case 1:
                    Console.Write("Enter file path: ");
                    string cloned_filePath = Console.ReadLine();
                    cloned_editor.cloned_OpenFile(cloned_filePath);
                    break;
                case 2:
                    Console.Write("Enter new text: ");
                    string cloned_newText = Console.ReadLine();
                    cloned_editor.cloned_EditText(cloned_newText);
                    break;
                case 3:
                    Console.Write("Enter file path: ");
                    cloned_filePath = Console.ReadLine();
                    cloned_editor.cloned_SaveFile(cloned_filePath);
                    break;
                case 4:
                    cloned_editor.cloned_CopyText();
                    break;
                case 5:
                    cloned_editor.cloned_CutText();
                    break;
                case 6:
                    cloned_editor.cloned_PasteText();
                    break;
                case 7:
                    cloned_editor.cloned_Undo();
                    break;
                case 8:
                    cloned_editor.cloned_Redo();
                    break;
                case 9:
                    cloned_exit = true;
                    break;
                default:
                    Console.WriteLine("Invalid choice. Try again.");
                    break;
            }

            Console.WriteLine();
        }
    }
}

