//Class COncessionari
public class Concessionari {
    //Array de cotxes
    private static Cotxe[] cotxes = new Cotxe[8];
    //Variable que guarda el numero de cotxes
    private static int numCotxes = 0;

    //Metode per afegir cotxes
    public static void afegirCotxe(Cotxe c) throws Exception {
        //Si el numero de cotxes es igual a la longitud de l'array
        if (numCotxes == cotxes.length) {
            //Llançem una excepcio
            throw new Exception("No caben més cotxes");
        }
        //Afegim el cotxe a l'array
        cotxes[numCotxes] = c;
        //Incrementem el numero de cotxes
        numCotxes++;
    }

    //Metode per eliminar cotxes
    public static void eliminarCotxe(String m) {
        //Recorrem l'array
        for (int i = 0; i < numCotxes; i++) {
            //Si la matricula del cotxe es igual a la matricula que li passem per parametre
            if (cotxes[i].getMatricula().equals(m)) {
                //Recorrem l'array
                for (int j = i; j < numCotxes - 1; j++) {
                    //Igualem el cotxe actual al cotxe seguent
                    cotxes[j] = cotxes[j + 1];
                }
                //Decreixem el numero de cotxes
                numCotxes--;
                //I sortim del bucle
                break;
            }
        }
    }

    //Metode per filtrar cotxes
    public static Cotxe[] filtrarCotxes(String tipus) {
        //Creem un array de cotxes
        Cotxe[] l = new Cotxe[numCotxes];
        //Variable que guarda el numero de cotxes
        int num = 0;
        //Recorrem l'array
        for (int i = 0; i < numCotxes; i++) {
            //Si el tipus del cotxe es igual al tipus que li passem per parametre
            if (cotxes[i].getClass().getSimpleName().equals(tipus)) {
                //Afegim el cotxe a l'array
                l[num] = cotxes[i];
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
            afegirCotxe(new CotxeCombustio("2236-CBC", 16000, 40, 6.5));
            afegirCotxe(new CotxeCombustio("2236-CBD", 24000, 30, 8.5));
            afegirCotxe(new CotxeCombustio("2236-CBE", 49000, 80, 10.5));
            afegirCotxe(new CotxeCombustio("2236-CBF", 16000, 60, 13.5));
            afegirCotxe(new CotxeCombustio("2236-CBG", 18000, 70, 4.5));
            afegirCotxe(new CotxeCombustio("2236-CBH", 10000, 65, 5.5));
            afegirCotxe(new CotxeElectric("2236-CBI", 30000, 120));
            afegirCotxe(new CotxeElectric("2236-CBJ", 20000, 100));
            //Mostrem la llista de cotxes
            System.out.println("Llista de cotxes");
            mostrarLlista(cotxes);
            System.out.println();
            //Eliminem un cotxe
            eliminarCotxe("2236-CBC");
            //Mostrem la llista de cotxes amb un cotxe eliminat
            System.out.println("Llista de cotxes amb un cotxe eliminat");
            mostrarLlista(cotxes);
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