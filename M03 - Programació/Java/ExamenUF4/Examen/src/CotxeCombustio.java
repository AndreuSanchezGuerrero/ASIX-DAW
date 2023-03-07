//Class CotxeCombustio
public class CotxeCombustio extends Cotxe implements Autonomia {
    //Atributs
    private int capacitatDiposit;
    private double consum100;
    
    //Constructor
    public CotxeCombustio(String matricula, int preu, int capacitat, double consum) throws Exception {
        //Cridem al constructor de la classe pare
        super(matricula, preu);
        //Igualem els atributs
        this.capacitatDiposit = capacitat;
        this.consum100 = consum;
    }
    
    //Metode per obtenir l'autonomia 
    public float getAutonomia() {
        return (int) (capacitatDiposit * 100 / consum100);
    }
    
    //Metode per obtenir informacio del cotxe
    public String getInfo() {
        return "Matrícula: " + getMatricula() + "\n  Preu: " + getPreu() + " €\n  Capacitat: " + capacitatDiposit + "\n  Consum: " + consum100 + "\n  Autonomia: " + getAutonomia() + " km\n";
    }
}