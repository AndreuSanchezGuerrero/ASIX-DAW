#Exercici 17
#Comprovem que s'ha passat un parametre
if [ $# -eq 1 ]; then
    #Comprovem que el parametre es una interficie de xarxa
    if [ -d /sys/class/net/$1 ]; then
        #Comprovem que la interficie te una mac assignada
        if [ -f /sys/class/net/$1/address ]; then
            #Mostrem la mac
            cat /sys/class/net/$1/address
        else
            echo "La interficie no te una mac assignada"
        fi
    else
        echo "No es una interficie de xarxa"
    fi
else
    echo "No s'ha passat cap parametre"
fi
