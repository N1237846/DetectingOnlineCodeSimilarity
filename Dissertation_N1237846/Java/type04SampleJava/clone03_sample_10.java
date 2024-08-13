//to prove that interfaces as well as abstract classes can inherit using decorator pattern

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

class Decorator implements Y
{
    protected C wrapped;

    public Decorator(C wrapped)
    {
        this.wrapped = wrapped;
    }

    public void methX()
    {
        wrapped.methX();
    }

    public void methY()
    {
        wrapped.methY();
    }
}

class ConcreteDecoratorA extends Decorator
{
    public ConcreteDecoratorA(C wrapped)
    {
        super(wrapped);
    }

    public void methA()
    {
        wrapped.methA();
    }
}

class Prog58
{
    public static void main(String[] args)
    {
        C obj = new C();
        ConcreteDecoratorA decorator = new ConcreteDecoratorA(obj);
        decorator.methA();
        decorator.methX();
        decorator.methY();
    }
}
