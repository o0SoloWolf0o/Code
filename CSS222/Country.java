public class Country {
    private String name;
    private String capital;
    private int population;

    public Country(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCapital() {
        return capital;
    }

    public void setCapital(String capital) {
        this.capital = capital;
    }

    public int getPopulation() {
        return population;
    }

    public void setPopulation(int population) {
        this.population = population;
    }

    @Override
    public String toString() {
        return "Country [name=" + name + ", capital=" + capital + ", population=" + population + "]";
    }

    public static void main(String[] args){
        Country India = new Country("India");
        India.setCapital("New Delhi");
        India.setPopulation(1212312121);
        System.out.println(India);
    }
}
