//Class Cotxe
public abstract class Cotxe implements Autonomia{
    //Atributs
    private String matricula;
    private int preu;
    
    //Constructor
    public Cotxe(String matricula, int preu) throws Exception {
        //Si el preu es menor que 5000 o mes gran que 50000 
        if (preu < 5000 || preu > 50000) {
            //Llançem una excepcio
            throw new Exception("Preu no vàlid");
        }
        //Igualem els atributs
        this.matricula = matricula;
        this.preu = preu;
    }
    
    //Metodes getters
    public String getMatricula() {
        return matricula;
    }

    public int getPreu() {
        return preu;
    }
    
    //Metode abstracte per obtenir informacio
    public abstract String getInfo();
}
