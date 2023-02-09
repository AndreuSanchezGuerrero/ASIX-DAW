package cat.sapa.uf4.Poligons;
/*Quadrat

Crea la subclasse Quadrat que tingui un constructor només amb la mida de la base.

Ha de tenir sobreescrits els mètodes per calcular l'àrea i el perímetre.

Ha de sobreescriure el mètode toString() per mostrar totes les dades. */

public class Quadrat extends PoligonRegular {
    public Quadrat(double base) {
        super("Quadrat");
        costat = base;
        nCostats = 4;
    }
    private double calculaArea() {
        return (costat * costat);
    }

    private String toString() {
        return "Quadrat: " + costat + " " + calculaArea() + " " + calculaPerimetre();
    }
}