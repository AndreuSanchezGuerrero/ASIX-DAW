//Classe Llibre que hereta de Producte i que conté l'atribut autor i tapaDura
public class Llibre extends Producte {
    private String autor;
    private boolean tapaDura;
    //Constructor de la classe Llibre
    public Llibre(String nom, double preu, String autor, boolean tapaDura) throws Exception {
        super(nom, preu);
        if (autor == null || autor.isEmpty()) {
            throw new Exception("L'autor no pot ser null o buit");
        }
        this.autor = autor;
        this.tapaDura = tapaDura;
    }
    //Getter de l'atribut autor
    public String getAutor() {
        return autor;
    }
    //Getter de l'atribut tapaDura
    public boolean isTapaDura() {
        return tapaDura;
    }
    //Setter de l'atribut tapaDura
    public void setTapaDura(boolean tapaDura) {
        this.tapaDura = tapaDura;
    }
    //Setter de l'atribut autor que només accepta valors no nulls o buits
    public void setAutor(String autor) throws Exception {
        if (autor == null || autor.isEmpty()) {
            throw new Exception("L'autor no pot ser null o buit");
        }
        this.autor = autor;
    }
    //Mètode que retorna la informació del llibre
    public String getInfo() {
        return super.getInfo() + "\n Autor: " + autor;
    }
    //Mètode que retorna el preu de venda al públic
    public double pvp() {
        return super.pvp() * 1.04;
    }
    @Override
    public String toString() {
        return getInfo();
    }
}