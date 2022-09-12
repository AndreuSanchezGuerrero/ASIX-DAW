   
/*Correció del model_id per a ferlo unsigned i mes gran*/
ALTER TABLE cotxes
	DROP FOREIGN KEY fk_cotxes,
	MODIFY COLUMN model_id SMALLINT UNSIGNED NOT NULL;

/*Correció taula model per donar nom a la pk i continuació model_id*/
ALTER TABLE models
	DROP PRIMARY KEY,
    MODIFY COLUMN model_id SMALLINT UNSIGNED AUTO_INCREMENT,
	ADD CONSTRAINT pk_models PRIMARY KEY(model_id);
ALTER TABLE cotxes
	ADD CONSTRAINT fk_cotxes_model_id FOREIGN KEY(model_id)
		REFERENCES models(model_id);

/*cotxes_cotxe_id posar nom pk i es auto_increment*/
ALTER TABLE vendes
	DROP FOREIGN KEY fk_vendes_cotxes,
    MODIFY COLUMN cotxe_id INT UNSIGNED;
ALTER TABLE cotxes
	DROP PRIMARY KEY,
	MODIFY COLUMN cotxe_id INT UNSIGNED AUTO_INCREMENT,
    ADD CONSTRAINT pk_cotxes_cotxe_id PRIMARY KEY(cotxe_id);
ALTER TABLE vendes
	ADD CONSTRAINT fk_vendes_cotxes FOREIGN KEY (cotxe_id)
		REFERENCES cotxes(cotxe_id);
        
/*taula cotxes correcions*/
ALTER TABLE cotxes
	MODIFY COLUMN nom VARCHAR(25) NOT NULL,
    MODIFY COLUMN color ENUM("BLANC","VERMELL","BLAU"),
    ADD CONSTRAINT uk_num_bastidot UNIQUE(num_bastidor);
    
/*TAula clients*/
CREATE TABLE clients(
	client_id 	SMALLINT UNSIGNED AUTO_INCREMENT,
    municipi_id	SMALLINT UNSIGNED,
    dni			CHAR(10) COMMENT "9 dígits i 1 caràcter",
    nom			VARCHAR(12) NOT NULL,
    cognom1		VARCHAR(15) NOT NULL,
    cognom2		VARCHAR(15),
    CONSTRAINT pk_clients PRIMARY KEY(client_id),
    CONSTRAINT uk_clients_dni UNIQUE(dni),
    CONSTRAINT fk_clients_municipi_id FOREIGN KEY(municipi_id)
		REFERENCES municipis(municipi_id)
    );

INSERT INTO clients(client_id,municipi_id,dni,nom,cognom1)
	VALUES (1,6,"456789876N","NIL","MASSÓ");
    
/*Correcions concessionari*/
ALTER TABLE concessionari /*/S'ha de canviar el nom de la taula a plural pero no recordo com*/
	DROP PRIMARY KEY,
    MODIFY COLUMN concessionari_id TINYINT UNSIGNED AUTO_INCREMENT,
    MODIFY COLUMN municipi_id SMALLINT UNSIGNED,
    MODIFY COLUMN cif VARCHAR(10) NOT NULL,
    MODIFY COLUMN nom VARCHAR(20) NOT NULL,
    ADD CONSTRAINT pk_concecionaris PRIMARY KEY(concessionari_id),
    ADD CONSTRAINT uk_concessionaris_cif UNIQUE(cif),
    ADD CONSTRAINT fk_concessionaris_municipi_id FOREIGN KEY(municipi_id)
		REFERENCES municipis(municipi_id);

/*Correcions vendes*/        
ALTER TABLE vendes
	MODIFY COLUMN concessionari_id INT UNSIGNED,
    MODIFY COLUMN client_id SMALLINT UNSIGNED,
    DROP FOREIGN KEY fk_vendes_cotxes,
    MODIFY COLUMN cotxe_id INT UNSIGNED,
    CHANGE COLUMN data_hora data DATE NOT NULL,
    MODIFY COLUMN preu FLOAT(8,3),
	ADD CONSTRAINT fk_vendes_client_id FOREIGN KEY(client_id)
		REFERENCES clients(client_id),
	ADD CONSTRAINT fk_vendes_cotxe_id FOREIGN KEY(cotxe_id)
		 REFERENCES cotxes(cotxe_id),
	ADD CONSTRAINT pk_vendes PRIMARY KEY(concessionari_id,client_id,cotxe_id);
         
         
    
	