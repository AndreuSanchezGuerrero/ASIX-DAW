package cat.sapa.uf4.Taller;

public class Ratoli {
    private String marca;
    private String model;
    private int preu;
    private int numBotoes;
    
    public Ratoli(String marca, String model, int preu, int numBotoes) {
        this.marca = marca;
        this.model = model;
        this.preu = preu;
        this.numBotoes = numBotoes;
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
    
    public int getNumBotoes() {
        return numBotoes;
    }
    
    @Override
    public String toString() {
        return "Ratoli: " + marca + " " + model + " " + preu + "€ " + numBotoes + " botons";
    }
}
