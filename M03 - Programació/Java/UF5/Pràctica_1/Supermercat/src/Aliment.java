//Classe Aliment que hereta de Producte i que conté l'atribut calories i beguda
public class Aliment extends Producte {
    private int calories;
    private boolean beguda;
    //Constructor de la classe Aliment
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
    //Getter de l'atribut calories
    public int getCalories() {
        return calories;
    }
    //Setter de l'atribut calories que només accepta valors superiors o iguals a 0
    public void setCalories(int calories) throws Exception {
        if (calories < 0) {
            throw new Exception("Les calories no poden ser negatives");
        }
        this.calories = calories;
    }
    //Getter de l'atribut beguda
    public boolean esBeguda() {
        return beguda;
    }
    //Mètode que retorna el preu de venda al públic
    public double pvp() {
        if (beguda) {
            return super.pvp() * 1.21;
        } else {
            return super.pvp() * 1.10;
        }
    }
    //Mètode que retorna la informació de l'aliment
    public String getInfo() {
        return super.getInfo() + "\n Calories: " + calories + "\n Drink: " + beguda;
    }
    @Override
    public String toString() {
        return getInfo();
    }
}