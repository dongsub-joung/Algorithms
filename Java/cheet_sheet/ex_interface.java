package test;

interface Animal
{
    public abstract void cry();
    public abstract void reaction();
}
interface action
{
    public abstract void move();
}

class Cat implements Animal,action
{
    int age, move;
    Cat(){}
    Cat(int age, int move)
    {
        this.age= age;
        this.move= move;
    }
    public void cry()
    {
        System.out.println("냐");
    }
    public void reaction()
    {
        System.out.println("쥐 잡기 놀이");
    }
    public void move()
    {
        int range= (age%10) * move;
        System.out.println( range + "만큼 움직였다.");
    }
}

class Dog implements Animal,action
{
    int age, move;

    Dog(){}
    Dog(int age, int move)
    {
        this.age= age;
        this.move= move;
    }
    public void cry()
    {
        System.out.println("멍");
    }
    public void reaction()
    {
        System.out.println("산책");
    }
    public void move()
    {
        int range= (age%10) * move;
        System.out.println( range + "만큼 움직였다.");
    }
}

public class ex_interface {
    public static void main(String[] args) {
        Cat c= new Cat(4, 10);
        Dog d= new Dog(2, 5);

        c.cry();
        c.reaction();
        c.move();
        d.cry();
        d.reaction();
        d.move();
    }
}
