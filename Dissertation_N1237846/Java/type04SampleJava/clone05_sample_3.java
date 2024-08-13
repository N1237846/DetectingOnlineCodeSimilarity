//write a hello world program in java using nested classes
import java.lang.*;

class Prog01
{
    public static void main(String[] args)
    {
        Printer printer = new Printer();
        Printer.Message message = printer.new Message();
        message.print();
    }

    class Printer
    {
        class Message
        {
            void print()
            {
                System.out.println("Hello World!");
            }
        }
    }
}
