/*2*/

/*3*/
SELECT adreca as carrer, count(adreca) as quantitat
	FROM centres_educatius
    WHERE adreca REGEXP"," /*falta lo de diferents municipis*/ 
	GROUP BY adreca
    ORDER BY count(adreca) DESC;

/*4*/
SELECT (datediff(max(data_generacio),min(data_generacio)))/30 as mesos
	FROM centres_educatius_casos
    WHERE centre_educatiu_id = 5;

/*5*/
SELECT c.centre_educatiu_id,e.denominacio as nom_centre
	FROM centres_educatius e 
    INNER JOIN centres_educatius_casos c ON (e.centre_educatiu_id = c.centre_educatiu_id)
	WHERE c.docents_positius_acum > c.alumnes_positius_acum AND c.alumnes_positius_acum = 0
    GROUP BY c.centre_educatiu_id
    ORDER BY e.denominacio;

/*6*/
SELECT p.nom as provincia, sum(c.quantitat) as quantitat
	FROM casos c
		INNER JOIN municipis m ON (c.municipi_id=m.municipi_id)
		INNER JOIN comarques co ON (co.comarca_id=m.comarca_id)
		INNER JOIN provincies p ON (p.provincia_id=co.provincia_id)
	WHERE year(c.data) = 2020 and month(c.data) = 6 /*faltaria posar juliol i agost*/
    GROUP BY p.provincia_id
    ORDER BY p.nom;

/*7*/
SELECT co.nom as nom_comarca, sum(c.quantitat) as casos
	FROM casos c
		INNER JOIN municipis m ON (c.municipi_id=m.municipi_id)
		INNER JOIN comarques co ON (co.comarca_id=m.comarca_id)
	WHERE year(c.data) = 2020
    GROUP BY co.comarca_id
    HAVING casos < 1000
    ORDER BY casos;

/*8*/
SELECT denominacio REGEXP"Llar d'infants" as tipus_centre, count(denominacio) as quantitat
	FROM centres_educatius
    GROUP BY denominacio REGEXP"Llar d'infants";
    
/*9*/
SELECT m.nom as municipi, c.data
	FROM casos c
		INNER JOIN municipis m ON (m.municipi_id = c.municipi_id)
	GROUP BY c.municipi_id and c.data;
    
    
    