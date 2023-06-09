package cat.sapa.uf4.Article;

import java.io.File;
import java.io.FileNotFoundException;
import java.text.DecimalFormat;
import java.util.Scanner;

/*3 - Classe Article

Crea la classe Article amb els atributs:

    codi: string (4 caràcters),
    descripcio: string,
    unitats: int (no pot ser negatiu),
    preu: float (no pot ser inferior a 10 cèntims),
    iva: int (només pot ser 0, 4, 5, 10 o 21) representa el tant per cent d'IVA.

Ha de tenir un constructor per inicialitzar els atributs anteriors.
S'han de fer les totes les comprovacions necessàries i no crear l'objecte si alguna dada no és correcta.

Ha de tenir un mètode per obtenir el preu final multiplicant el preu per les unitats i sumant l'IVA.

S'han de crear getters per totes les propietats i setters per les unitats, preu i IVA.
Els setters han de verificar que les dades siguin correctes. Si no ho són, no actualitzaran l'atribut corresponent i retornaran false.

El mètode toString() ha de retornar un string amb el format codi : descripcio : preuFinal.
El preu final s'ha de mostrar en el format local (2 decimals separats per coma i el símbol de l'€: 12,50 €).

Crea també una classe TestArticle amb un mètode main() que tingui un array per guardar 5 articles.
Ha de tenir un mètode per demanar les dades d'aquests articles a l'usuari.
Si alguna dada no és correcta o es produeix algun error, no s'ha de crear l'article ni afegir-lo a l'array.

Afegeix en aquesta classe un mètode per sumar i mostrar el total dels articles comprats.

És molt recomanable utilitzar la introducció automàtica de dades des d'un arxiu per fer les proves! */

public class Article {
    private String codi;
    private String descripcio;
    private int unitats;
    private float preu;
    private int iva;

    public Article(String codi, String descripcio, int unitats, float preu, int iva) {
        this.codi = codi;
        this.descripcio = descripcio;
        this.unitats = unitats;
        this.preu = preu;
        this.iva = iva;
    }

    public String getCodi() {
        return codi;
    }

    public String getDescripcio() {
        return descripcio;
    }

    public int getUnitats() {
        return unitats;
    }

    public float getPreu() {
        return preu;
    }

    public int getIva() {
        return iva;
    }

    public boolean setUnitats(int unitats) {
        if (unitats < 0) {
            return false;
        }
        this.unitats = unitats;
        return true;
    }

    public boolean setPreu(float preu) {
        if (preu < 0.1) {
            return false;
        }
        this.preu = preu;
        return true;
    }

    public boolean setIva(int iva) {
        if (iva != 0 && iva != 4 && iva != 5 && iva != 10 && iva != 21) {
            return false;
        }
        this.iva = iva;
        return true;
    }

    public float getPreuFinal() {
        return (preu * unitats) * (1 + iva / 100f);
    }

    @Override
    public String toString() {
        return codi + " : " + descripcio + " : " + String.format("%.2f €", getPreuFinal());
    }

    public void setCodi(String codi) {
        this.codi = codi;
    }

    public void setDescripcio(String descripcio) {
        this.descripcio = descripcio;
    }
}

class TestArticle {
    private static Article[] articles = new Article[5];

    public static void main(String[] args) {
        llegeixFitxer();
        mostraTotal();
    }

    private static void llegeixFitxer() {
        try {
            Scanner scanner = new Scanner(new File("UF4/src/cat/sapa/uf4/Article/dadesArticles.txt"));
            int i = 0;
            while (scanner.hasNextLine() && i < articles.length) {
                String[] dades = scanner.nextLine().split(",");
                if (dades.length == 5) {
                    Article article = new Article(dades[0], dades[1], Integer.parseInt(dades[2]), Float.parseFloat(dades[3]), Integer.parseInt(dades[4]));
                    articles[i] = article;
                    i++;
                }
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("No s'ha pogut trobar el fitxer dadesArticles.txt");
        }
    }

    private static void mostraTotal() {
        DecimalFormat df = new DecimalFormat("#.00");
        float total = 0;
        for (Article Article : articles) {
            if (Article != null) {
                System.out.println(Article);
                total += Article.getPreuFinal();
            }
        }
        System.out.println("Total: " + df.format(total) + " €");
    }
}