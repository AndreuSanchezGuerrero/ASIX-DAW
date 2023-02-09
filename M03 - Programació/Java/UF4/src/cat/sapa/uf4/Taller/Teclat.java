package cat.sapa.uf4.Taller;

public class Teclat {
    private String marca;
    private String model;
    private int preu;
    private String tipus;
    
    public Teclat(String marca, String model, int preu, String tipus) {
        this.marca = marca;
        this.model = model;
        this.preu = preu;
        this.tipus = tipus;
    }
    
    public String getMarca() {
        return marca;
    }
    
    public String getModel() {
        return model;
    }
    
    public int getPreu() {
        return preu;
    }
    
    public String gettipus() {
        return tipus;
    }
    
    @Override
    public String toString() {
        return "Teclat: " + marca + " " + model + " " + preu + "€ " + tipus + " tecles";
    }
}
