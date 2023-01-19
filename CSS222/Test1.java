public class Test1 {
    public static void main(String[] args) {
        Employee emp1 = new Employee("Por", 12000);
        Employee emp2 = new Employee("Louis", 15000);
        Manager mng1 = new Manager("Yayee", 24000, "DEV");
        System.out.println(emp1);
        System.out.println(emp2);
        System.out.println(mng1);
    }
    
}