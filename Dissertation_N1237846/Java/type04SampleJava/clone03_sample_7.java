//to prove that interfaces as well as abstract classes can inherit using reflection

import java.lang.reflect.Method;

interface X
{
    void methX();
}

interface Y extends X
{
    void methY();
}

abstract class A implements Y
{
    abstract void methA();
}

abstract class B extends A
{
    public void methY()
    {
        System.out.println("B's implementation of methY()");
    }
}

class C extends B
{
    public void methX()
    {
        System.out.println("C's implementation of methX()");
    }
    
    public void methA()
    {
        System.out.println("C's implementation of methA()");
    }
}

class Prog58
{
    public static void main(String[] args)
    {
        try
        {
            C obj = new C();
            
            Method methA = C.class.getMethod("methA");
            Method methX = C.class.getMethod("methX");
            Method methY = C.class.getMethod("methY");
            
            methA.invoke(obj);
            methX.invoke(obj);
            methY.invoke(obj);
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}
