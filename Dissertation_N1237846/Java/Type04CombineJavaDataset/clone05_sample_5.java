//write a hello world program in java using an array of Runnable
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
