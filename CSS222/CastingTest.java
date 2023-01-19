public class CastingTest {
    public static void main(String[] args)
    {
        //Widening Casting
        int a = 9;
        // convert int to double
        double b = a;
        //Narrowing Casting
        double c = 9.8;
        // convert double to int
        int d = (int)c;
        // print
        System.out.println("int : "+a);
        System.out.println("After convert to double : "+b);
        System.out.println("double : "+c);
        System.out.println("After convert to int : "+d);
    }
}
