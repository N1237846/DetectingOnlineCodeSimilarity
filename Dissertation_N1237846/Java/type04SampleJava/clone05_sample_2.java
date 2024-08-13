//write a hello world program in java using the builder pattern
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
