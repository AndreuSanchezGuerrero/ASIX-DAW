//Class CotxeElectric
public class CotxeElectric extends Cotxe implements Autonomia {
    //Atributs
    private float capacitat;
    //Constructor
    public CotxeElectric(String matricula, int preu, int capacitat) throws Exception {
        //Cridem al constructor de la classe pare
        super(matricula, preu);
        //Si la capacitat es menor que 0 llancem una excepcio
        if (capacitat < 0) {
            throw new Exception("La capacitat de la bateria no pot ser negativa");
        }
        //Igualem els atributs
        this.capacitat = capacitat;
    }
    //Metode per obtenir l'autonomia
    public float getAutonomia() {
        return this.capacitat * 10;
    }
    //Metode per obtenir informacio del cotxe
    public String getInfo() {
        return "Matrícula: " + this.getMatricula() + "\n  Preu: " + this.getPreu() + " €\n  Capacitat: " + this.capacitat + " kwh\n  Autonomia:  " + this.getAutonomia() + " km\n";
    }
}
