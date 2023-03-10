public class Llibre extends Producte {
    private String autor;
    private boolean tapaDura;
    public Llibre(String nom, double preu, String autor, boolean tapaDura) throws Exception {
        super(nom, preu);
        if (autor == null || autor.isEmpty()) {
            throw new Exception("L'autor no pot ser null o buit");
        }
        this.autor = autor;
        this.tapaDura = tapaDura;
    }
    public String getAutor() {
        return autor;
    }

    public boolean isTapaDura() {
        return tapaDura;
    }
    public void setTapaDura(boolean tapaDura) {
        this.tapaDura = tapaDura;
    }
    
    public void setAutor(String autor) throws Exception {
        if (autor == null || autor.isEmpty()) {
            throw new Exception("L'autor no pot ser null o buit");
        }
        this.autor = autor;
    }
    public String getInfo() {
        return super.getInfo() + "\n Autor: " + autor;
    }

    public double pvp() {
        return super.pvp() * 1.04;
    }

    @Override
    public String toString() {
        return getInfo();
    }
}