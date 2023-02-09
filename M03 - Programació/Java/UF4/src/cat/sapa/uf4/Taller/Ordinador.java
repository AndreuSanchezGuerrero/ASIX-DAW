package cat.sapa.uf4.Taller;

public class Ordinador {
    private int preu;
    private Monitor monitor;
    private Teclat teclat;
    private Ratoli ratoli;
    private Torre torre;
    
    public Ordinador(){}
    public Ordinador(int preu, Monitor monitor, Teclat teclat, Ratoli ratoli, Torre torre) {
        this.preu = preu;
        this.monitor = monitor;
        this.teclat = teclat;
        this.ratoli = ratoli;
        this.torre = torre;
    }

    public int getPreu() {
        return preu;
    }

    public Monitor getMonitor() {
        return monitor;
    }

    public Teclat getTeclat() {
        return teclat;
    }

    public Ratoli getRatoli() {
        return ratoli;
    }

    public Torre getTorre() {
        return torre;
    }

    public void setPreu(int preu) {
        this.preu = preu;
    }

    public void setMonitor(Monitor monitor) {
        this.monitor = monitor;
    }

    public void setTeclat(Teclat teclat) {
        this.teclat = teclat;
    }

    public void setRatoli(Ratoli ratoli) {
        this.ratoli = ratoli;
    }

    public void setTorre(Torre torre) {
        this.torre = torre;
    }

    @Override
    public String toString() {
        return "Ordinador: " + preu + "€\n" + monitor + "\n" + teclat + "\n" + ratoli + "\n" + torre;
    }

}