#!/bin/bash

while IFS=", " read -r user pass groups
do 
    if id -u $user >/dev/null 2>&1
    then
        echo "L'usuari $user ja existeix"
        echo "L'usuari $user ja existeix" >> existents.log
    else
        useradd -m -g profes -s /bin/bash $user
        echo "$user:$pass" | chpasswd
        echo "Usuari $user creat correctament" >> nous.log
    fi
    for i in $(echo $groups | tr ";" " ")
    do
        usermod -a -G $i $user
    done
    echo "Usuari creat/modificat correctament"
    id $user
done < Ex2_v1.csv

