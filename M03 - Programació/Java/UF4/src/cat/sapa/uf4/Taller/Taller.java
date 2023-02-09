package cat.sapa.uf4.Taller;
    /*4 - Taller d'ordinadors

Per muntar un ordinador de sobretaula cal triar, com a mínim:

    Un monitor
    Un teclat
    Un ratolí
    Una torre

Crea les classes Monitor, Teclat, Ratoli i Torre amb els atributs i mètodes que consideris necessaris.
Com a mínim han de tenir marca, model, preu i algunes característiques interessants.

Crea uns quants monitors, teclats, ratolins i torres (amb 2 o 3 de cada n'hi ha prou, no cal crear arrays).

Crea la classe Ordinador que tingui com atributs un monitor, un teclat, un ratoli i una torre.

També ha de tenir un mètode per calcular el preu final i un altre per retornar les característiques.

Fes una classe de prova per crear un ordinador triant els diferents components.
Un cop creat, s'hauran de mostrar les característiques i el preu total.

Opcionalment, pots crear la classe Taller amb un menú per triar els components de l'ordinador.
Igual que abans, un cop triats els components, haurà de mostrar les característiques i el preu final. */

import java.util.Arrays;
import java.util.Scanner;

public class Taller {
    public static void main(String[] args) {
        //Creem varis objectes de les classes Monitor, Teclat, Ratoli i Torre
        //Monitor(String marca, String model, Float preu, int polzades, int hz, int amplada, int alcada)
        Monitor monitor1 = new Monitor("HP", "V194", 100, 19, 60, 1600, 900);
        Monitor monitor2 = new Monitor("Acer", "V196L", 120, 19, 60, 1600, 900);
        Monitor monitor3 = new Monitor("Lenovo", "L1940P", 150, 19, 60, 1600, 900);
        //Teclat(String marca, String model, int preu, String tipus)
        Teclat teclat1 = new Teclat("Logitech", "K120", 10, "QWERTY");
        Teclat teclat2 = new Teclat("HP", "KB-0316", 15, "QWERTY");
        //Ratoli(String marca, String model, int preu, int numBotoes)
        Ratoli ratoli1 = new Ratoli("Logitech", "M100", 10, 3);
        Ratoli ratoli2 = new Ratoli("HP", "X3000", 15, 3);
        Ratoli ratoli3 = new Ratoli("Logitech", "M185", 15, 3);
        //Torre(String marca, String model, int preu, int capacitatDisc, int capacitatRAM, String CPU)
        Torre torre1 = new Torre("HP", "250-G3", 300, 500, 4, "Intel Core i3-5005U");
        Torre torre2 = new Torre("Lenovo", "ThinkCentre M700", 400, 500, 4, "Intel Core i3-6100");
        Torre torre3 = new Torre("Acer", "Aspire XC-705", 350, 500, 4, "Intel Core i3-6100");
        //Ordinador(int preu, Monitor monitor, Teclat teclat, Ratoli ratoli, Torre torre)
        Ordinador ordinador1 = new Ordinador(1000, monitor1, teclat1, ratoli1, torre1);
        Ordinador ordinador2 = new Ordinador(1100, monitor2, teclat2, ratoli2, torre2);
        Ordinador ordinador3 = new Ordinador(1200, monitor3, teclat1, ratoli3, torre3);
        Ordinador ordinador4 = new Ordinador(1300, monitor1, teclat2, ratoli1, torre1);
        Ordinador ordinador5 = new Ordinador(1400, monitor2, teclat1, ratoli2, torre2);

        //Creem un array amb els objectes de les classes Monitor, Teclat, Ratoli i Torre
        Monitor[] monitors = {monitor1, monitor2, monitor3};
        Teclat[] teclats = {teclat1, teclat2};
        Ratoli[] ratolis = {ratoli1, ratoli2, ratoli3};
        Torre[] torres = {torre1, torre2, torre3};

        //Creem un array amb els objectes de la classe Ordinador
        Ordinador[] ordinadors = {ordinador1, ordinador2, ordinador3, ordinador4, ordinador5};

        //Menu
        Scanner sc = new Scanner(System.in);
        int opcio = 0;
        do {
            System.out.println("1. Crear un ordinador");
            System.out.println("2. Mostrar caracteristiques d'un ordinador");
            System.out.println("3. Mostrar preu d'un ordinador");
            System.out.println("4. Sortir");
            System.out.print("Opcio: ");
            opcio = sc.nextInt();
            switch (opcio) {
                case 1:
                    //Creem un objecte de la classe Ordinador
                    Ordinador ordinador = new Ordinador();
                    //Triem el monitor
                    System.out.println("Monitors disponibles:");
                    for (int i = 0; i < monitors.length; i++) {
                        System.out.println((i + 1) + ". " + monitors[i].getMarca() + " " + monitors[i].getModel());
                    }
                    System.out.print("Tria un monitor: ");
                    int monitor = sc.nextInt();
                    ordinador.setMonitor(monitors[monitor - 1]);
                    //Triem el teclat
                    System.out.println("Teclats disponibles:");
                    for (int i = 0; i < teclats.length; i++) {
                        System.out.println((i + 1) + ". " + teclats[i].getMarca() + " " + teclats[i].getModel());
                    }
                    System.out.print("Tria un teclat: ");
                    int teclat = sc.nextInt();
                    ordinador.setTeclat(teclats[teclat - 1]);
                    //Triem el ratoli
                    System.out.println("Ratolis disponibles:");
                    for (int i = 0; i < ratolis.length; i++) {
                        System.out.println((i + 1) + ". " + ratolis[i].getMarca() + " " + ratolis[i].getModel());
                    }
                    System.out.print("Tria un ratoli: ");
                    int ratoli = sc.nextInt();
                    ordinador.setRatoli(ratolis[ratoli - 1]);
                    //Triem la torre
                    System.out.println("Torres disponibles:");
                    for (int i = 0; i < torres.length; i++) {
                        System.out.println((i + 1) + ". " + torres[i].getMarca() + " " + torres[i].getModel());
                    }
                    System.out .print("Tria una torre: ");
                    int torre = sc.nextInt();
                    ordinador.setTorre(torres[torre - 1]);
                    //Calculem el preu
                    ordinador.setPreu(ordinador.getMonitor().getPreu() + ordinador.getTeclat().getPreu() + ordinador.getRatoli().getPreu() + ordinador.getTorre().getPreu());
                    //Afegim l'objecte Ordinador a l'array ordinadors
                    ordinadors = Arrays.copyOf(ordinadors, ordinadors.length + 1);
                    ordinadors[ordinadors.length - 1] = ordinador;
                    break;
                case 2:
                    //Mostrar caracteristiques d'un ordinador
                    System.out.println("Ordinadors disponibles:");
                    for (int i = 0; i < ordinadors.length; i++) {
                        System.out.println((i + 1) + ". " + ordinadors[i].getMonitor().getMarca() + " " + ordinadors[i].getMonitor().getModel() + " " + ordinadors[i].getTeclat().getMarca() + " " + ordinadors[i].getTeclat().getModel() + " " + ordinadors[i].getRatoli().getMarca() + " " + ordinadors[i].getRatoli().getModel() + " " + ordinadors[i].getTorre().getMarca() + " " + ordinadors[i].getTorre().getModel());
                    }
                    System.out.print("Tria un ordinador: ");
                    int ord = sc.nextInt();
                    //Ha de mostrar tambe les caracteristiques dels components
                    System.out.println("Monitor: " + ordinadors[ord - 1].getMonitor().getMarca() + " " + ordinadors[ord - 1].getMonitor().getModel() + " " + ordinadors[ord - 1].getMonitor().getPreu());
                    System.out.println("Teclat: " + ordinadors[ord - 1].getTeclat().getMarca() + " " + ordinadors[ord - 1].getTeclat().getModel() + " " + ordinadors[ord - 1].getTeclat().getPreu());
                    System.out.println("Ratoli: " + ordinadors[ord - 1].getRatoli().getMarca() + " " + ordinadors[ord - 1].getRatoli().getModel() + " " + ordinadors[ord - 1].getRatoli().getPreu());
                    System.out.println("Torre: " + ordinadors[ord - 1].getTorre().getMarca() + " " + ordinadors[ord - 1].getTorre().getModel() + " " + ordinadors[ord - 1].getTorre().getPreu());
                    break;
                case 3:
                    //Mostrar preu d'un ordinador
                    System.out.println("Ordinadors disponibles:");
                    for (int i = 0; i < ordinadors.length; i++) {
                        System.out.println((i + 1) + ". " + ordinadors[i].getMonitor().getMarca() + " " + ordinadors[i].getMonitor().getModel() + " " + ordinadors[i].getTeclat().getMarca() + " " + ordinadors[i].getTeclat().getModel() + " " + ordinadors[i].getRatoli().getMarca() + " " + ordinadors[i].getRatoli().getModel() + " " + ordinadors[i].getTorre().getMarca() + " " + ordinadors[i].getTorre().getModel());
                    }
                    System.out.print("Tria un ordinador: ");
                    int ord2 = sc.nextInt();
                    System.out.println("Preu: " + ordinadors[ord2 - 1].getPreu());
                    break;
                case 4:
                    //Sortir
                    break;
                default:
                    System.out.println("Opcio incorrecta");
            }
        } while (opcio != 4);
    }
}
