package com.company;

import java.util.Arrays;
import java.util.Scanner;
import static java.lang.Math.round;

public class nil_masso_2 {
    Scanner in = new Scanner(System.in);

    public void main(String[] args) {

        final var RECORD_ACTUAL = (float) 6.77;
        int opcio;
        int dorsal_corredor1 = -1;
        int dorsal_corredor2 = -1;
        String nom_corredor1 = "";
        String nom_corredor2 = "";
        float temps_corredor1 = 0;
        float temps_corredor2 = 0;
        float temps_aleatori = 0;

        funcio0();

        do {
            opcio = in.nextInt();
            in.nextLine();
            switch (opcio) {
                case 1:
                    if (funcio1(nom_corredor1, dorsal_corredor1)) {
                        System.out.println("El corredor te assignat un dorsal del 1er grup (0-50)");
                    } else
                        System.out.println("El corredor te assignat un dorsal del 2n grup (51-100)");
                    break;
                case 2:
                    funcio2(nom_corredor2, dorsal_corredor2);
                    break;
                case 3:
                    funcio3(temps_aleatori);
                    break;
                case 4:
                    int resposta;
                    System.out.println("Entra els 3 valors dels quals farem la mitja del temps");
                    String m = in.nextLine();
                    do {
                        System.out.println("A quin corredor assignem aquesta mitja (1 o 2)?");
                        resposta = in.nextInt();
                    } while ((resposta != 1) && (resposta != 2));
                    if (resposta == 1)
                        temps_corredor1 = funcio4(m);
                    else
                        temps_corredor2 = funcio4(m);
                    break;
                case 0:
                    System.out.println("Fins la propera!");
                    break;
                default:
                    System.out.println("ATENCIÓ!!! \nHa de ser un valor entre 0 i 4");
            }
        } while (opcio != 0);

    }

/*
@description: Funció que mostra el menú principal i demana una opció al usuari per a executar una de les funcions del programa.
@param: Cap
@return: Cap
*/

    public static void menu() {
        System.out.println("1. Opcio 1");
        System.out.println("2. Opcio 2");
        System.out.println("3. Opcio 3");
        System.out.println("4. Opcio 4");
        System.out.println("0. Acabar");
        System.out.print("Entra una opció (0-4):");
    }

/*
@description: Funció que demana el nom i el dorsal del corredor i retorna un booleà indicant si el dorsal és del primer o del segon grup. Si el dorsal o el nom no estan assignats els demana.
@param: String nom_corredor, int dorsal_corredor
@return: boolean (true si el dorsal és del primer grup, false si és del segon)
*/

    public boolean Grup(String nom1, int dorsal1) {

        do {
            System.out.printf("Introdueix el nom del corredor 1 (no es pot deixar en blanc): ");
            nom1 = in.next();
        } while (nom1.equals(""));
        nom1 = nom1.toUpperCase();
        do {
            System.out.printf("introdueix un numero dorsal (0-100): ");
            dorsal1 = in.nextInt();
        } while (dorsal1 < 0);
        if (dorsal1 > 0 && dorsal1 <= 50)
            return true;
        else
            return false;

    }

/*
@description: Funció que demana el nom i el dorsal del corredor metre que aquests tinguin valors per defecte
@param: String nom_corredor, int dorsal_corredor
@return: Cap
*/

    public void DorsalNom(String nom2, int dorsal2) {
        do {
            System.out.printf("Introdueix el nom del corredor 2 (no es pot deixar en blanc): ");
            nom2 = in.next();
        } while (nom2.equals(""));
        nom2 = nom2.toUpperCase();

        do {
            System.out.printf("introdueix un numero dorsal (0-100): ");
            dorsal2 = in.nextInt();
        } while (dorsal2 < 0);
    }

/*
@description: Funció que genera un temps aleatori, per a generarlo fara un bucle de 5 iteracions on cada iteració sumara un numero aleatori entre 0 i 99 a la variable temps. Despres de les 5 iteracions dividira la variable temps entre 5 per a obtenir la mitja.
@param: float temps
@return: Cap
*/

    public static void temps1(float temps) {
        temps = 0;
        for (int i = 0; i < 5; i++) {
            temps += (float) (Math.random() * 99);
        }
        temps = temps / 5;
    }

/*
@description: Funció que rep un String amb 3 valors separats per espais i retorna la mitja dels 3 valors.
@param: String temps
@return: float (mitja dels 3 valors)
*/

    public static float temps2(String mig) {
        String t = "";
        int ndx;
        float mitja = 0;
        mig = mig.trim();

        ndx = mig.indexOf(" ");
        while (ndx > 0) {
            mitja += Float.parseFloat(mig.substring(0, ndx));
            mig = mig.substring(ndx).trim();
            ndx = mig.indexOf(" ");
        }
        mitja += Float.parseFloat(mig);
        mitja = mitja / 3;

        return mitja;
    }
}
