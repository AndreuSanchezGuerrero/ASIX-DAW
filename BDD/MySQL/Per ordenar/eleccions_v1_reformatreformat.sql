
-- --
-- Autor: Pere Pi
-- Data: 15/05/2013
-- Descripció: Script per la creació de la base de dades d'eleccions
-- --
DROP DATABASE IF EXISTS eleccions_generals;

/* Creació de la BD eleccions */
/* Canviem utf8 per  utf8mb4 i utf8_general_ci per utf8mb4_0900_ai_ci*/
CREATE SCHEMA eleccions_generals DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

USE eleccions_generals;

/* Taula CIRCUMSCRIPCIONS */
CREATE TABLE eleccions_generals.circumscripcions (
  circumscripcio_id INT NOT NULL,
  nom VARCHAR(45) NULL,
  escons VARCHAR(45) NULL,
  provincia_id INT NOT NULL
);

/* Taula CANDIDATS */
CREATE TABLE eleccions_generals.candidats (
  candidat_id INT NULL,
  dni VARCHAR(50) NULL,
  nom VARCHAR(45) NULL,
  num_vegades VARCHAR(45) NULL COMMENT 'Nº de vegades que un candidat s\'ha presentat a les eleccions',
  partit_id INT UNSIGNED NOT NULL
);


/* Taula LLISTES */
CREATE TABLE eleccions_generals.llistes (
  llista_id INT NOT NULL,
  circumscripcio_id CHAR(10) NULL,
  partit_id VARCHAR(45) NULL
);

/* Taula PARTITS */
CREATE TABLE eleccions_generals.partits (
  partit_id BIGINT NOT NULL COMMENT 'Clau primària de la taula. Com a màxim tenim 50 partits diferents',
  nom VARCHAR(45) NULL,
  sigles VARCHAR(45) NULL,
  PRIMARY KEY (partit_id));

/* Taula PROVINCIES */
CREATE TABLE eleccions_generals.provincies (
  provincia_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nom VARCHAR(45) NULL,
  capital_nom VARCHAR(45) NULL COMMENT 'Nom de la captital de la província',
  comunitat_autonoma_nom VARCHAR(45) NULL,
  superficie VARCHAR(45) NULL,
  PRIMARY KEY (provincia_id)
);

/* Taula MUNICIPIS */
CREATE TABLE eleccions_generals.municipis (
  municipi_id INT NOT NULL AUTO_INCREMENT COMMENT 'Com a màxim tenim 9.000 municipis',
  nom VARCHAR(45) NOT NULL,
  nom1 VARCHAR(45) NULL COMMENT 'Nom de l\'alcalde',
  codi VARCHAR(45) NULL COMMENT 'Codi del municipi',
  alcalde_cognoms VARCHAR(45) NULL,
  num_habitants CHAR(45) NULL COMMENT 'El municipi més poblat té una quanitat de 4 milions i mig d\'habitants',
  provincia_id INT NOT NULL,
  PRIMARY KEY (municipi_id)
);


CREATE TABLE eleccions_generals.cens (
  cens_id INT NOT NULL COMMENT 'Com a màxim tenim un cents de 40 milions de ciutadants',
  dni VARCHAR(45) NULL,
  nom VARCHAR(45) NULL,
  cognoms VARCHAR(45) NULL,
  telefon VARCHAR(45) NULL,
  municipi_id VARCHAR(45) NULL COMMENT 'Municipi del qual el ciutadà hi està empadronat',
  mesa_electoral_id VARCHAR(45) NULL COMMENT 'Clau de la mesa electoral el cituadà ha d\'anar a votar.',
  PRIMARY KEY (cens_id)
);


INSERT INTO provincies (provincia_id,nom)
	VALUES(1,'Barcelona')
		,(2,'Girona')
        ,(4,'Lleida')
        ,(5,'Tarragona');
		
INSERT INTO circumscripcions (circumscripcio_id,nom,escons,provincia_id)
	VALUES(1,'BARCELONA',32,1)
		,(2,'GIRONA',6,2)
        ,(3,'LLEIDA',4,4)
        ,(4,'TARRAGONA',6,5);

INSERT INTO partits (partit_id,nom,sigles)
	VALUES(1,'PARTIT DEL MIG','PDM')
		,(2,'PARTIT DE MÉS ENLLÀ','PDME')
        ,(3,'PARTIT DE NO COMPLIR','PDNC')
        ,(4,'PARTIT COMPLIDOR','PC')
        ,(5,'PARTIT COMPLAENT','PCC');

INSERT INTO candidats(candidat_id,dni,nom,partit_id)
	VALUES (1,'111','Pere Pi',1)
			,(2,'222','Sandra Llens',1)
            ,(3,'333','Lidia Parra',3)
            ,(4,'444','Joan Delmas',3);

INSERT INTO municipis(municipi_id,nom,provincia_id, codi)
	VALUES (1,'Blanes',2,'001')
			,(2,'Girona',2,'002')
            ,(3,'Lloret de Mar',2,'003')
            ,(4,'Lleida',4,'004')
            ,(5,'Tarragona',5,'005')
            ,(6,'Reus',5,'006');