#!/bin/bash
#No puc fer servir l'script de nouprofe.sh perque aqui haig de obrir el csv, em sebla mes raonable partir del Ex2_v1
while IFS=", " read -r name surname1 surname2 groups mail
do
    user=$(echo $name"."$surname1 | tr " " "." | tr -d "[:punct:]" | tr "[:upper:]" "[:lower:]")
    if id -u $user >/dev/null 2>&1
    then
        echo "L'usuari $user ja existeix li afegim un numero"
        $user = $user + $RANDOM
    else
        useradd -m -g profes -s /bin/bash $user
        echo "Usuari $user creat correctament" >> nous.log
    fi
    for i in $(echo $groups | tr ";" " ")
    do
        usermod -a -G $i $user
    done
    echo "Usuari creat/modificat correctament"
    id $user
done < Ex2_v2.csv