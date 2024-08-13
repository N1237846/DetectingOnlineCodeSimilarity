//write a hello world program in java using command pattern
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
