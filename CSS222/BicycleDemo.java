public class BicycleDemo {
    public static void main(String[] args) {
        Bicycle bike1 = new Bicycle();
        // Bicycle bike2 = new Bicycle();
        System.out.println(bike1);
        bike1.changeCadence(50);
        bike1.changespeed(10);
        bike1.changeGear(2);
        bike1.printGear();
        System.out.println(bike1);
        System.out.println(bike1);
    }
}