//Classe Roba que hereta de Producte i que conté els atributs color i talla
public class Roba extends Producte {
    private String color;
    private char talla;

    //Constructor de la classe Roba
    public Roba(String nom, double preu, String color, char talla) throws Exception {
        super(nom, preu);
        if (color == null || color.isEmpty()) {
            throw new Exception("El color no pot ser null o buit");
        }
        if (talla != 'S' && talla != 'M' && talla != 'L') {
            throw new Exception("La talla ha de ser S, M o L");
        }
        this.color = color;
        this.talla = talla;
    }
    //Getter de l'atribut color
    public String getColor() {
        return color;
    }
    //Setter de l'atribut color que només accepta valors no nulls o buits
    public void setColor(String color) throws Exception {
        if (color == null || color.isEmpty()) {
            throw new Exception("El color no pot ser null o buit");
        }
        this.color = color;
    }
    //Getter de l'atribut talla
    public char getTalla() {
        return talla;
    }
    //Setter de l'atribut talla que només accepta els valors S, M o L
    public void setTalla(char talla) throws Exception {
        if (talla != 'S' && talla != 'M' && talla != 'L') {
            throw new Exception("La talla ha de ser S, M o L");
        }
        this.talla = talla;
    }

    //Mètode que retorna el preu de venda al públic
    public double pvp() {
        return super.pvp() * 1.21;
    }
    //Mètode que retorna la informació de la roba
    public String getInfo() {
        return super.getInfo() + "\n Color: " + color + "\n Talla: " + talla;
    }
    @Override
    public String toString() {
        return getInfo();
    }
}


