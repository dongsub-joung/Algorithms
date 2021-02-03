package test;

abstract class Animal
{
    String crying;
    int moving;

    Animal(){}
    abstract void cry();
    abstract void move();
}

class Cat extends Animal
{
    Cat(){}
    Cat(String crying, int moving)
    {
        this.crying= crying;
        this.moving= moving;
    }
    void cry()  { System.out.println(crying); }
    void move() { System.out.println(moving); }
}

class Dog extends Animal
{
    Dog(){}
    Dog(String crying, int moving)
    {
        this.crying= crying;
        this.moving= moving;
    }
    void cry()  { System.out.println(crying); }
    void move() { System.out.println(moving); }
}

public class ex_abstract {
    public static void main(String[] args) {
        Cat cat= new Cat("nay", 2);
        Dog dog= new Dog("mong",5);
        System.out.println("--------sound--------");
        cat.cry();
        dog.cry();

        System.out.println("--------move--------");
        cat.move();
        dog.move();
    }
}