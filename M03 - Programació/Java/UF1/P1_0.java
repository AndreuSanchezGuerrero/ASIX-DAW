/*Cursa de carreres entre 2 profes

Fes un programa que demani:

    el nom del primer corredor,
    el dorsal del primer corredor,
    i el nom del segon corredor.

El dorsal del segon corredor s'ha de generar aleatòriament entre 0 i 99 (tots dos inclosos).

Després ha de:

    mostrar el nom i el dorsal dels dos corredors,
    demanar el temps que ha fet cada un en minuts (pot tenir decimals),
    i mostrar una taula amb els resultats de forma semblant a com es mostra més avall.

També has d'inclure una constant amb el rècord anterior.

Exemple d'execució

Introdueix el nom del corredor 1: Pere
Introdueix el numero dorsal: 50
Introdueix el nom del corredor 2: Xavier
El dorsal s'ha assignat aleatòriament (0 a 99)...
 
El dorsal de Pere és 50
El dorsal de Xavier és 16
 
Introdueix els minuts que ha trigat el 1r corredor: 6,8
Introdueix els minuts que ha trigat el 2n corredor: 6,7

RESULTATS
--------------------------------------------------------
Dorsal  Nom     Temps  Nou rècord?
    50  Pere     6,80  false
    16  Xavier   6,70  true
--------------------------------------------------------
Rècord anterior: 6.77*/

import java.util.Scanner;
import java.util.Random;

public class P1_0 {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        
        Random r = new Random();
        final double RECORD_ANTERIOR = 6.77;
        String nom1, nom2;
        int dorsal1, dorsal2;
        double temps1, temps2;
        boolean nouRecord;

        System.out.print("Introdueix el nom del corredor 1: ");
        nom1 = sc.nextLine();
        System.out.print("Introdueix el numero dorsal: ");
        dorsal1 = sc.nextInt();
        sc.nextLine();
        System.out.print("Introdueix el nom del corredor 2: ");
        nom2 = sc.nextLine();
        dorsal2 = r.nextInt(100);
        System.out.println("El dorsal s'ha assignat aleatòriament (0 a 99)...");
        System.out.println();
        System.out.println("El dorsal de " + nom1 + " és " + dorsal1);
        System.out.println("El dorsal de " + nom2 + " és " + dorsal2);
        System.out.println();
        System.out.print("Introdueix els minuts que ha trigat el 1r corredor: ");
        temps1 = sc.nextDouble();
        System.out.print("Introdueix els minuts que ha trigat el 2n corredor: ");
        temps2 = sc.nextDouble();
        System.out.println();
        System.out.println("RESULTATS");
        System.out.println("--------------------------------------------------------");
        System.out.printf("%-7s%-8s%-8s%-10s%n", "Dorsal", "Nom", "Temps", "Nou rècord?");
        System.out.printf("%-7d%-8s%-8.2f%-10b%n", dorsal1, nom1, temps1, false);
        if (temps2 < RECORD_ANTERIOR) {
            nouRecord = true;
        } else {
            nouRecord = false;
        }
        System.out.printf("%-7d%-8s%-8.2f%-10b%n", dorsal2, nom2, temps2, nouRecord);
        System.out.println("--------------------------------------------------------");
        System.out.printf("Rècord anterior: %.2f%n", RECORD_ANTERIOR);
    }
}