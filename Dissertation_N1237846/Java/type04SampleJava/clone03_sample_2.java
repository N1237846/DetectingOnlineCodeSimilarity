//to prove that interfaces as well as abstract classes can inherit using the builder pattern

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

class CBuilder
{
    private C instance;

    public CBuilder()
    {
        instance = new C();
    }

    public CBuilder withMethA()
    {
        instance.methA();
        return this;
    }

    public CBuilder withMethX()
    {
        instance.methX();
        return this;
    }

    public CBuilder withMethY()
    {
        instance.methY();
        return this;
    }

    public C build()
    {
        return instance;
    }
}

class Prog58
{
    public static void main(String[] args)
    {
        C obj = new CBuilder().withMethA().withMethX().withMethY().build();
    }
}
