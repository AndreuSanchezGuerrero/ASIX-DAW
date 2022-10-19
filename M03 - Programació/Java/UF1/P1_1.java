/*Botiga online

Si heu vist la sèrie The Big Bang Theory, segurament coneixereu el Sheldon Cooper i l'Amy Farrah Fowler, apassionats per la vexilologia (disciplina que estudia les banderes i escuts heràldics).
Els agrada tant el tema que han decidit muntar una botiga online (e-commerce) anomenat "Diversió i compra de banderes".
Però com estan molt enfeinats amb la super-asimetria, una teoria que els pot fer guanyar el premi Nobel, ens han demanat ajuda amb el programa.

 

El programa haurà de mostrar un menú amb, almenys, 8 banderes i/o escuts identificats amb un codi que pot contenir dígits i lletres.
L’usuari haurà de triar una de les opcions escrivint el codi. Si l’opció no és vàlida, el programa finalitzarà indicant l’error.
Utilitza l’estructura switch almenys en aquest apartat, per fer la comprovació o altres tasques.

Exemple de menú:

ESCUTS STAR TREK
F1 - Ferengi
K2 - Klingon
R1 - Romulans
V3 - Vulcanians
Escriu el codi de l’escut que vols: 

 

Després ha de demanar la mida de la bandera o escut en centímetres (amplada i alçada), si la forma ha de ser rectangular, amb cantonades arrodonides o en forma ovalada (R, A, O) i finalment, si vol brodar un text (SÍ o NO); en cas que sigui que sí, a continuació s’ha d’escriure el text (pot contenir més d’una paraula).

Per si l’usuari escriu en minúscula, és convenient convertir a majúscules (excepte el text).
Si les opcions no són R, A, O, SÍ o NO, el programa finalitzarà indicant l’error.
Si s’ha indicat que es vol brodar un text (SÍ) però el text està buit o té més de 24 caracters, també s’ha de mostrar l’error i finalitzar.

Exemple de dades a introduir:

Introdueix l’amplada i alçada en centímetres, la forma (R, A o O), si vols un text (SI o NO) i el text:
30 50 A SI Guanyar o morir

 

El preu es calcularà en funció dels paràmetres anteriors:

    un cèntim per cada centímetre quadrat que ocupi la bandera o l’escut.
    si ha triat cantonades arrodonides (un euro més) o forma ovalada (dos euros més).
    si vol brodar un text, 10 cèntims més per cada lletra (incloent espais).
    si el preu és inferior a 30 €, es cobraran 3 € d’enviament.

A part de mostrar el preu, s’ha de mostrar un resum de les dades en columnes (si no es vol brodar un text, no s’ha de mostrar la línia corresponent):
Bandera (o escut) 	Klingon
Amplada i alçada 	30 x 50 = 1500 cm2 	15,00 €
Forma 	Cantonades arrodonides 	1,00 €
Text 	Guanyar o morir 	1,50 €
Subtotal 		17,50 €
Transport 		3,00 €
TOTAL 		20,50 €

 

Alguns mètodes útils

Per tancar un programa es pot utilitzar la comanda System.exit(0), però en programes senzills com aquest, que només tenen una funció, és més fàcil utilitzar simplement return.

Per saber quants caràcters té un text es pot utilitzar el mètode String.length().

Per convertir caràcters o textos a majúscules es poden utilitzar els mètodes Character.toUpperCase(ch) o String.toUpperCase().

Un altre mètode dels Strings que us pot ser útil és String.trim(), que elimina els espais que pugui tenir un text al principi i al final.

Recorda que per comparar textos s’ha d’utilitzar String.equals(text).*/

import java.util.Scanner;

public class P1_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String codi, forma, vtext, text;
        int amplada, alcada;
        double preu;
        System.out.println("ESCUTS STAR TREK");
        System.out.println("F1 - Ferengi");
        System.out.println("K2 - Klingon");
        System.out.println("R1 - Romulans");
        System.out.println("V3 - Vulcanians");
        System.out.print("Escriu el codi de l'escut que vols: ");
        codi = sc.nextLine();
        switch (codi) {
            case "F1":
            case "K2":
            case "R1":
            case "V3":
                System.out.print("Introdueix l'amplada i alçada en centímetres, la forma (R, A o O), si vols un text (SI o NO) i el text: ");
                amplada = sc.nextInt();
                alcada = sc.nextInt();
                forma = sc.next();
                forma = forma.toUpperCase();
                vtext = sc.next();
                text = sc.nextLine();
                text = text.trim();
                if (forma.equals("R") || forma.equals("A") || forma.equals("O")) {
                    preu = ((amplada * alcada)/100);
                    if (forma.equals("A")) {
                        preu += 1;
                    } else if (forma.equals("O")) {
                        preu += 2;
                    }
                    if (vtext.equals("SI")) {
                        if (text.length() > 0 && text.length() <= 24) {
                            preu += text.length() * 0.1;
                        } else {
                            System.out.println("Error: el text no pot estar buit ni tenir més de 24 caràcters.");
                            return;
                        }
                    }
                    System.out.println("Bandera (o escut)\t" + codi);
                    System.out.println("Amplada i alçada\t" + amplada + " x " + alcada + " = " + (amplada * alcada) + " cm2\t" + (amplada * alcada) / 100.0 + " €");
                    if (forma.equals("A")) {
                        System.out.println("Forma\t\t\tCantonades arrodonides\t1.0 €");
                    } else if (forma.equals("O")) {
                        System.out.println("Forma\t\t\tForma ovalada\t\t2.0 €");
                    }
                    if (vtext.equals("SI")) {
                        System.out.println("Text\t\t\t" + text + "\t\t" + text.length() * 0.1 + " €");
                    }
                    System.out.println("Subtotal\t\t\t\t\t" + preu + " €");
                    if (preu < 30) {
                        System.out.println("Transport\t\t\t\t\t3.0 €");
                        preu += 3;
                    }
                    System.out.println("TOTAL\t\t\t\t\t\t" + preu + " €");
                } else {
                    System.out.println("Error: la forma ha de ser R, A o O.");
                }
                break;
            default:
                System.out.println("Error: el codi de l'escut ha de ser F1, K2, R1 o V3.");
        }
    }
}
