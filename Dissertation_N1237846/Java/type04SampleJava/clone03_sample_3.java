//to prove that interfaces as well as abstract classes can inherit using nested classes

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

    static class NestedC
    {
        void execute(C obj)
        {
            obj.methA();
            obj.methX();
            obj.methY();
        }
    }
}

class Prog58
{
    public static void main(String[] args)
    {
        C obj = new C();
        C.NestedC nested = new C.NestedC();
        nested.execute(obj);
    }
}
