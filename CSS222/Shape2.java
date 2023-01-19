abstract public class Shape2{
    private String color;
    public Shape2(String color){
        this.color = color;
    }
    @Override
    public String toString(){
        return "Shape of color=\"" + color + "\"";
    }
    public double getArea(){
        System.err.println("Shape unknown! Cannot compute area!");
        return 0;
    }
}