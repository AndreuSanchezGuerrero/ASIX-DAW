package cat.sapa.uf4.Taller;

public class Monitor {
    private String marca;
    private String model;
    private int polzades;
    private int hz;
    private int amplada;
    private int alcada;
    private int preu;
    
    public Monitor(String marca, String model, int preu, int polzades, int hz, int amplada, int alcada) {
        this.marca = marca;
        this.model = model;
        this.polzades = polzades;
        this.hz = hz;
        this.amplada = amplada;
        this.alcada = alcada;
        this.preu = preu;
    }
    
    public int getPreu() {
        return preu;
    }
    
    public String getMarca() {
        return marca;
    }
    
    public String getModel() {
        return model;
    }
    
    public int getPolzades() {
        return polzades;
    }
    
    public int getHz() {
        return hz;
    }
    
    public int getAmplada() {
        return amplada;
    }
    
    public int getAlcada() {
        return alcada;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public void setPreu(int preu) {
        this.preu = preu;
    }
    
    public void setPolzades(int polzades) {
        this.polzades = polzades;
    }

    public void setHz(int hz) {
        this.hz = hz;
    }

    public void setAmplada(int amplada) {
        this.amplada = amplada;
    }

    public void setAlcada(int alcada) {
        this.alcada = alcada;
    }

    @Override
    public String toString() {
        return "Monitor: " + marca + " " + model + " " + polzades + " polzades " + hz + " Hz " + amplada + "x" + alcada;
    }
}
