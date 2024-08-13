//to prove that interfaces as well as abstract classes can inherit using command pattern

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

interface Command
{
    void execute();
}

class MethACommand implements Command
{
    private C receiver;

    public MethACommand(C receiver)
    {
        this.receiver = receiver;
    }

    @Override
    public void execute()
    {
        receiver.methA();
    }
}

class MethXCommand implements Command
{
    private C receiver;

    public MethXCommand(C receiver)
    {
        this.receiver = receiver;
    }

    @Override
    public void execute()
    {
        receiver.methX();
    }
}

class MethYCommand implements Command
{
    private C receiver;

    public MethYCommand(C receiver)
    {
        this.receiver = receiver;
    }

    @Override
    public void execute()
    {
        receiver.methY();
    }
}

class Prog58
{
    public static void main(String[] args)
    {
        C obj = new C();
        Command methA = new MethACommand(obj);
        Command methX = new MethXCommand(obj);
        Command methY = new MethYCommand(obj);
        
        methA.execute();
        methX.execute();
        methY.execute();
    }
}
