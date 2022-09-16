/*Ex1*/
INSERT INTO empleats (empleat_id,nom, cognoms, email, data_contractacio, feina_codi, salari)
	VALUES (210,'Pere','Pi','perepi@gmail.com','2011-07-10','IT_PROG','7.000');

/*Ex2*/
INSERT INTO empleats (empleat_id,nom, cognoms, email, data_contractacio, feina_codi, salari)
          VALUES (211,'Sandra','González','sgonzalez@empresa.cat','2013-02-1','AD_VP','6.000'),
				 (212,'Marta','Pérez','mperez@empresa.cat','2013-04-15','IT_PROG','6.000'),
			     (213,'Maria','Cantó','mcantó@empresa.cat','2013-04-21','MK_REP','6.000');

/*Ex3*/
INSERT INTO empleats (empleat_id,nom, cognoms, email, data_contractacio, feina_codi, salari)
	VALUES (214,'Pau','Serra','pserra@empresa.cat','1992-01-15','IT_PROG','8.000');
INSERT INTO historial_feines (empleat_id,data_inici, data_fi, feina_codi, departament_id)
                VALUES 	(214,'1992-01-15','1993-09-20','IT_PROG',60),
						(214,'1993-09-21','1994-09-21','SA_REP',50),
						(214,'1994-09-21','1994-12-31','SA_MAN',50);
/*Ex4*/
INSERT INTO paisos(pais_id,nom,regio_id)
        VALUES ('ES','Espanya','1'),
                   ('FR','França','1'),
                   ('AU','Austràlia','5'),
                   ('JP','Japó','2'),
                   ('KR','Corea del Sud','2');

/*Ex5*/


/*Ex6*/


/*Ex7*/


/*Ex8*/
SELECT * FROM empleats;

/*Ex9*/
SELECT 	nom,
		cognoms,
        salari
	FROM empleats
    LIMIT 4;

/*Ex10*/
SELECT * FROM feines;

/*Ex11*/
SELECT DISTINCT departament_id
	FROM empleats;

/*Ex12*/
SELECT 	empleat_id,
		cognoms,
        nom,
        salari,
	TRUNCATE(salari*166.3860,1) as SalariPTS
	FROM empleats;

/*Ex13*/
SELECT 	cognoms,
		nom,
        salari
	FROM empleats
    WHERE salari > 12000;	

/*Ex14*/
SELECT * FROM paisos
	ORDER BY nom ASC;

/*Ex15*/
SELECT nom
	FROM paisos
    WHERE regio_id = 2;

/*Ex16*/
SELECT cognoms,
		empleat_id,
        departament_id,
        email
	FROM empleats
	WHERE empleat_id = 176;

/*Ex17*/
SELECT * FROM empleats
	WHERE data_contractacio >= 1996

