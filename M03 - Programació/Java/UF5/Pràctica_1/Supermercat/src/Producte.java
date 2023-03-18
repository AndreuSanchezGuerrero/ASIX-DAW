//Classe Producte que conté els atributs nom i preu
public class Producte {
    private String nom;
    private double preu;

    //Constructor de la classe Producte
    public Producte(String nom, double preu) throws Exception {
        if (nom == null || nom.isEmpty()) {
            throw new Exception("El nom no pot ser null o buit");
        }
        if (preu < 1) {
            throw new Exception("El preu no pot ser inferior a 1");
        }
        this.nom = nom;
        this.preu = preu;
    }
    //Getter de l'atribut nom
    public String getNom() {
        return nom;
    }
    //Setter de l'atribut nom que només accepta valors no nulls o buits
    public void setNom(String nom) throws Exception {
        if (nom == null || nom.isEmpty()) {
            throw new Exception("El nom no pot ser null o buit");
        }
        this.nom = nom;
    }
    //Getter de l'atribut preu
    public double getPreu() {
        return preu;
    }
    //Setter de l'atribut preu que només accepta valors superiors o iguals a 1
    public void setPreu(double preu) throws Exception {
        if (preu < 0) {
            throw new Exception("El preu no pot ser inferior a 1");
        }
        this.preu = preu;
    }
    //Mètode que retorna el preu de venda al públic
    public double pvp() {
        return preu;
    }
    //Mètode que retorna la informació del producte
    public String getInfo() {
        return "\nNom: " + nom + "\n Preu: " + preu;
    }
    @Override
    public String toString() {
        return getInfo();
    }
}