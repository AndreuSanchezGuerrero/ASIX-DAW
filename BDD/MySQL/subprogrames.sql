/*Esquema
DROP FUNCTION IF EXISTS nom:
DELIMITER //
CREATE FUNCTION nom(arg INT) RETURNS INT
DETERMINISTIC
BEGIN

RETURN ;
END
//
*/
/*1*/
DROP FUNCTION IF EXISTS spData;
DELIMITER //
CREATE FUNCTION spData(pdata DATE) RETURNS VARCHAR(10)
	NOT DETERMINISTIC READS SQL DATA
BEGIN 
	DECLARE vRetorn VARCHAR(10) DEFAULT NULL;
	SET vRetorn = date_format(pdata,"%d-%m-%Y");
    RETURN vRetorn;
END
//
    
SELECT spData('1988-12-01')//

/*2 (esta malament)*/
DROP FUNCTION IF EXISTS spPotencia//
DELIMITER //
CREATE FUNCTION spPotencia(pb INT,pe INT) RETURNS BIGINT
DETERMINISTIC
BEGIN 
	DECLARE r BIGINT DEFAULT NULL;
    LOOP
    IF pe > 1 THEN
		SET r := pb*pb;
	END IF;
    END LOOP;
    RETURN r;
END
//
    
SELECT spPotencia(2,5)//

/*3*/
DROP FUNCTION IF EXISTS nom:
DELIMITER //
CREATE FUNCTION nom(arg INT) RETURNS INT
DETERMINISTIC
BEGIN

RETURN ;
END
//
/**/



#Procediments
#Esquema
DELIMITER //
DROP PROCEDURE IF EXISTS nom//
CREATE PROCEDURE nom([def_param[,def_param]]) 
BEGIN


END
//
#1
DROP PROCEDURE IF EXISTS spdatauser//
DELIMITER //
CREATE PROCEDURE spDatauser(OUT pDatahora DATETIME,OUT puser VARCHAR(20)) 
BEGIN
DECLARE puser VARCHAR(20);
DECLARE pDatahora DATETIME;
SET pDatahora = now();
SET puser = CURRENT_USER;

END
//
set pDatahora = "a";
set puser = "b";
CALL spDatauser(pDatahora,puser);

#3
DELIMITER //
DROP PROCEDURE IF EXISTS spChange//
CREATE PROCEDURE spChange(IN pEmpleat1 INT, IN pEmpleat2 INT) 
BEGIN
DECLARE pIntercanvi INT;
SELECT departament_id INTO pIntercanvi
	FROM empleats
    WHERE empleat_id = pEmpleat1;
UPDATE empleats SET departament_id = pIntercanvi
WHERE empleat_id = pEmpleat2;
END
//
CALL spChange(100,107);

#4
DELIMITER //
DROP PROCEDURE IF EXISTS spChangeDep//
CREATE PROCEDURE spChangeDep(IN pDep1 INT, IN pDep2 INT) 
BEGIN
UPDATE empleats SET departament_id = pdep1
WHERE departament_id = pdep2;
END
//
CALL spCdep(90,60);

#5
DELIMITER //
DROP PROCEDURE IF EXISTS spLempleats//
CREATE PROCEDURE spLempleats() 
BEGIN
SELECT (e.empleat_id, e.nom, d.nom, d.localitzacio_id)
	FROM empleats e
		INNER JOIN departaments d;
END
//
CALL spLempleats;

/*6*/
DROP PROCEDURE IF EXISTS sp_info_empleats;
DELIMITER //
CREATE PROCEDURE sp_info_empleats(	IN pEmp_Id INT, 
									OUT pNom VARCHAR(30),
                                    OUT pCognoms VARCHAR(30), 
                                    OUT pSalari DECIMAL(8,2), 
                                    OUT pDep_id INT)
BEGIN
	SELECT e.nom, e.cognoms, e.salari, e.departament_id 
			INTO pNom,pCognoms,pSalari,pDep_id
			FROM empleats e
			WHERE empleat_id = pEmp_Id;
END
//
SET @nom = 0;
SET @cognom = 0;
SET @salari = 0;
SET @dep = 0;
CALL sp_info_empleats(202,@nom,@cognom,@salari,@dep);
SELECT @nom, @cognom, @salari, @dep;

/*9*/
DROP PROCEDURE IF EXISTS spAfegirDepartament;
DELIMITER //
CREATE PROCEDURE spAfegirDepartament(IN pDepId INT
									, IN pDepNom VARCHAR(30)
                                    , IN pLocId INT)
BEGIN
    
    IF NOT pLocId IN (SELECT localitzacio_id
							FROM localitzacions
							WHERE localitzacio_id = pLocId) THEN
	SET pLocId = NULL;
	END IF;
    
    INSERT INTO departaments(departament_id,nom,localitzacio_id)
                VALUES(pDepId,pDepNom,pLocId);
END
//

#12
DELIMITER //
DROP TABLE IF EXISTS logs_usuaris//

CREATE TABLE logs_usuaris(
	usuari VARCHAR(100),
    data DATETIME,
    taula VARCHAR(50),
    accio VARCHAR(20),
    valor_pk VARCHAR(200),
    error INT(4)
)//

DROP PROCEDURE IF EXISTS spRegistrarLog//
CREATE PROCEDURE spRegistrarLog(IN spNomTaula VARCHAR(50), IN spAccio VARCHAR(20), IN spValor_pk VARCHAR(200))
BEGIN
	INSERT INTO logs_usuaris(usuari, data, taula, accio, valor_pk)
		VALUES (CURRENT_USER,CURRENT_DATE,spNomTaula,spAccio,spValor_pk);
END
//

#
DELIMITER //
DROP PROCEDURE IF EXISTS spInfoCount//
CREATE PROCEDURE spInfoCount(OUT pNumEmpleats INT UNSIGNED,
								OUT pNumDepartaments INT UNSIGNED,
                                OUT pNumLocalitzacions INT UNSIGNED) 
BEGIN
	SELECT COUNT(*) INTO pNumEmpleats
		FROM empleats;
        
	SELECT COUNT(*) INTO pNumDepartaments
		FROM empleats;
        
	SELECT COUNT(*) INTO pNumLocalitzacions
		FROM empleats;
END
//






