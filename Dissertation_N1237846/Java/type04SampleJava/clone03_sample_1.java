//to prove that interfaces as well as abstract classes can inherit using method references

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
        C obj = new C();
        Prog58.execute(obj::methA, obj::methX, obj::methY);
    }
    
    static void execute(Runnable... methods)
    {
        for (Runnable method : methods)
        {
            method.run();
        }
    }
}
