/*Realitza un rànquing de quanitat d'hotels per població.

    Ordena el resultat per la quanitat d'hotels de més a menys. Si hi ha poblacions amb el mateix número d'hotels ordena per nom de la població de forma ASC.

+--------------------------+-----------+
| poblacio                 | quantitat |
+--------------------------+-----------+*/

SELECT p.nom as poblacio, count(h.poblacio_id) as quantitat
FROM hotels h
    INNER JOIN poblacions p ON (h.poblacio_id = p.poblacio_id)
    GROUP BY p.poblacio_id
    ORDER BY quantitat DESC, p.nom ASC;

/*Mostra els clients que els hi coincideix el dia de naixement amb el mes.

    Mostra el nom, el primer cognom i la data de naixment.
    Ordena el resultat per client_id

+--------+---------+------------+
| nom    | cognom1 | data_naix  |
+--------+---------+------------+*/

SELECT nom, cognom1, data_naix
FROM clients
WHERE month(data_naix) = day(data_naix)
order by client_id;

/*S'han detectat errors a la BD. No pot ser que hi hagin reserves sense cap nit. Busca aquestes reserves i digues quantes n'hi ha

+---------+
| quantes |
+---------+*/

SELECT count(*) as quantes
FROM reserves
WHERE data_inici = data_fi;

/*Volem premiar els clients fidels. Entenem com a client fidel aquell que ha realitzat alguna reserva durant els anys 2014, 2015 i 2016 de forma consecutiva.

    Tingues en compte que una reserva pertany a un any si la seva data_inici hi pertany.
    No cal que els clients repeteixin hotel.
    Tampoc cal que repteixin quantitat de reserves. És a dir, si hi ha un client va fer 3 reserves l'any 204 no cal que el 2015 i el 2016 hagi hagut de fer 3 reserves. Tan sols que en tingui una ja es suficient per considerar-lo com a fidel.
    Ordena el resultat per client_id

+-----------+--------+---------+
| client_id | nom    | cognom1 |
+-----------+--------+---------+*/

SELECT c.client_id, c.nom, c.cognom1
FROM clients c
    INNER JOIN reserves r ON (r.client_id = c.client_id)
    WHERE year(r.data_inici) = 2014
        OR year(r.data_inici) = 2015
        OR year(r.data_inici) = 2016
    GROUP BY  r.client_id
    HAVING count(*) > 1
    ORDER BY c.client_id;

/*Quantes reserves va rebre l’hotel ‘Catalonia Ramblas’ de Barcelona durant tot l’any 2015?

    No pots fer servir els Ids de les taules.
    Una reserva pertany a l'any si la seva data d'inici hi pertany.

+--------------+
| num_reserves |
+--------------+*/

SELECT count(*) as num_reserves
FROM reserves r
INNER JOIN habitacions h ON (r.hab_id = h.hab_id)
INNER JOIN hotels ht ON (h.hotel_id = ht.hotel_id)
WHERE ht.nom = 'Catalonia Ramblas'
    AND year(r.data_inici) = 2015;

/*S'han detectat errors a la BD. No pot ser que hi hagin reserves sense cap nit. Busca aquestes reserves i mostra-les

    Mostra l'identificador de la reserva, la data d'inici i la data de fi
    Ordena el resultat per identificador de la reserva

+------------+------------+------------+
| reserva_id | data_inici | data_fi    |
+------------+------------+------------+*/

SELECT reserva_id, data_inici, data_fi
FROM reserves
WHERE data_inici = data_fi
ORDER BY reserva_id;

/*Quants mesos té la reserva més curta de la BD?

Expressa el resultat en mesos i arrodonint el resultat a 0 decimals

+-------+
| mesos |
+-------+*/

SELECT min(round(DATEDIFF(data_fi, data_inici), 0)) as mesos  
FROM reserves

/*De l'Hotel 'Catalonia Ramblas' de Barcelona mostra la quantitat de nits disponibles (teòriques) que tindria l'hotel per cada mes de l'any 2016

    Ordena per número de mes de forma ascendent

+------+------+
| mes  | nits |
+------+------+
|    1 |   ? |
|    2 |   ? |
|    3 |   ? |
+------+------+
...
|   11 |   ? |
|   12 |   ? |

+------+------+*/

SELECT month(data_inici) as mes, count(*) as nits
FROM reserves r
INNER JOIN habitacions h ON (r.hab_id = h.hab_id)
INNER JOIN hotels ht ON (h.hotel_id = ht.hotel_id)
WHERE ht.nom = 'Catalonia Ramblas'
    AND year(r.data_inici) = 2016
GROUP BY month(data_inici)
ORDER BY month(data_inici);