//Change all the code to use ArrayLists instead of arrays.

import java.util.ArrayList;

public class Supermercat {
    private ArrayList<Producte> llistaProductes;
    public Supermercat() {
        llistaProductes = new ArrayList<Producte>();
    }
    public void afegirProducte(Producte p) {
        llistaProductes.add(p);
    }
    public void eliminarProducte(String n) {
        for (int i = 0; i < llistaProductes.size(); i++) {
            if (llistaProductes.get(i).getNom().equals(n)) {
                llistaProductes.remove(i);
            }
        }
    }
    public ArrayList<Producte> filtrarProductes(String tipus) {
        ArrayList<Producte> aux = new ArrayList<Producte>();
        for (int i = 0; i < llistaProductes.size(); i++) {
            if (llistaProductes.get(i).getClass().getSimpleName().equals(tipus)) {
                aux.add(llistaProductes.get(i));
            }
        }
        return aux;
    }
    public void mostrarLlista(ArrayList<Producte> l) {
        for (int i = 0; i < l.size(); i++) {
            System.out.println(l.get(i));
        }
    }

    //comapreto per preu(a:producte,b:producte):int
    public int compararPreus(Producte a, Producte b) {
        if (a.getPreu() > b.getPreu()) {
            return 1;
        } else if (a.getPreu() < b.getPreu()) {
            return -1;
        } else {
            return 0;
        }
    }


    public static void main(String[] args) {
        Supermercat s = new Supermercat();
        try {
            s.afegirProducte(new Aliment("Patates", 1.5, 100, false));
            s.afegirProducte(new Llibre("El Quijote", 10, "Cervantes", true));
            //String nom, double preu, String color, char talla
            s.afegirProducte(new Roba("Camiseta", 10, "Blanca", 'M'));
            s.afegirProducte(new Aliment("Coca-Cola", 1.5, 100, true));
            s.afegirProducte(new Llibre("El principito", 5, "Saint-Exupéry", false));
            s.afegirProducte(new Roba("Pantaló", 20, "Negre", 'L'));
            s.afegirProducte(new Aliment("Llet", 1, 100, true));
            s.afegirProducte(new Llibre("El senyor dels anells", 15, "Tolkien", true));
            s.afegirProducte(new Roba("Camiseta", 10, "Blanca", 'S'));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        s.mostrarLlista(s.filtrarProductes("Aliment"));
        s.mostrarLlista(s.filtrarProductes("Llibre"));
        s.mostrarLlista(s.filtrarProductes("Roba"));
        s.eliminarProducte("Llet");
        s.mostrarLlista(s.filtrarProductes("Aliment"));
        s.compararPreus("Patates", "Coca-Cola");
        s.compararPreus("Patates", "Llet");
    }
    private void compararPreus(String string, String string2) {
    }
}