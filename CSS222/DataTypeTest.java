public class DataTypeTest
{
    public static void main(String[] args)
    {
        // Byte (-128 to 127)
        byte a = 127;
        // Short (-32768 to 32767)
        short b = 32767;
        // Integer (-2147483648 to 2147483647)
        int c = 2147483647;
        // Long (-9223372036854775808 to 9223372036854775807)
        long d = 9223372036854775807L;
        // Float (3.4E-038 to 3.4E+038)
        float e = 3.4f;
        // Double (1.7E-308 to 1.7E+308)
        double f = 1.7d;
        // Boolean (true or false)
        boolean isJavaFun = true;
        // Char
        char g = 'Z';
        // String
        String h = "Run..........";
        // Print
        System.out.println("Byte : "+a);
        System.out.println("Short : "+b);
        System.out.println("Integer : "+c);
        System.out.println("Long : "+d);
        System.out.println("Float : "+e);
        System.out.println("Double : "+f);
        System.out.println("Boolean : "+isJavaFun);
        System.out.println("Char : "+g);
        System.out.println("String : "+h);
    }
}