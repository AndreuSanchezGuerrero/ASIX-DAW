package cat.sapa.uf4.Poligons;

public class Hexagon extends TriangleEquilater {
    public Hexagon(double costat) {
        super(costat);
        nCostats = 6;
    }

    public String toString() {
        return "Hexagon: " + costat + " " + calculaArea() + " " + calculaPerimetre();
    }
}
