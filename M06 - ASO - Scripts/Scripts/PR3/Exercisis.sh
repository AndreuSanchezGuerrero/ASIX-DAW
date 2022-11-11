#!/bin/bash
#demanem el nom del fitxer
echo "Introdueix el nom del fitxer per a fer les modificacions"
#fem el bucle pq semre torni a crear el menu excepte q s'apreti la opcio de sortir
while [[ $opc -ne 12 ]]
do
    #Fem un menu per seleccionar l'exercici que volem executar
    echo "Quin exercici vols executar?"
    echo "1. Canvia la població de Bleins per Blanes."
    echo "2. Elimineu les tres primeres línies."
    echo "3. Imprimeix les línies 5 a 10."
    echo "4. Eliminar les línies que contenen Lane."
    echo "5. Imprimiu totes les línies en què els aniversaris són al novembre o desembre."
    echo "6. Annexa tres asteriscos al final de les línies que comencen amb Fred."
    echo "7. Substitueix la línia que comença per Jose, per JOSE SHA JUBILAT"
    echo "8. Canvia la data de naixement de Popeye per 11/14/46. Suposa que no saps la data original de Popeye. Utilitza una expressió regular per buscar-la."
    echo "9. Elimina totes les línies en blanc."
    echo "10. (Val per 4). Fent servir el awk fes alguna cosa interessant amb el fitxer anterior, indica el que has fet."
    echo "11. Regenera el fitxer de proves."
    echo "12. Sortir."
    echo "13. Mostrar el fitxer."
    echo "Introdueix el número de l'exercici que vols executar:"
    read opcio

    #Fem un case per executar l'exercici que hem seleccionat cuan ens doni el resultat pausem dins a intro de teclat i regenerem el menu
    case $opcio in
    1) sed -i 's/Bleins/Blanes/g' fitxerproves.txt;;
    2) sed '1,3d' fitxerproves.txt;;
    3) sed -n '5,10p' fitxerproves.txt;;
    4) sed '/Lane/d' fitxerproves.txt;;
    5) sed -n '/11\|12/p' fitxerproves.txt;;
    6) sed -i 's/^Fred/&*** /g' fitxerproves.txt;;
    7) sed 's/^Jose/JOSE SHA JUBILAT/' fitxerproves.txt;;
    8) sed -i 's/.*Popeye.*/Popeye 11\/14\/46/' fitxerproves.txt;;
    9) sed '/^$/d' fitxerproves.txt;;
    10) awk 'BEGIN {FS=","} {print $1}' fitxerproves.txt;;
    #Regenerem el fitxer original elimant tot el contingut previ
    11) sudo cp fitxer.txt fitxerproves.txt;;
    12) exit;;
    13) cat fitxerproves.txt | more;;
    *) echo "Opció incorrecta";;
    esac

    echo "Prem intro per continuar"
    read
done



