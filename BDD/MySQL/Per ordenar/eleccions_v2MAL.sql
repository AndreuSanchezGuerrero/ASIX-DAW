
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
  circumscripcio_id INT UNSIGNED AUTO_INCREMENT,
  nom 				VARCHAR(25) NOT NULL,
  escons			SMALLINT UNSIGNED NOT NULL,
  provincia_id 		INT UNSIGNED,
  
  CONSTRAINT pk_circumscripcions PRIMARY KEY(circumscripcio_id),
  CONSTRAINT fk_circumscripcions_provincies FOREIGN KEY(provincia_id)
	REFERENCES provincies (provincia_id),
  CONSTRAINT ck_circumscripcions_escons CHECK(escons >1 AND escons<350),
  CONSTRAINT ck_circumscripcions_circumscripcio_id CHECK(circumscripcio_id <52)
);

/* Taula CANDIDATS */
CREATE TABLE eleccions_generals.candidats (
  candidat_id 	SMALLINT UNSIGNED AUTO_INCREMENT,
  dni 			CHAR(9),
  nom 			VARCHAR(45),
  num_vegades 	TINYINT UNSIGNED COMMENT 'Nº de vegades que un candidat s\'ha presentat a les eleccions',
  partit_id 	SMALLINT UNSIGNED NOT NULL,
  
  CONSTRAINT pk_candidats PRIMARY KEY(candidat_id),
  CONSTRAINT fk_candidats_parits FOREIGN KEY(partits_id)
	REFERENCES partits (partits_id)
);


/* Taula LLISTES */
CREATE TABLE eleccions_generals.llistes (
  llista_id 			SMALLINT NOT NULL,
  circumscripcio_id 	CHAR(10),
  partit_id 			SMALLINT NOT NULL,
  
  CONSTRAINT pk_llistes PRIMARY KEY(llista_id,circumscripcio_id,partit_id),
  CONSTRAINT fk_llistes_circumscripcions FOREIGN KEY(circumscripcio_id)
	REFERENCES circumscripcions (circumscripcio_id),
  CONSTRAINT fk_llistes_partits FOREIGN KEY (partit_id)
	REFERENCES partits (partit_id)
);

/* Taula PARTITS */
CREATE TABLE eleccions_generals.partits (
  partit_id 	TINYINT UNSIGNED COMMENT 'Clau primària de la taula. Com a màxim tenim 50 partits diferents',
  nom 			VARCHAR(45),
  sigles 		VARCHAR(8),
  
  CONSTRAINT pk_partits PRIMARY KEY(partit_id)
  );

/* Taula PROVINCIES */
CREATE TABLE eleccions_generals.provincies (
  provincia_id 				TINYINT UNSIGNED AUTO_INCREMENT,
  nom 						VARCHAR(45),
  capital_nom 				VARCHAR(45) COMMENT 'Nom de la captital de la província',
  comunitat_autonoma_nom 	VARCHAR(45),
  superficie 				VARCHAR(20),
  CONSTRAINT pk_provincies PRIMARY KEY (provincia_id)
);

/* Taula MUNICIPIS */
CREATE TABLE eleccions_generals.municipis (
  municipi_id 		SMALLINT UNSIGNED AUTO_INCREMENT COMMENT 'Com a màxim tenim 9.000 municipis',
  nom 				VARCHAR(30) NOT NULL,
  codi 				CHAR(4) COMMENT 'Codi del municipi',
  alcalde_nom 		VARCHAR(20) COMMENT 'Nom de l\'alcalde',
  alcalde_cognoms 	VARCHAR(45),
  num_habitants 	MEDIUMINT COMMENT 'El municipi més poblat té una quanitat de 4 milions i mig d\'habitants',
  provincia_id 		SMALLINT NOT NULL,
  CONSTRAINT pk_municipis PRIMARY KEY (municipi_id),
  CONSTRAINT fk_municipis_provincies FOREIGN KEY (provincia_id)
	REFERENCES provincies (provincia_id)
);


CREATE TABLE eleccions_generals.cens (
  cens_id 			INT UNSIGNED COMMENT 'Com a màxim tenim un cents de 40 milions de ciutadants',
  dni 				CHAR(9),
  nom 				VARCHAR(45),
  cognoms 			VARCHAR(45),
  telefon 			CHAR(9) COMMENT 'es podria posar un int pero aixi m\'asseguro de q posin un num valid',
  municipi_id 		SMALLINT UNSIGNED AUTO_INCREMENT COMMENT 'Municipi del qual el ciutadà hi està empadronat',
  mesa_electoral_id INT UNSIGNED COMMENT 'Clau de la mesa electoral el cituadà ha d\'anar a votar.',
  PRIMARY KEY (cens_id)
);


INSERT INTO provincies (provincia_id,nom)
	VALUES	(1,'Barcelona'),
			(2,'Girona'),
			(4,'Lleida'),
			(5,'Tarragona');
		
INSERT INTO circumscripcions (nom,escons,provincia_id)
	VALUES	('BARCELONA',32,1),
			('GIRONA',6,2),
			('LLEIDA',4,4),
			('TARRAGONA',6,5);

INSERT INTO partits (nom,sigles)
	VALUES	('PARTIT DEL MIG','PDM'),
			('PARTIT DE MÉS ENLLÀ','PDME'),
			('PARTIT DE NO COMPLIR','PDNC'),
			('PARTIT COMPLIDOR','PC'),
			('PARTIT COMPLAENT','PCC');

INSERT INTO candidats(dni,nom,partit_id)
	VALUES 	('11111111A','Pere Pi',1),
			('22222222B','Sandra Llens',1),
            ('33333333C','Lidia Parra',3),
            ('44444444D','Joan Delmas',3);

INSERT INTO municipis(nom,provincia_id, codi)
	VALUES 	('Blanes',2,'0001'),
			('Girona',2,'0002'),
            ('Lloret de Mar',2,'0003'),
            ('Lleida',4,'0004'),
            ('Tarragona',5,'0005'),
            ('Reus',5,'0006');