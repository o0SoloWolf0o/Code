class StaticOuter {
    String a = "Static Outer String";
    static String b = "Static Outer Static String";
    void seeStaticInner(){
        // 1
        // System.out.println(nonstatic);
        // 2
        // System.out.println(StaticInner.nonstatic);
        System.out.println(new StaticInner().nonstatic);
        System.out.println(StaticInner.s);
    }
    public static void main(String[] args){
        // 3
        // System.out.println(s);
        System.out.println(StaticInner.s);
        StaticOuter so = new StaticOuter();
        so.seeStaticInner();
    }
    static class StaticInner{
        String nonstatic = "StaticInner Nonstatic String";
        static String s = "StaticInner Static String";
        public static void main(String[] args){
            // 4
            // System.out.println(nonstatic);
            System.out.println(s);
            System.out.println(b);
        }
    }
}
class SomeOther{
    public static void main(String[] args){
        System.out.println(StaticOuter.StaticInner.s);
        StaticOuter.StaticInner si = new StaticOuter.StaticInner();
        System.out.println(si.nonstatic);
        // System.out.println(si.s);
    }
}