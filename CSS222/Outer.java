class Outer{
    Inner i1 = new Inner();
    private String s = "Outer string";
    void getS(){
        System.out.println(s);
    }
    void getInnerS(){
        System.out.println(i1.s);
    }
    class Inner{
        private String s = "Inner string";
        void getS(){
            System.out.println(s);
        }
        void getOuterS(){
            System.out.println(Outer.this.s);
        }
    }
    public static void main(String[] args){
        Outer o = new Outer();
        o.getS();
        o.getInnerS();
        Outer.Inner oi = new Outer(). new Inner();
        oi.getOuterS();
        oi.getS();
    }
}