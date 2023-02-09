package cat.sapa.uf4.Poligons;

/*5 - Polígons regulars

Crea la classe PoligonRegular que tingui un constructor amb els atributs nom, radi i costats.
També ha de tenir un constructor només amb el nom.

Ha de tenir un mètode privat per calcular la mida de cada costat i l'apotema:

double angle = 2 * Math.PI / nCostats;
double base = radi - radi * Math.cos(angle);
double altura = radi * Math.sin(angle);
costat = Math.sqrt(base * base + altura * altura);
apotema = Math.sqrt(radi * radi - costat * costat / 4);

Ha de tenir un mètode per calcular l'àrea i un per calcular el perímetre:

area = (nCostats * costat * apotema) / 2
perimetre = nCostats * costat

Ha de sobreescriure el mètode toString() per mostrar totes les dades.

També ha de sobreescriure el mètode equals(Object o) per comprovar si dos polígons són iguals.
La condició d'igualtat serà que el nom sigui igual o que el perímetre o l'àrea siguin similars amb un marge d'error de 0.1.
Quadrat

Crea la subclasse Quadrat que tingui un constructor només amb la mida de la base.

Ha de tenir sobreescrits els mètodes per calcular l'àrea i el perímetre.

Ha de sobreescriure el mètode toString() per mostrar totes les dades.
Triangle equilàter

Crea la subclasse TriangleEquilater que tingui un constructor només amb la mida de la base.

Ha de calcular l'altura amb la fórmula:

altura = base * Math.sin(Math.PI / 3)

Ha de tenir sobreescrits els mètodes per calcular l'àrea i el perímetre.

Ha de sobreescriure el mètode toString() per mostrar totes les dades.
Hexagon

Aquesta classe ha de ser subclasse de TriangleEquilater.

Se li ha de passar la mida del costat al constructor.

L'àrea serà 6 vegades la del triangle que tingui la mateixa base.

El perímetre serà el doble que el del triangle amb la mateixa base.

Utilitza els mètodes de la classe TriangleEquilater per fer aquests càlculs.
Proves

Crea la classe TestPoligonRegular per fer les proves.

Utilitza només variables de tipus PoligonRegular. */
public class PoligonRegular {
    private String nom;
    private double radi;
    protected int nCostats;
    protected double costat;
    private double apotema;
    private double area;
    private double perimetre;
    
    public PoligonRegular(String nom, double radi, int nCostats) {
        this.nom = nom;
        this.radi = radi;
        this.nCostats = nCostats;
        this.costat = calculaCostat();
        this.apotema = calculaApotema();
        this.area = calculaArea();
        this.perimetre = calculaPerimetre();
    }
    
    public PoligonRegular(String nom) {
        this.nom = nom;
    }
    
    private double calculaCostat() {
        double angle = 2 * Math.PI / nCostats;
        double base = radi - radi * Math.cos(angle);
        double altura = radi * Math.sin(angle);
        return Math.sqrt(base * base + altura * altura);
    }
    
    private double calculaApotema() {
        return Math.sqrt(radi * radi - costat * costat / 4);
    }
    
    private double calculaArea() {
        return (nCostats * costat * apotema) / 2;
    }
    
    protected double calculaPerimetre() {
        return nCostats * costat;
    }
    
    @Override
    public String toString() {
        return "PoligonRegular{" + "nom=" + nom + ", radi=" + radi + ", nCostats=" + nCostats + ", costat=" + costat + ", apotema=" + apotema + ", area=" + area + ", perimetre=" + perimetre + '}';
    }
    
    @Override
    public boolean equals(Object o) {
        if (o instanceof PoligonRegular) {
            PoligonRegular p = (PoligonRegular) o;
            if (nom.equals(p.nom)) {
                return true;
            } else if (Math.abs(perimetre - p.perimetre) < 0.1) {
                return true;
            } else if (Math.abs(area - p.area) < 0.1) {
                return true;
            }
        }
        return false;
    }
}


