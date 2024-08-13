//write a hello world program in java using the strategy pattern
import java.lang.*;

class Prog01
{
    public static void main(String[] args)
    {
        MessagePrinter printer = new MessagePrinter(new SimpleMessageStrategy());
        printer.printMessage();
    }
}

interface MessageStrategy
{
    void print();
}

class SimpleMessageStrategy implements MessageStrategy
{
    public void print()
    {
        System.out.println("Hello World!");
    }
}

class MessagePrinter
{
    private final MessageStrategy strategy;

    public MessagePrinter(MessageStrategy strategy)
    {
        this.strategy = strategy;
    }

    public void printMessage()
    {
        strategy.print();
    }
}
