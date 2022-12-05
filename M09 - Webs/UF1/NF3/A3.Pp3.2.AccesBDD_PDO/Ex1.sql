-- SQLBook: Code
/*
Exercici 1: (1.0p) Crea una base de dades per tal de poder “guardar” les dades que obtenim de les incidències que hem treballant en una activitat anterior. ALERTA amb els valors amb els que l’has de crear: (El servidor localhost, el nom de la BDD ha de ser incidencies, l’usuari user i el password aplicacions. (Recorda que es necessari l’script generat afegit a l’entrega)

		Id: (enter) 
		Dispositiu: (string)


		Data: (string)-> Date() 
		Sol·licitat (String)
		Correu Sol·licitant (String)
		Descripció de la incidència
*/
CREATE DATABASE incidencies;
USE incidencies;
CREATE TABLE incidencies(
    id INT NOT NULL,
    dispositiu VARCHAR(255) NOT NULL,
    data VARCHAR(255) NOT NULL,
    solicitat VARCHAR(255) NOT NULL,
    correu VARCHAR(255) NOT NULL,
    descripcio VARCHAR(255) NOT NULL
);

#Insertem una entrada de prova
INSERT INTO incidencies (id, dispositiu, data, solicitat, correu, descripcio) VALUES (1, 'PC', '2020-01-01', 'Joan', '', 'No funciona');

