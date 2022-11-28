#Exercici 19
#Comprovem que s'ha passat un parametre
if [ $# -eq 1 ]; then
    ping -c 4 $1 | cut -d" " -f8 | grep "time"
else
    echo "No s'ha passat cap parametre"
fi