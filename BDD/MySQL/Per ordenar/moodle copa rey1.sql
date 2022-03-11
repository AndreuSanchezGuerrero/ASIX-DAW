SELECT DISTINCT lloc_naixement 
	FROM jugadors 
	WHERE lloc_naixement LIKE "B%"
    ORDER BY lloc_naixement ASC;
    
SELECT nom_complet
	FROM jugadors
    WHERE pes IS NOT NULL
    ORDER BY nom_complet ASC;

SELECT COUNT(partit_id) AS quantitat
	FROM partits
    WHERE MONTH(data_hora) = 3;
    
SELECT nom_complet
	FROM jugadors
    WHERE pes IS NULL
    ORDER BY nom_complet ASC;
    
SELECT nom_complet
	FROM jugadors
    WHERE twitter COLLATE utf8mb4_0900_as_cs LIKE "@P%"
    ORDER BY nom_complet ASC;
	
UPDATE jugadors
	SET cognoms = LEFT(nom_complet,INSTR(nom_complet,",")-1);
    
SELECT nom_complet
	FROM jugadors
    WHERE cognoms  max(length(cognoms));

SELECT nom
	FROM competicions
    ORDER BY data_inici ASC;
    
SELECT count(partit_id) AS quantitat
	FROM partits
    WHERE year(data_hora) = 2017;
    
SELECT count(nom_complet) AS quants
	FROM jugadors
    WHERE nom_complet REGEXP "[aeiou]{3,}";
    
SELECT count(nom_complet) AS qt_desembre
	FROM jugadors
    WHERE month(data_naixement) = 12;

SELECT nom_complet
	FROM jugadors
    WHERE twitter IS NULL
    ORDER BY nom_complet ASC;

SELECT nom 
	FROM clubs
    WHERE web IS NULL;
		
SELECT nom_complet, ROUND(ifnull(pes,70)/power(ifnull(alcada,1.90),2),2) AS IMC
	FROM jugadors
    WHERE jugador_id IN (101,135);

SELECT nom_complet
	FROM jugadors
    WHERE instr(nom_complet,",") = ANY
									(SELECT max(instr(nom_complet,","))
										FROM jugadors);