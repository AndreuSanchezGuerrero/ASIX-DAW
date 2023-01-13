import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        menuPrincipal();
    }

    public static void menuPrincipal(){
        Scanner scan = new Scanner(System.in);
        int opcio;
        do {
            System.out.println("1. Buscar un valor en un vector");
            System.out.println("2. Ordenar un vector");
            System.out.println("3. Generar una matriu");
            System.out.println("4. Sumar parelles d'elements consecutius");
            System.out.println("5. Comprovar si hi ha 10 o més números parells");
            System.out.println("6. Comprovar si dues llistes coincideixen");
            System.out.println("7. Desplaçar els elements d'una llista");
            System.out.println("8. Barrejar una llista");
            System.out.println("0. Acabar");
            System.out.print("Entra una opció(0-8): ");
            opcio = scan.nextInt();
            scan.nextLine();
            switch (opcio) {
                case 1:
                    System.out.println("Introdueix quin valor vols buscar: ");
                    BuscarVal(scan.nextInt(),GenVec4Val());
                    break;
                case 2:
                    System.out.println("Generem un vector aleatoriament i l'ordenem....");
                    OrdenaValVec(GenVec4Val());
                    break;
                case 3:
                    System.out.println("Introdueix el número de files");
                    int files = scan.nextInt();
                    System.out.println("Introdueix el número de columnes");
                    int columnes = scan.nextInt();
                    GenMatriu(files,columnes);
                    break;
                case 4:
                    SumParellesElemConsec(SumVec());
                    break;
                case 5:
                    System.out.println("Generem números aleatoris entre 100 i 10000 ....");
                    System.out.println();
                    if(ParellsConsec())
                        System.out.println("Hi ha 10 o més números parells");;
                    break;
                case 6:
                    if (VecIguals()) {
                        System.out.println("Les llistes coincideixen");
                    }
                    else System.out.println("No s'han trobat coincidències");
                    break;
                case 7:
                    System.out.println("Entra el número d'elements de la llista");
                    int elems = scan.nextInt();
                    char[] lletres = RotacioVecChar(elems);
                    System.out.println("Mostrem els elements de la llista desplaçats: ");
                    //TODO: pendent arreglar el rang de l'array
                    for (int i = 0; i <= elems; ++i) {
                        System.out.print(lletres[i] + " ");
                    }
                    System.out.println();
                    break;
                case 8:
                    System.out.println("Mostrem una llista barrejada: ");
                    int[] llista =CombinaVec();
                    for (int i = 0; i < llista.length; ++i) {
                        System.out.print(llista[i] + " ");
                    }
                    System.out.println();
                    break;

                case 0:
                    System.out.println("Fins la propera!");
                    break;
                default:
                    System.out.println("ATENCIÓ!!! \nHa de ser un valor entre 0 i 8");
            }
        } while (opcio != 0);
    }


/**
 * Genera un vector de 4 elements amb valors aleatoris entre 1 i 10 
 * @return valors
 * @printpantalla No
 */
   public static int[] GenVec4Val(){
       final int NUM_VALORS = 4;
       int[] valors = new int[NUM_VALORS];
       for (int i = 0; i < NUM_VALORS; ++i) {
           valors[i] = (int) (Math.random() * 10 + 1);
       }
       return valors;
   }


/**
 * Busca un valor en un vector i retorna la posició on es troba
 * @param valor
 * @param n
 * @printpantalla Si, mostra la posició on es troba el valor
 */
    public static void BuscarVal (int valor, int []n){
        int min = 0;
        int max = n.length - 1;
        int mid = 0;
        System.out.println("Els valors de l'array son " + n);  //TODO: pendent de mostrar el contingut de l'array correctament
        while (min <= max) {
            mid = (min + max) / 2;
            if (n[mid] < valor) {
                min = mid + 1;
            } else if (n[mid] > valor) {
                max = mid - 1;
            } else {
                break;
            }
        }

        if (n.length > 0 && n[mid] == valor) {
            System.out.println("S'ha trobat el valor en la posició " + mid);
        } else {
            System.out.println("NO s'ha trobat el valor en la llista");
        }
    }

    /**
     * Ordena un vector de menor a major
     * @param n
     * @printpantalla Si, mostra el vector ordenat
     */
    public static void OrdenaValVec (int []n){
        int t;
        for (int i = 0; i < n.length - 1; i++) {
            for (int j = i + 1; j < n.length; j++) {
                if (n[i] > n[j]) {
                    t = n[i];
                    n[i] = n[j];
                    n[j] = t;
                }
            }
        }
        for (int i = 0; i < n.length; i++) {
            System.out.println(n[i]);
        }
    }

    /**
     * Genera una matriu de files i columnes amb valors aleatoris entre 1 i 100
     * @param f
     * @param c
     * @printpantalla Si, mostra la matriu per pantalla
     */
    public static void GenMatriu (int f, int c){

        int[][] a = new int[f][c];
        for (int i = 0; i < f; ++i) {
            for (int j = 0; j < c; ++j) {
                a[i][j] = i * j;
            }
        }
        for (int i = 0; i < f; ++i) {
            for (int j = 0; j < c; ++j) {
                System.out.print(a[i][j]);
            }
            System.out.println();
        }
    }

/**
 * Genera un vector de 10 elements amb valors aleatoris entre 1 i 100 i fa la suma dels valors de cada parella d'elements consecutius
 * @param a1
 * @printpantalla Si, mostra per pantalla la suma
 */
    public static void SumParellesElemConsec (int[] a1){
        for (int i = 0; i < a1.length; ++i) {
            a1[i] = (int)(Math.random() * 100);
            System.out.printf("%4d", a1[i]);
        }
        System.out.println();

        System.out.print("    ");
        for (int i = 1; i < a1.length; ++i) {
            System.out.printf("%4d", (a1[i - 1] + a1[i]));
        }
        System.out.println();

        for (int i = 0; i < a1.length / 2; ++i) {
            System.out.printf("%4d", (a1[i] + a1[a1.length - i - 1]));
        }
        System.out.println();
    }

    /**
     * Genera un vector de 1000 elements amb valors aleatoris entre 100 i 10000 i retorna true si hi ha 10 nombres parells consecutius i false si no
     * @return boolean
     * @printpantalla No
     */
    public static boolean ParellsConsec (){
        int n[] = new int[1000];
        int comptador = 0;
        boolean b = false;
        for (int i = 0; i < n.length; i++) {
            n[i] = (int)(Math.random() * (10000 - 100 + 1) + 100);
        }
        for (int i = 0; i < n.length; i++) {
            if (n[i] % 2 == 0) {
                ++comptador;
                if (comptador >= 10) {
                    b = true;
                    break;
                }
            }
        }
        return b;
    }

    /**
     * Genera dos vectors de 40 elements amb valors aleatoris entre 1 i 10 i retorna true si els dos vectors són iguals i false si no
     * @return boolean
     * @printpantalla No
     */
    public static boolean VecIguals(){
        final int MIDA = 40;
        int[] a1 = new int[MIDA];
        int[] a2 = new int[MIDA];
        boolean iguals = true;

        System.out.println("Generem dues llistes aleatòriament ...");
        for (int i = 0; i < MIDA; ++i) {
            a1[i] = (int)(Math.random() * 10);
            System.out.printf("%2d", a1[i]);
        }
        System.out.println();
        for (int i = 0; i < MIDA; ++i) {
            a2[i] = (int)(Math.random() * 10);
            System.out.printf("%2d", a2[i]);
        }
        System.out.println();
        for (int i = 0; i < MIDA; ++i) {
            if (a1[i] != a2[i]) {
                iguals = false;
            }
        }
        return iguals;
    }


    /**
     * Genera una llista de j elements amb valors aleatoris entre A i Z i retorna una llista amb els valors rotats una posició cap a la dreta 
     * @param j
     * @return rotat
     * @printpantalla No
     */
    public static char[] RotacioVecChar (int j){
        char[] lletres = new char[j];
        char[] rotat = new char[j];
        int l = lletres.length - 1;
        char c;

        for (int i = 0; i <= l; ++i) {
            lletres[i] = (char)(Math.random() * ('Z' - 'A' + 1) + 'A');
            System.out.print(lletres[i] + " ");
        }
        System.out.println();

        c = lletres[l];

        for (int i = l; i > 0; i--) {
            lletres[i] = lletres[i - 1];
        }

        lletres[0] = c;
        return rotat;
    }

    /**
     * Genera dos vectors de 5 elements amb valors aleatoris entre 1 i 10 i retorna un vector amb els valors dels dos vectors alternats
     * @return n3
     * @printpantalla No
     */
    public static int[] CombinaVec (){
        int[] n1 = {1,3,5,7,9};
        int[] n2 = {10,8,6,4,2};
        int[] n3 = new int[n1.length + n2.length];
        int j = 0;
        int l = n1.length > n2.length ? n1.length : n2.length;

        for (int i = 0; i < n1.length; ++i) {
            System.out.print(n1[i] + " ");
        }
        System.out.println();
        for (int i = 0; i < n2.length; ++i) {
            System.out.print(n2[i] + " ");
        }
        System.out.println();
        for (int i = 0; i < l; ++i) {
            if (i < n1.length) {
                n3[j] = n1[i];
                ++j;
            }
            if (i < n2.length) {
                n3[j] = n2[i];
                ++j;
            }
        }
        return n3;
    }


    /**
     * Genera dos vectors de 10 elements amb valors aleatoris entre 1 i 100 i retorna un vector amb els valors de la suma dels dos vectors
     * @return a3
     * @printpantalla No
     */
    public static int[] SumVec (){
        int[] a1 = new int[10];
        int[] a2 = new int[10];
        int[] a3 = new int[10];

        for (int i = 0; i < a1.length; ++i) {
            a1[i] = (int)(Math.random() * 100 + 1);
          }
        for (int i = 0; i < a1.length; ++i) {
            a2[i] = (int)(Math.random() * 100 + 1);
         }
        for (int i = 0; i < a1.length; ++i) {
        }

        for (int i = 0; i < a1.length; ++i) {
            for (int j = 0; j < a2.length; ++j) {
                a3[i] = (a1[i] + a2[j]);
            }
        }
        return a3;
    }


    /**@deprecated*/
    public static void invertirArraysLletres (){
        char[] lletres = new char[10];
        int l = lletres.length - 1;
        char c;
        for (int i = 0; i <= l; ++i) {
            lletres[i] = (char)(Math.random() * ('Z' - 'A' + 1) + 'A');
        }

        for (int i = 0; i <= l; i++) {
            System.out.printf("%2s", lletres[i]);
        }
        System.out.println();

        for (int i = l; i >= 0; i--) {
            System.out.printf("%2s", lletres[i]);
        }
        System.out.println();

         for (int i = 0; i <= l / 2; i++) {
            c = lletres[i];
            lletres[i] = lletres[l - i];
            lletres[l - i] = c;
        }

        for (int i = 0; i <= l; i++) {
            System.out.printf("%2s", lletres[i]);
        }
        System.out.println();
    }

}