public class TestMovable {
    // public static void main(String[] args) {
    //     Movable m1 = new MovablePoint(5, 5); // upcast
    //     System.out.println(m1);
    //     m1.moveLeft();
    //     System.out.println(m1);
    //     m1.moveRight();
    //     System.out.println(m1);
    //     m1.moveUp();
    //     System.out.println(m1);
    //     m1.moveDown();
    //     System.out.println(m1);
    // }
    public static void main(String[] args) {
        Movable m2 = new MovableCircle(5, 6, 10, 4, 20); // upcast
        System.out.println(m2);
        m2.moveLeft();
        System.out.println(m2);
        m2.moveRight();
        System.out.println(m2);
        m2.moveUp();
        System.out.println(m2);
        m2.moveDown();
        System.out.println(m2);
    }
}