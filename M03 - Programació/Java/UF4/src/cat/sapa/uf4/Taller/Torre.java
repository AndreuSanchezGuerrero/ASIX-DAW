package cat.sapa.uf4.Taller;

public class Torre {
    private String marca;
    private String model;
    private int preu;
    private int capacitatDisc;
    private int capacitatRAM;
    private String CPU;
    
    public Torre(String marca, String model, int preu, int capacitatDisc, int capacitatRAM, String CPU) {
        this.marca = marca;
        this.model = model;
        this.preu = preu;
        this.capacitatDisc = 0;
        this.capacitatRAM = 0;
        this.CPU = CPU;
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

    public int getCapacitatDisc() {
        return capacitatDisc;
    }

    public int getCapacitatRAM() {
        return capacitatRAM;
    }

    public void setCapacitatDisc(int capacitatDisc) {
        this.capacitatDisc = capacitatDisc;
    }

    public void setCapacitatRAM(int capacitatRAM) {
        this.capacitatRAM = capacitatRAM;
    }

    public String getCPU() {
        return CPU;
    }

    @Override
    public String toString() {
        return "Torre: " + marca + " " + model + " " + preu + "€";
    }
}
