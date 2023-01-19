public class OperatorTest {
    public static void main(String[] args)
    {
        // Initial some variables
        int a = 9;
        int b = 9;
        // Arithmetic operators
        // addition
        int result_add = a+b;
        System.out.println("Addition : "+result_add);
        ++result_add;
        System.out.println("Increment Result of addition : "+result_add);
        // Modulus
        double result_mod = result_add%b;
        System.out.println("Modulus : "+result_mod);
        // Assignment and Bitwise
        a += 5;
        System.out.println("Result of variable a : "+a);
        // Example: 2 in binary is 10 , 1 in binary is 01
        // 10|01 = 11 = 3
        System.out.println("Result of 2|1 : "+ (2|1));
        // Comparison
        boolean compare_ab = (a == b);
        System.out.println("Compare a and b : "+compare_ab);
        // Logical
        boolean logical_ab = (a<5 && b>8);
        System.out.println("Logical a and b : "+logical_ab);
    }
}
