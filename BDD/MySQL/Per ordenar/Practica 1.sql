ALTER TABLE circumscipcions
	MODIFY COLUMN circumscipcions_id TINYINT(52) UNSIGNED,
    MODIFY COLUMN nom VARCHAR(25) NOT NULL,
    MODIFY COLUMN escons SMALLINT CHECK (1<350) NOT NULL,
    MODIFY COLUMN provincia_id INT UNSIGNED NOT NULL,
    ADD CONSTRAINT PK_circumscipcions PRIMARY KEY (circumscipcions_id),
    ADD CONSTRAINT FK_provincia_id FOREIGN KEY (provincia_id)
    REFERENCES provincies (provincia_id);
    
ALTER TABLE provincies 
	MODIFY COLUMN provincia_id INT UNSIGNED,
    MODIFY COLUMN nom VARCHAR(25) NOT NULL,
    CHANGE COLUMN capital_nom capital VARCHAR(20),
    CHANGE COLUMN comunitat_autonoma_nom com_autonoma VARCHAR(20),
    MODIFY COLUMN superficie DECIMAL,
    ADD CONSTRAINT PK_provincia_id PRIMARY KEY (provincia_id);

ALTER TABLE candidats
	MODIFY COLUMN candidat_id INT UNSIGNED,
    MODIFY COLUMN dni CHAR(10),
    MODIFY COLUMN nom VARCHAR(25) NOT NULL,
    MODIFY COLUMN num_vegades INT UNSIGNED DEFAULT "0",
    MODIFY COLUMN partit_id INT UNSIGNED,
    ADD COLUMN num_llista INT UNSIGNED,
    ADD COLUMN num_ordre INT UNSIGNED,
    ADD CONSTRAINT PK_candidad_id PRIMARY KEY (candidat_id),
    ADD CONSTRAINT FK_partit_id FOREIGN KEY (partit_id)
    REFERENCES llistes,
    ADD CONSTRAINT FK_num_llista FOREIGN KEY (num_llista)
    REFERENCES llistes;
    
ALTER TABLE llistes
	MODIFY COLUMN partit_id INT UNSIGNED,
    MODIFY COLUMN circumscripcio_id INT UNSIGNED,
    CHANGE COLUMN llista_id num_llista INT UNSIGNED AUTO_INCREMENT,
    ADD CONSTRAINT PK_partit_id 
	ADD CONSTRAINT PK_num_llista
    
    

#- prohibit fer drops
#- no usar create tables, nomes alter tables
#- no ficar check a les pk
