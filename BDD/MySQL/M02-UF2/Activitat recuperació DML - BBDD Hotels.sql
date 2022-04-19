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
    INNER JOIN reserves r ON (c.client_id = r.client_id)
    WHERE year(r.data_inici) = 2014 OR year(r.data_inici) = 2015 OR year(r.data_inici) = 2016
    HAVING count(client_id)
    ORDER BY c.client_id;