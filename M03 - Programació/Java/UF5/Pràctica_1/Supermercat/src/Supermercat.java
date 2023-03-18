import java.util.ArrayList;

//Creem la classe Supermercat
public class Supermercat {
    //Creem l'arraylist de productes
    private ArrayList<Producte> llistaProductes;
    //Creem el constructor
    public Supermercat() {
        llistaProductes = new ArrayList<Producte>();
    }
    //Creem el mètode afegirProducte per afegir un producte a l'arraylist
    public void afegirProducte(Producte p) {
        llistaProductes.add(p);
    }
    //Creem el mètode eliminarProducte per eliminar un producte de l'arraylist
    public void eliminarProducte(String n) {
        for (int i = 0; i < llistaProductes.size(); i++) {
            if (llistaProductes.get(i).getNom().equals(n)) {
                llistaProductes.remove(i);
            }
        }
    }
    //Creem el mètode filtrarProductes per filtrar els productes per tipus i retornar un arraylist amb els productes filtrats
    public ArrayList<Producte> filtrarProductes(String tipus) {
        ArrayList<Producte> aux = new ArrayList<Producte>();
        for (int i = 0; i < llistaProductes.size(); i++) {
            if (llistaProductes.get(i).getClass().getSimpleName().equals(tipus)) {
                aux.add(llistaProductes.get(i));
            }
        }
        return aux;
    }
    //Creem el mètode mostrarLlista per mostrar els productes de l'arraylist que li passem per paràmetre
    public void mostrarLlista(ArrayList<Producte> l) {
        for (int i = 0; i < l.size(); i++) {
            System.out.println(l.get(i));
        }
    }

    //Creem el mètode compararPreus per comparar els preus de dos productes i retornar un enter 
    /* //Comparem els preus de dos productes
        s.compararPreus("Patates", "Coca-Cola");
        s.compararPreus("Patates", "Llet"); */
    public int compararPreus(String n1, String n2) {
        int aux = 0;
        for (int i = 0; i < llistaProductes.size(); i++) {
            if (llistaProductes.get(i).getNom().equals(n1)) {
                for (int j = 0; j < llistaProductes.size(); j++) {
                    if (llistaProductes.get(j).getNom().equals(n2)) {
                        if (llistaProductes.get(i).getPreu() > llistaProductes.get(j).getPreu()) {
                            aux = 1;
                        } else if (llistaProductes.get(i).getPreu() < llistaProductes.get(j).getPreu()) {
                            aux = -1;
                        } else {
                            aux = 0;
                        }
                    }
                }
            }
        }
        return aux;
    }

    //Creem el mètode main
    public static void main(String[] args) {
        //Creem un objecte de la classe Supermercat
        Supermercat s = new Supermercat();
        //Afegim productes a l'arraylist
        try {
            s.afegirProducte(new Aliment("Patates", 1.5, 100, false));
            s.afegirProducte(new Llibre("El Quijote", 10, "Cervantes", true));
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
        //Mostrem els productes filtrats per tipus
        s.mostrarLlista(s.filtrarProductes("Aliment"));
        s.mostrarLlista(s.filtrarProductes("Llibre"));
        s.mostrarLlista(s.filtrarProductes("Roba"));
        //Eliminem un producte
        s.eliminarProducte("Llet");
        //Mostrem els productes filtrats per tipus
        s.mostrarLlista(s.filtrarProductes("Aliment"));
        //Comparem els preus de dos productes
        s.compararPreus("Patates", "Coca-Cola");
        s.compararPreus("Patates", "Llet");
    }
}
