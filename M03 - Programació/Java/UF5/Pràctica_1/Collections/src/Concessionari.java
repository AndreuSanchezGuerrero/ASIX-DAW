//Repetim tot el programa pero fent us de HashMap.
/*En el cas de Concessionaris, és possible aplicar ArrayList i HashMap, valoreu si us cal també aplicar ArrayList i a on. */
import java.util.HashMap;

public class Concessionari {
    //Creem un HashMap
    private static HashMap<String, Cotxe> cotxes = new HashMap<String, Cotxe>();

    //Metode per afegir cotxes
    public static void afegirCotxe(Cotxe c) throws Exception {
        //Si el cotxe ja existeix
        if (cotxes.containsKey(c.getMatricula())) {
            throw new Exception("El cotxe ja existeix");
        }
        //Afegim el cotxe al HashMap
        cotxes.put(c.getMatricula(), c);
    }

    //Metode per eliminar cotxes
    public static void eliminarCotxe(String m) {
        //Eliminem el cotxe del HashMap
        cotxes.remove(m);
    }

    //Metode per filtrar cotxes
    public static Cotxe[] filtrarCotxes(String tipus) {
        //Creem un array de cotxes
        Cotxe[] l = new Cotxe[cotxes.size()];
        //Variable que guarda el numero de cotxes
        int num = 0;
        //Recorrem el HashMap
        for (Cotxe c : cotxes.values()) {
            //Si el tipus del cotxe es igual al tipus que li passem per parametre
            if (c.getClass().getSimpleName().equals(tipus)) {
                //Afegim el cotxe a l'array
                l[num] = c;
                //Incrementam el numero de cotxes
                num++;
            }
        }
        //Creem un array de cotxes
        Cotxe[] l2 = new Cotxe[num];
        //Recorrem l'array
        for (int i = 0; i < num; i++) {
            //Igualam el cotxe actual al cotxe seguent
            l2[i] = l[i];
        }
        //Retornem l'array
        return l2;
    }

    //Metode per mostrar la llista de cotxes
    public static void mostrarLlista(Cotxe[] l) {
        //Recorrem l'array
        for (int i = 0; i < l.length; i++) {
            //Mostrem la informacio del cotxe
            System.out.println(l[i].getInfo());
        }
    }

    //Metode per ordenar els cotxes per preu
    public static void ordenarPerPreu(Cotxe[] l) {
        //Recorrem l'array
        for (int i = 0; i < l.length - 1; i++) {
            //Recorrem l'array
            for (int j = i + 1; j < l.length; j++) {
                //Si el preu del cotxe actual es mes gran que el preu del cotxe seguent
                if (l[i].getPreu() > l[j].getPreu()) {
                    //Creem un cotxe
                    Cotxe c = l[i];
                    //Igualam el cotxe actual al cotxe seguent
                    l[i] = l[j];
                    //Igualam el cotxe seguent al cotxe actual
                    l[j] = c;
                }
            }
        }
    }

    //Metode principal
    public static void main(String[] args) {
        try {
            //Afegim cotxes
            afegirCotxe(new CotxeCombustio("2236-CHC", 16000, 40, 6.5));
            afegirCotxe(new CotxeCombustio("2236-CBD", 24000, 30, 8.5));
            afegirCotxe(new CotxeCombustio("2236-CBE", 49000, 80, 10.5));
            afegirCotxe(new CotxeCombustio("2236-CBF", 16000, 60, 13.5));
            afegirCotxe(new CotxeCombustio("2236-CBG", 18000, 70, 4.5));
            afegirCotxe(new CotxeCombustio("2236-CBH", 10000, 65, 5.5));
            afegirCotxe(new CotxeElectric("2236-CBI", 30000, 120));
            afegirCotxe(new CotxeElectric("2236-CBJ", 20000, 100));
            //Mostrem la llista de cotxes
            System.out.println("Llista de cotxes");
            mostrarLlista(cotxes.values().toArray(new Cotxe[cotxes.size()]));
            System.out.println();
            //Eliminem un cotxe
            eliminarCotxe("2236-CBC");
            //Mostrem la llista de cotxes amb un cotxe eliminat
            System.out.println("Llista de cotxes amb un cotxe eliminat");
            mostrarLlista(cotxes.values().toArray(new Cotxe[cotxes.size()]));
            System.out.println();
            //Filtrem els cotxes per tipus i els guardam a un array
            Cotxe[] l = filtrarCotxes("CotxeCombustio");
            //Mostrem la llista de cotxes de combustio
            System.out.println("Llista de cotxes de combustio");
            mostrarLlista(l);
            System.out.println();
            //Ordenam els cotxes per preu i els guardam a un array
            ordenarPerPreu(l);
            //Mostrem la llista de cotxes de combustio ordenats per preu
            System.out.println("Llista de cotxes de combustio ordenats per preu");
            mostrarLlista(l);
            System.out.println();
        //Si hi ha una excepcio
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}