#!/bin/bash

#Comprovem que el nombre d'arguments sigui correcte
if [ $# -lt 3 ]
then
    echo "Nombre d'arguments incorrecte"
    echo "S'ha d'executar el script de la següent manera:"
    echo "adduser nom password grup1 [grup2] [grup3] ..."
    exit 1
fi

#Comprovem que l'usuari no existeixi
if id -u $1 >/dev/null 2>&1
then
    echo "L'usuari $1 ja existeix"
    exit 1
fi

#Comprovem que els grups secundaris existeixin (supsoso que ja els tens creats, pero per asegurar)
for i in ${@:3} 
do
    if ! grep -q "^$i:" /etc/group
    then
        echo "El grup secundari $i no existeix"
        exit 1
    fi
done

#Creem l'usuari
useradd -m -g profes -s /bin/bash $1

#Afegim el password
echo "$1:$2" | chpasswd

#Afegim els grups secundaris
for i in ${@:3} 
do
    usermod -a -G $i $1
done

#Mostrem l'usuari creat
echo "Usuari creat correctament"
id $1

