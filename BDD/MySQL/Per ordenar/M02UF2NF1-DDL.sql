CREATE DATABASE exercicis_ddl1;

CREATE TABLE jugadors (
jugador_id 	INT UNSIGNED,
nom 		VARCHAR(25) NOT NULL,
cognom1 	VARCHAR(30) NOT NULL,
cognom2 	VARCHAR(30) NOT NULL,
posició 	ENUM('BASE','ALER','ALER-PIVOT','PIVOT') NOT NULL,
dorsal 		TINYINT UNSIGNED,
punts 		SMALLINT UNSIGNED,
valoracio 	TINYINT UNSIGNED,

CONSTRAINT pk_jugadors PRIMARY KEY(jugador_id),
CONSTRAINT ck_jugadors_dorsal CHECK(dorsal<=100),
CONSTRAINT ck_jugadors_punts CHECK(punts<=300),
CONSTRAINT ck_jugadors_valoracio CHECK(valoracio<=10) 
);

CREATE TABLE factures (
numero 	INT UNSIGNED,
serie 	CHAR(3),
data 	DATE,
any 	YEAR,
client_id INT UNSIGNED NOT NULL,
CONSTRAINT pk_factures PRIMARY KEY(numero,serie,any),
CONSTRAINT ck_factures_client_id CHECK(client_id <= 5000)
);

CREATE TABLE linies_factura(
numero			INT UNSIGNED,
serie			CHAR(3),
any				YEAR,			
linia			INT,
producte_id		SMALLINT UNSIGNED NOT NULL,
qt				SMALLINT UNSIGNED NOT NULL,
import			FLOAT NOT NULL,
descompte		FLOAT,
subtotal		FLOAT GENERATED ALWAYS AS (qt*import*(1 - descompte)),
CONSTRAINT pk_linies_factura PRIMARY KEY(numero, serie, any, linia),
CONSTRAINT fk_linies_factura_factures FOREIGN KEY(numero,serie,any)
	REFERENCES factures(numero,serie,any)
);

CREATE TABLE productes (
nom 			VARCHAR(30),
producte_id 	SMALLINT UNSIGNED,
CONSTRAINT pk_productes PRIMARY KEY (producte_id)
);

CREATE TABLE persones(
persona_id 	INT UNSIGNED,
nom			VARCHAR(30),
cognom		VARCHAR(45),
CONSTRAINT pk_persones PRIMARY KEY(persona_id)
);

CREATE TABLE clients(
client_id	SMALLINT UNSIGNED,
dni			CHAR(10) UNIQUE, 
nom			VARCHAR(15) NOT NULL,
CONSTRAINT pk_clients PRIMARY KEY(client_id)
);

CREATE TABLE pobles(
poble_id		INT,
municipi_id		INT,
nom				VARCHAR(40), 
provincia_nom	VARCHAR(14) NOT NULL DEFAULT '',
CONSTRAINT pk_pobles PRIMARY KEY(poble_id,municipi_id)
);

ALTER TABLE jugadors
	ADD COLUMN dni CHAR(9)
		AFTER jugador_id,
	ADD CONSTRAINT uk_jugadors_dni UNIQUE (dni);

#Ex 8
ALTER TABLE linies_factura
    DROP FOREIGN KEY FK_linies_factura_factures;
ALTER TABLE linies_factura
    ADD  CONSTRAINT fk_linies_factura_factures FOREIGN KEY (numero,serie,any) 
		REFERENCES factures (numero,serie,any)  ON DELETE CASCADE ON UPDATE CASCADE;

#Ex9
#Error Code: 3780. Referencing column 'producte_id' and referenced column 'producte_id' in foreign key constraint 'fk_linies_factura_productes' are incompatible.
ALTER TABLE linies_factura
    MODIFY COLUMN producte_id     TINYINT UNSIGNED,
    ADD CONSTRAINT FK_linies_factures_productes FOREIGN KEY (producte_id)
        REFERENCES productes (producte_id);

#Ex10
ALTER TABLE linies_factura
	ADD CONSTRAINT FK_linies_factures_productes FOREIGN KEY (producte_id)
        REFERENCES productes (producte_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE;

#Ex11
ALTER TABLE jugadors 
	ADD COLUMN cognoms VARCHAR(65) GENERATED ALWAYS AS (cognom1+" "+cognom2) STORED NOT NULL
		AFTER cognom2;

#Ex12
ALTER TABLE factures RENAME factura;

#Ex13
CREATE TABLE proveidors LIKE clients;

#Ex14
CREATE TABLE feines(
feina_id	TINYINT UNSIGNED AUTO_INCREMENT,
nom			VARCHAR(25) NOT NULL DEFAULT "",
salari_min 	FLOAT DEFAULT 0,
salari_max	FLOAT DEFAULT 8000,
CONSTRAINT pk_feines PRIMARY KEY (feina_id)
);

#Ex15
ALTER TABLE jugadors
	ADD CONSTRAINT ck_jugadors_max CHECK (jugador_id <= 65000);

#Ex16
ALTER TABLE clients
	ADD COLUMN poble_id INT,
	ADD CONSTRAINT fk_clients_poble_id FOREIGN KEY (poble_id)
		REFERENCES pobles (poble_id);

#Ex17
ALTER TABLE jugadors
	ADD CONSTRAINT uk_jugadors_dni UNIQUE (dni);

#Ex18
ALTER TABLE jugadors
	DROP dorsal;

#Ex19
ALTER TABLE clients
	DROP FOREIGN KEY fk_clients_poble_id,
	DROP COLUMN poble_id;

#Ex20
ALTER TABLE clients
	DROP FOREIGN KEY fk_clients_poble_id,
	DROP COLUMN poble_id;

#Ex21
CREATE VIEW v_max_anotadors (jugador_id,nom,punts) AS
	SELECT jugador_id, nom, punts
	FROM jugadors
    ORDER BY punts DESC
    LIMIT 10;

#Ex22
CREATE VIEW v_jugadors_10p (jugador_id,nom,punts) AS
	SELECT jugador_id, nom, punts
	FROM jugadors
    WHERE punts > 10
    WITH CHECK OPTION;

#Ex23
CREATE INDEX idx_nom_cognom1
	USING BTREE
    ON jugadors (nom,cognom1);

#Ex24
CREATE INDEX idx_punts
	USING HASH
    ON jugadors(punts);

#Ex25
ALTER TABLE linies_factura
	DROP FOREIGN KEY FK_linies_factures_productes;
ALTER TABLE productes
	MODIFY COLUMN producte_id TINYINT UNSIGNED AUTO_INCREMENT;
ALTER TABLE linies_factura
	ADD CONSTRAINT FK_linies_factures_productes FOREIGN KEY (producte_id)
        REFERENCES productes (producte_id);






