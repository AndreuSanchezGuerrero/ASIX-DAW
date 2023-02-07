1 - Classe Persona

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
