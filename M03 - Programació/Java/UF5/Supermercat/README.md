Opció B (7 punts)

S'ha d'implementar les classes necessàries per gestionar un supermercat.
El disseny es troba en l'arxiu adjunt.

S'ha d'implementar la classe Supermercat que ha d'inclure els següents atributs i mètodes estàtics:

    Un array per guardar els productes.
    Mètode afegirProducte(Producte p)
    Mètode eliminarProducte(String n)
    Mètode filtrarProductes(String tipus)
    El tipus pot ser "Roba", "Aliment" o "Llibre" i s'ha de detectar mirant el nom de la classe de l'objecte.
    Ha de retornar un array amb tots els productes del tipus indicat.
    Mètode mostrarLlista(array l)
    Ha de mostrar les dades dels productes de la llista amb el format retornat pel mètode getInfo() de la classe corresponent.
    Mètode main() ha de:
        Crear i afegir uns quants productes de cada tipus.
        Eliminar un dels productes.
        Mostrar tota la roba.
        Mostrar tots els aliments.
        Mostrar tots els llibres.
        Comparar el preu de dos productes i dir quin és més gran (o més petit o igual).
        Tractar les excepcions mostrant el missatge corresponent.

Altres detalls a tenir en compte:

    S'han de documentar els mètodes de totes les classes, però no cal generar la documentació.
    Els atributs, mètodes i paràmetres han de ser els que hi ha en el disseny (si creus que has de crear algun altre mètode, pregunta al profe).
    El constructor de Producte ha de generar una excepció si el preu és inferior a 1.
    El IVA serà:
        Roba: 21%
        Aliments: 10% (21% si és una beguda)
        Llibres: 4%
    La talla de la roba només pot ser 'S', 'M' o 'L'.
    En cas contrari, el constructor ha de llençar una excepció.
    Les calories han de ser superiors a 0 i inferiors a 1000.
    En cas contrari, el constructor ha de llençar una excepció.
    El  mètode getInfo() ha de retornar un String per mostrar la informació en el següent format:
       Nom:      Samarreta
       Color:    Groc   
       Talla:    M
       PVP:      30.25 €

       Nom:      Patates
       Calories: 600
       PVP:      5.52 €

       Nom:      SuperFoods
       PVP:      15.84 €
    El PVP s'ha d'obtenir amb el mètode pvp()

Recorda utilitzar ArrayList a tot arreu on puguis i sigui necessari.