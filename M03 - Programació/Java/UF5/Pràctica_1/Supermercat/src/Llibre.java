public class Llibre extends Producte {
    private String autor;
    public Llibre(String nom, double preu, String autor) throws Exception {
        super(nom, preu);
        if (autor == null || autor.isEmpty()) {
            throw new Exception("L'autor no pot ser null o buit");
        }
        this.autor = autor;
    }
    public String getAutor() {
        return autor;
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
    @Override
    public String toString() {
        return getInfo();
    }
}