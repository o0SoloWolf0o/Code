public class HourlyWorker extends Worker {
    private int hours_Worked;
    HourlyWorker(String name, double salary_rate, int hours_Worked){
        super(name, salary_rate);
        this.hours_Worked = hours_Worked;
    }    
    @Override
    public double computePay() {
        return 50*hours_Worked;
    }
}
