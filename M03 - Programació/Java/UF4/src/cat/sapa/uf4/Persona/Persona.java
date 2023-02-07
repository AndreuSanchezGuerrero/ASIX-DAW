package cat.sapa.uf4.Persona;
import java.time.LocalDate;

public class Persona {
    /* 1 - Classe Persona

    Crea la classe Persona amb els atributs:

    nif: string amb 8 dígits i una lletra majúscula,
    nom: string,
    dataNaixement: string amb el format DD-MM-AAAA.

    Ha de tenir un constructor per inicialitzar els atributs anteriors.
    De moment, no es verificarà que les dades siguin correctes.

    Ha de tenir un mètode per obtenir l'edat de la persona.
    La classe java.time.LocalDate té mètodes que et poden ser útils.

    Fes el mètode toString() que retorni un string amb el format nif : nom : edat.

    Els atributs han de ser privats i els mètodes, públics.

    Crea també una classe TestPersona amb un mètode main() que creï unes quantes persones i mostri les seves dades.
    
    2 - Classe Persona (v2.0)

    Afegeix a la classe Persona un atribut que serveixi per comptar quantes persones s'han creat i un mètode per consultar aquest atribut.

    Crea també els mètodes getNif(), getNom() i getDataNaixement() per obtenir aquestes dades.

    A més, ha de tenir mètodes privats per comprovar si un NIF i una data de naixement són correctes.
    En cas que alguna d'elles no ho sigui, el constructor ha de llençar una excepció que serà tractada en el mètode creador(nif, nom, dn), que serà l'encarregat de crear les persones.
    Aquest mètode s'ha de definir en la classe TestPersona i ha de retornar la persona creada o, en cas d'error, ha de mostrar un missatge per consola i retornar null.

    En el mètode main() de la classe TestPersona crea alguna persona amb dades incorrectes.
    Després de mostrar la informació de les persones, mostra quantes s'han creat.
*/
    private String nif;
    private String nom;
    private String dataNaixement;
    private static int numPersones = 0;
    private int edat;

    public Persona(String nif, String nom, String dataNaixement) {
        if (comprovarNif(nif)) {
            this.nif = nif;
        } else {
            throw new IllegalArgumentException("NIF incorrecte");
        }
        this.nom = nom;
        if (comprovarData(dataNaixement)) {
            this.dataNaixement = dataNaixement;
        } else {
            throw new IllegalArgumentException("Data de naixement incorrecte");
        }
    }

    public String getNif() {
        return nif;
    }

    public String getNom() {
        return nom;
    }

    public String getDataNaixement() {
        return dataNaixement;
    }

    public int getEdat() {
        String[] data = dataNaixement.split("-");
        int dia = Integer.parseInt(data[0]);
        int mes = Integer.parseInt(data[1]);
        int any = Integer.parseInt(data[2]);
        LocalDate dataActual = LocalDate.now();
        int anyActual = dataActual.getYear();
        int mesActual = dataActual.getMonthValue();
        int diaActual = dataActual.getDayOfMonth();
        edat = anyActual - any;
        if (mesActual < mes) {
            edat--;
        } else if (mesActual == mes) {
            if (diaActual < dia) {
                edat--;
            }
        }
        return edat;
    }

    public void setNif(String nif) {
        this.nif = nif;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public void setDataNaixement(String dataNaixement) {
        this.dataNaixement = dataNaixement;
    }

    public String toString() {
        return nif + " : " + nom + " : " + edat;
    }

    public static int getNumPersones() {
        return numPersones;
    }

    public static void setNumPersones(int numPersones) {
        Persona.numPersones = numPersones;
    }

    private boolean comprovarNif(String nif) {
        boolean correcte = false;
        if (nif.length() == 9) {
            String numeros = nif.substring(0, 8);
            String lletra = nif.substring(8);
            if (numeros.matches("[0-9]+") && lletra.matches("[A-Z]")) {
                correcte = true;
            }
        }
        return correcte;
    }

    private boolean comprovarData(String dataNaixement) {
        boolean correcte = false;
        if (dataNaixement.length() == 10) {
            String[] data = dataNaixement.split("-");
            if (data.length == 3) {
                int dia = Integer.parseInt(data[0]);
                int mes = Integer.parseInt(data[1]);
                int any = Integer.parseInt(data[2]);
                if (dia >= 1 && dia <= 31 && mes >= 1 && mes <= 12 && any >= 1900 && any <= 2020) {
                    correcte = true;
                }
            }
        }
        return correcte;
    }

    class TestPersona {
        public static void main(String[] args) {
            Persona persona1 = creador("1A345678A", "Pere", "01-01-2000");
            Persona persona2 = creador("12345678A", "Pere", "01-01-2000");
            Persona persona3 = creador("12345678A", "Pere", "01-01-2000");
            System.out.println(persona1.getEdat());
            System.out.println(persona2.getEdat());
            System.out.println(Persona.getNumPersones());
        }

        public static Persona creador(String nif, String nom, String dataNaixement) {
            Persona persona = null;
            try {
                persona = new Persona(nif, nom, dataNaixement);
                numPersones++;
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
            return persona;
        }
    }
}

