public class Roba extends Producte {
    private String color;
    private char talla;

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
    public String getColor() {
        return color;
    }
    public void setColor(String color) throws Exception {
        if (color == null || color.isEmpty()) {
            throw new Exception("El color no pot ser null o buit");
        }
        this.color = color;
    }
    public char getTalla() {
        return talla;
    }
    public void setTalla(char talla) throws Exception {
        if (talla != 'S' && talla != 'M' && talla != 'L') {
            throw new Exception("La talla ha de ser S, M o L");
        }
        this.talla = talla;
    }
    public double pvp() {
        return super.pvp() * 1.21;
    }
    public String getInfo() {
        return super.getInfo() + "\n Color: " + color + "\n Talla: " + talla;
    }
    @Override
    public String toString() {
        return getInfo();
    }
}

