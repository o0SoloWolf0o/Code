class Animal {
    public void speak() {
        System.out.println("Animal Speak !");
    }
}

class Dog extends Animal {
    public void speak() {
        bark();
    }

    public void bark() {
        System.out.println("Woof !");
    }
}

class Seal extends Animal {
    public void speak() {
        bark();
    }

    public void bark() {
        System.out.println("Arf !");
    }
}

class Bird extends Animal {
    public void speak() {
        bark();
    }

    public void bark() {
        System.out.println("Tweet !");
    }
}

class useanimal {
    public static void main(String[] args) {
        Animal a = new Animal();
        Animal d = new Dog();
        Animal s = new Seal();
        Animal b = new Bird();
        a.speak();
        d.speak();
        s.speak();
        b.speak();
    }
}
