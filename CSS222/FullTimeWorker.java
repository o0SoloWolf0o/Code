public class FullTimeWorker extends Worker{

    private int hours_Worked;
    private double salary_rate;

    FullTimeWorker(String name, double salary_rate, int hours_Worked){
        super(name, salary_rate);
        this.salary_rate = salary_rate;
        this.hours_Worked = hours_Worked;
    }

    @Override
    public double computePay() {
        if(hours_Worked > 240){
            return -1;
        } else {
            return salary_rate*hours_Worked;
        }
    }
    
}
