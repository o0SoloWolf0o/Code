public class TestWorker {
    public static void main(String[] args) {
        Worker w1 = new HourlyWorker("Por", 50, 40);
        // System.out.println(w1);
        if(w1.computePay() == -1){
            System.out.println("Error: Hours worked is greater than 60");
        } else {
            System.out.println("Pay: " + w1.computePay());
        }

        Worker w2 = new FullTimeWorker("Louis", 100, 40);
        // System.out.println(w2);
        if(w2.computePay() == -1){
            System.out.println("Error: Hours worked is greater than 250");
        } else {
            System.out.println("Pay: " + w2.computePay());
        }

        Worker w3 = new HourlyWorker("Ten", 50, 99999999);
        // System.out.println(w3);
        if(w3.computePay() == -1){
            System.out.println("Error: Hours worked is greater than 60 hour");
        } else {
            System.out.println("Pay: " + w3.computePay());
        }

        Worker w4 = new FullTimeWorker("Yayee", 100, 99999999);
        // System.out.println(w4);
        if(w4.computePay() == -1){
            System.out.println("Error: Hours worked is greater than 250 hour");
        } else {
            System.out.println("Pay: " + w4.computePay());
        }
    }
}
