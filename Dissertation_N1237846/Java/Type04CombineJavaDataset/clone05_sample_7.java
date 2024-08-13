//write a hello world program in java using reflection for method invocation
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
