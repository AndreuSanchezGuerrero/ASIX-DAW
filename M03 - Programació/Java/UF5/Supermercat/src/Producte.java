public class Producte {
    private String nom;
    private double preu;
    public Producte(String nom, double preu) throws Exception {
        if (nom == null || nom.isEmpty()) {
            throw new Exception("El nom no pot ser null o buit");
        }
        if (preu < 0) {
            throw new Exception("El preu no pot ser negatiu");
        }
        this.nom = nom;
        this.preu = preu;
    }
    public String getNom() {
        return nom;
    }
    public void setNom(String nom) throws Exception {
        if (nom == null || nom.isEmpty()) {
            throw new Exception("El nom no pot ser null o buit");
        }
        this.nom = nom;
    }
    public double getPreu() {
        return preu;
    }
    public void setPreu(double preu) throws Exception {
        if (preu < 0) {
            throw new Exception("El preu no pot ser negatiu");
        }
        this.preu = preu;
    }
    public double pvp() {
        return preu;
    }
    public String getInfo() {
        return "\nNom: " + nom + "\n Preu: " + preu;
    }
    @Override
    public String toString() {
        return getInfo();
    }
}
