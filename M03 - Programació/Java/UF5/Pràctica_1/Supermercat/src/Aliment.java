public class Aliment extends Producte {
    private int calories;
    private boolean beguda;
    public Aliment(String nom, double preu, int calories, boolean beguda) throws Exception {
        super(nom, preu);
        if (calories < 0) {
            throw new Exception("Les calories no poden ser negatives");
        }
        if (calories > 1000) {
            throw new Exception("Les calories no poden ser superiors a 1000");
        }
        this.calories = calories;
        this.beguda = beguda;
    }
    public int getCalories() {
        return calories;
    }
    public void setCalories(int calories) throws Exception {
        if (calories < 0) {
            throw new Exception("Les calories no poden ser negatives");
        }
        this.calories = calories;
    }
    public boolean esBeguda() {
        return beguda;
    }
    public double pvp() {
        if (beguda) {
            return super.pvp() * 1.21;
        } else {
            return super.pvp() * 1.10;
        }
    }
    public String getInfo() {
        return super.getInfo() + "\n Calories: " + calories + "\n Drink: " + beguda;
    }
    @Override
    public String toString() {
        return getInfo();
    }
}