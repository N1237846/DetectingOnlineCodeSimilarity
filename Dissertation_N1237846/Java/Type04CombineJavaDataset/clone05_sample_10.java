//write a hello world program in java using decorator pattern
import java.lang.*;

class Prog01
{
    public static void main(String[] args)
    {
        MessageComponent component = new ConcreteMessageComponent();
        MessageDecorator decorator = new MessageDecorator(component);
        decorator.print();
    }
}

interface MessageComponent
{
    void print();
}

class ConcreteMessageComponent implements MessageComponent
{
    public void print()
    {
        System.out.println("Hello World!");
    }
}

class MessageDecorator implements MessageComponent
{
    private final MessageComponent wrapped;

    public MessageDecorator(MessageComponent wrapped)
    {
        this.wrapped = wrapped;
    }

    public void print()
    {
        wrapped.print();
    }
}
