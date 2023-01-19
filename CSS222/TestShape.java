public class TestShape {
    public static void main(String[] args) {
        Shape s1 = new Triangle("red", 4, 5);
        System.out.println(s1);
        System.out.println("Area is " + s1.getArea()); 
        Shape s2 = new Rectangle("blue", 4, 5);
        System.out.println(s2);
        System.out.println("Area is " + s2.getArea());
    }
}
