//write a hello world program in java using method references
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
