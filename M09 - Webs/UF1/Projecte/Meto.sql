'''
S’ha de realitzar una aplicació amb PHP que mostri les dades que s’obtenen de la estació
Meteorològica, pel projecte Temperatura i humitat de l’aire. (les dades de la BDD les haureu d’afegir vosaltres...)

A la pantalla s’haurà de mostrar:
Darrera temperatura registrada (es mostraran només si cliquem el botó que es determini)
Darrera humitat de l’aire registrada (es mostraran només si cliquem el botó que es determini)
Temperatura més alta i més baixa registrada al dia actual.
La Humitat relativa mitjana del dia actual. 
Temperatura més alta i més baixa registrada a l’any actual.

Es valorarà la representació “elegant” de les dades dins la pàgina...
Es valorarà si hi ha més informació mostrada de la estrictament demanada.
S’ha de fer una demo/presentació del treball realitzat.
'''

#Creem la base de dades
CREATE DATABASE meteo;
USE meteo;

#Creem la taula
CREATE TABLE meteo (
  id INT NOT NULL AUTO_INCREMENT,
  temperatura FLOAT NOT NULL,
  humitat FLOAT NOT NULL,
  data TIMESTAMP NOT NULL,
  PRIMARY KEY (id)
);

#Afegim dades desde una web

