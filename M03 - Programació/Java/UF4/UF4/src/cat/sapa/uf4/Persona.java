package cat.sapa.uf4;

public class Persona {
    // Atributs privats de l'objecte (no són estàtics)
    String nom;
    int edat;

    // Constructor
    public Persona(String _nom, int _edat) {
        nom = _nom;
        edat = _edat;
    }

    // Mètode públic de l'objecte (no és estàtic)
    public void mostrarDadesPersona() {
        System.out.println("Nom: " + nom);
        System.out.println("Edat: " + edat);
    }
}
