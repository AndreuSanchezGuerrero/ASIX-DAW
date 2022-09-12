#Ens mostri per pantalla un únic missatge amb el contingut del fitxer cotxes.txt
import os
#no canvio l'encoding ja que he creat els arxius desde linux
#Es pot utilitzar un path absolut pero m'agrada mes canviar el directori de execució
os.chdir(os.path.dirname(__file__))
with open("cotxes.txt", mode="r") as f:
    print(f.read())