//to prove that interfaces as well as abstract classes can inherit using the strategy pattern

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

interface Strategy
{
    void execute();
}

class Prog58
{
    public static void main(String[] args)
    {
        C obj = new C();
        
        Strategy methA = obj::methA;
        Strategy methX = obj::methX;
        Strategy methY = obj::methY;
        
        methA.execute();
        methX.execute();
        methY.execute();
    }
}
