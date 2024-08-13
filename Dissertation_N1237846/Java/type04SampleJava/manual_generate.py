# Define the 10 Type IV clone samples as strings
clone_samples = [
    '''//write a hello world program in java using method references
import java.lang.*;

class Prog01
{
    public static void main(String[] args)
    {
        Prog01 program = new Prog01();
        program.execute(Prog01::printMessage);
    }

    void execute(Runnable method)
    {
        method.run();
    }

    static void printMessage()
    {
        System.out.println("Hello World!");
    }
}
''',

    '''//write a hello world program in java using the builder pattern
import java.lang.*;

class Prog01
{
    public static void main(String[] args)
    {
        MessageBuilder builder = new MessageBuilder();
        builder.withMessage("Hello World!")
               .build()
               .print();
    }
}

class MessageBuilder
{
    private String message;

    public MessageBuilder withMessage(String message)
    {
        this.message = message;
        return this;
    }

    public Message build()
    {
        return new Message(message);
    }
}

class Message
{
    private final String message;

    public Message(String message)
    {
        this.message = message;
    }

    public void print()
    {
        System.out.println(message);
    }
}
''',

    '''//write a hello world program in java using nested classes
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
''',

    '''//write a hello world program in java using the strategy pattern
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
''',

    '''//write a hello world program in java using an array of Runnable
import java.lang.*;

class Prog01
{
    public static void main(String[] args)
    {
        Runnable[] tasks = {
            () -> System.out.println("Hello World!")
        };

        for (Runnable task : tasks)
        {
            task.run();
        }
    }
}
''',

    '''//write a hello world program in java using static methods
import java.lang.*;

class Prog01
{
    public static void main(String[] args)
    {
        Prog01.printMessage();
    }

    static void printMessage()
    {
        System.out.println("Hello World!");
    }
}
''',

    '''//write a hello world program in java using reflection for method invocation
import java.lang.*;
import java.lang.reflect.Method;

class Prog01
{
    public static void main(String[] args)
    {
        try
        {
            Method method = Prog01.class.getDeclaredMethod("printMessage");
            method.invoke(null);
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }

    static void printMessage()
    {
        System.out.println("Hello World!");
    }
}
''',

    '''//write a hello world program in java using lambda expressions
import java.lang.*;

class Prog01
{
    public static void main(String[] args)
    {
        Runnable task = () -> System.out.println("Hello World!");
        task.run();
    }
}
''',

    '''//write a hello world program in java using command pattern
import java.lang.*;

class Prog01
{
    public static void main(String[] args)
    {
        Command command = new PrintMessageCommand();
        Invoker invoker = new Invoker(command);
        invoker.execute();
    }
}

interface Command
{
    void execute();
}

class PrintMessageCommand implements Command
{
    public void execute()
    {
        System.out.println("Hello World!");
    }
}

class Invoker
{
    private final Command command;

    public Invoker(Command command)
    {
        this.command = command;
    }

    public void execute()
    {
        command.execute();
    }
}
''',

    '''//write a hello world program in java using decorator pattern
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
'''
]

# Generate 10 Java files with the clone samples
def generate_clone_files():
    for i, sample in enumerate(clone_samples, start=1):
        filename = f"clone05_sample_{i}.java"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(sample)

if __name__ == "__main__":
    generate_clone_files()
    print("10 Java clone files have been created.")
