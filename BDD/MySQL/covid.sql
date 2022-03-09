/*2*/
SELECT sum(quantitat) as quantitat
	FROM casos 
    WHERE year(data) = 2021 and weekday(data) = 0;

/*3*/
SELECT tipus_cas_id, sum(quantitat) as casos
	FROM casos
    GROUP BY tipus_cas_id
    ORDER BY casos DESC;

/*4*/
SELECT min(length(nom)) as longitud
	FROM municipis;

/*5*/
SELECT count(codi) as quantitat
	FROM municipis
    WHERE left(codi,2) = 17;

/*6*/
SELECT 	centre_educatiu_id,nom_centre,sum(alumnes_positius_acum) as alumnes_positius
	FROM centres_educatius_casos c, centres_educatius e
    GROUP BY c.centre_educatiu_id;

/*7*/
SELECT denominacio as nom_centre
	FROM centres_educatius
    GROUP BY denominacio
    HAVING count(denominacio) >= 2
    ORDER BY nom_centre ASC;

/*8*/ 
SELECT centre_educatiu_id,docents_positius_acum,alumnes_positius_acum
	FROM centres_educatius_casos
    WHERE sum(docents_positius_acum) > sum(alumnes_positius_acum)
	GROUP BY centre_educatiu_id;
  
/*10*/
SELECT municipi_id, sum(quantitat) as casos
	FROM casos
    WHERE year(data) = 2021 
    GROUP BY municipi_id;
    
    

