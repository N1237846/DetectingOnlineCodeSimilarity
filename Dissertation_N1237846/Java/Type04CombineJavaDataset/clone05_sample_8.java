//write a hello world program in java using lambda expressions
import java.lang.*;

class Prog01
{
    public static void main(String[] args)
    {
        Runnable task = () -> System.out.println("Hello World!");
        task.run();
    }
}
