DROP DATABASE IF EXISTS bd_pp1_asix;

CREATE DATABASE IF NOT EXISTS bd_pp1_asix;

USE bd_pp1_asix;

CREATE TABLE municipis (
  municipi_id	SMALLINT UNSIGNED PRIMARY KEY,
  nom 			VARCHAR(20),
  codi_postal	CHAR(5)
 );
 
 INSERT INTO municipis(municipi_id,nom,codi_postal)
	VALUES 	(1,'Barcelona-Sants','08081')
			,(2,'Barcelona-Sants','08082')
            ,(3,'Girona','17001')
            ,(4,'Girona','17002')
            ,(5,'Banyoles','1782')
            ,(6,'Blanes','17300');

 CREATE TABLE concessionari (
  concessionari_id 	SMALLINT UNSIGNED NOT NULL PRIMARY KEY,
  municipi_id 		SMALLINT UNSIGNED NOT NULL,
  cif 				VARCHAR(10),
  nom				VARCHAR(20),
  CONSTRAINT cif UNIQUE (cif)
 );
 
 INSERT INTO concessionari(concessionari_id,municipi_id,cif,nom)
	VALUES	(1,1,'1222222','Automóviles Alpe'),
			(2,1,'11111111','Móvil Begar'),
            (3,1,'11232123','BMW Barna'),
            (4,6,'44554433','Fercar'),
            (5,5,'77323232','Motor Sport');
            
 CREATE TABLE models(
	model_id 	TINYINT  AUTO_INCREMENT PRIMARY KEY,
    marca_codi 	CHAR(15) NOT NULL,
    nom 		VARCHAR(20)
);

INSERT INTO models(model_id, marca_codi, nom)
	VALUES	(1,'BMW','BMWe34'),
			(2, 'BMW','BMWe46'),
            (3, 'SEAT','IBIZA');
 
 
 CREATE TABLE cotxes (
	cotxe_id 		TINYINT UNSIGNED PRIMARY KEY,
    model_id 		TINYINT,
    num_bastidor	VARCHAR(17),
    nom				VARCHAR(15),
    color			VARCHAR(10),
    CONSTRAINT fk_cotxes FOREIGN KEY (model_id)
		REFERENCES models(model_id)
 );
 
 INSERT INTO cotxes(cotxe_id,model_id,num_bastidor,nom,color)
	VALUES	(1,1,'454474AAFAF7464HF','BMWe34 diesel','VERMELL'),
			(2,1,'454654AAFAF7UR4HY','BMWe34 diesel','BLANC'),
            (3,2,'454654AAFA6FHEPHG','BMWe46 benzina','BLAU');
 
CREATE TABLE vendes (
	concessionari_id 	TINYINT NOT NULL,
	client_id 			TINYINT NOT NULL,
	cotxe_id 			TINYINT UNSIGNED NOT NULL,
	data_hora			DATETIME,
	preu				INT,
    CONSTRAINT fk_vendes_cotxes FOREIGN KEY (cotxe_id)
		REFERENCES cotxes(cotxe_id)
);
  
INSERT INTO vendes(concessionari_id,client_id,cotxe_id,data_hora,preu)
	VALUES 	(1,1,1,'2021-05-05 12:59:35',15000)
			,(1,1,2,'2021-06-05 15:59:35',35000);