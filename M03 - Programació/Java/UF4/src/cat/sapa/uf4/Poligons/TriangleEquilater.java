package cat.sapa.uf4.Poligons;
/*Triangle equilàter

Crea la subclasse TriangleEquilater que tingui un constructor només amb la mida de la base.

Ha de calcular l'altura amb la fórmula:

altura = base * Math.sin(Math.PI / 3)

Ha de tenir sobreescrits els mètodes per calcular l'àrea i el perímetre.

Ha de sobreescriure el mètode toString() per mostrar totes les dades. */
public class TriangleEquilater extends PoligonRegular {
    public TriangleEquilater(double base) {
        super("Triangle Equilater");
        costat = base;
        nCostats = 3;
    }
    private double calculaArea() {
        return (costat * costat * Math.sin(Math.PI / 3)) / 2;
    }
    }
    private String toString() {
        return "Triangle Equilater: " + costat + " " + calculaArea() + " " + calculaPerimetre();
    }
}
