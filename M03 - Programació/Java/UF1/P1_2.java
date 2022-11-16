/*
Cursa de carreres (2)

El programa que vau fer anteriorment es pot millorar bastant.

Ara es tracta de fer un programa sobre una cursa, en el que ens apareixerà el següent menú:

1. Introduir dades corredor 1
2. Introduir dades corredor 2
3. Assignar un temps fent la mitja de 5 valors aleatoris
4. Assignar un temps amb 3 valors entrats per teclat
0. Acabar
Entra una opció (0-4):

Si s'escull l'opció 1 o 2, s'haurà de introduir el nom del corredor 1 o 2 respectivament.
També s'haurà d'introduir un dorsal amb un número comprés entre 0 i 100.
S'ha de verificar que  el nom no estigui en blanc, que el dorsal estigui entre 0 i 100 i que no coïncideixi amb el de l'altre corredor.
En cas d'error, s'han de tornar a demanar les dades.

Si s'escull l'opció 3, es generaran 5 valors reals aleatoris entre 10 i 20, es calcularà la mitjana i se li assignarà al corredor 1.

Si s'escull l'opció 4, s'han d'introduir tres valors (tots en la mateixa línia), s'han de llegir tots de cop (en un únic string), separar-los, calcular la mitjana i assignar-la al corredor 2.

Si s'escull l'opció 0, el programa finalitzarà mostrant les dades tabulades dels dos corredors: dorsal, nom i temps amb 2 decimals.

Qualsevol altra opció no serà vàlida.

Exemple de resultat

RESULTATS
---------------------
Dorsal  Nom     Temps
    50  Pere    16,42
     6  Xavier   9,70
---------------------
*/

import java.util.Scanner;
import java.util.Random;

public class P1_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random r = new Random();
        int dorsal1 = -1, dorsal2 = -1;
        String nom1 = "", nom2 = "";
        double temps1 = 0, temps2 = 0;
        int opcio = 0;
        do {
            System.out.println("1. Introduir dades corredor 1");
            System.out.println("2. Introduir dades corredor 2");
            System.out.println("3. Assignar un temps fent la mitja de 5 valors aleatoris");
            System.out.println("4. Assignar un temps amb 3 valors entrats per teclat");
            System.out.println("0. Acabar");
            System.out.print("Entra una opció (0-4): ");
            opcio = sc.nextInt();
            switch (opcio) {
                case 1:
                    System.out.print("Entra el nom del corredor 1: ");
                    nom1 = sc.next();
                    System.out.print("Entra el dorsal del corredor 1: ");
                    while (dorsal1 < 0 || dorsal1 > 100) {
                        dorsal1 = sc.nextInt();
                        if (dorsal1 < 0 || dorsal1 > 100) {
                            System.out.println("El dorsal ha de ser un número entre 0 i 100");
                        }
                        if (dorsal1 == dorsal2) {
                            System.out.println("El dorsal ha de ser diferent al del corredor 2");
                            dorsal1 = 0;
                        }
                    }
                    break;
                case 2:
                    System.out.print("Entra el nom del corredor 2: ");
                    nom2 = sc.next();
                    System.out.print("Entra el dorsal del corredor 2: ");
                    while (dorsal2 < 0 || dorsal2 > 100) {
                        dorsal2 = sc.nextInt();
                        if (dorsal2 < 0 || dorsal2 > 100) {
                            System.out.println("El dorsal ha de ser un número entre 0 i 100");
                        }
                        if (dorsal2 == dorsal1) {
                            System.out.println("El dorsal ha de ser diferent al del corredor 1");
                            dorsal2 = 0;
                        }
                    }
                    break;
                case 3:
                    for (int i = 0; i < 5; i++) {
                        temps1 += 10 + r.nextDouble() * 10;
                    }
                    temps1 /= 5;
                    break;
                case 4:
                    System.out.print("Entra els 3 temps del corredor 2: ");
                    for (int i = 0; i < 3; i++) {
                        temps2 += sc.nextDouble();
                    }
                    temps2 /= 3;
                    break;
                case 0:
                    System.out.println("RESULTATS");
                    System.out.println("---------------------");
                    System.out.println("Dorsal  Nom     Temps");
                    System.out.printf("%5d  %s    %.2f %n", dorsal1, nom1, temps1);
                    System.out.printf("%5d  %s    %.2f %n", dorsal2, nom2, temps2);
                    System.out.println("---------------------");
                    break;
                default:
                    System.out.println("Opció incorrecta");
                    break;
            }
        } while (opcio != 0);
    }
}

