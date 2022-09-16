SELECT COUNT(data_contractacio) AS Empleats_contractats_lany_passat
	FROM empleats
    WHERE YEAR(data_contractacio) = 1994;
    
SELECT min(year(data_contractacio)) as empleat_mes_antic
	from empleats;
    
SELECT max(year(data_contractacio)) as empleat_mes_antic
	from empleats;
    
SELECT truncate(avg(salari),2) as salari_mig
	from empleats;

select max(salari) as salari_max, min(salari) as salari_min
	from empleats;

select count(empleat_id) as nempleats, avg(salari)
from empleats;

select feina_codi,avg(salari)
	from empleats 
    GROUP BY feina_codi;
    
select count(empleat_id), feina_codi
	from empleats
    group by feina_codi;

select departament_id, COUNT(empleat_id)
	FROM empleats
    where departament_id is NULL;
    
select concat(cognoms,", ",nom)
	from empleats

	
