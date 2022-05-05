"""
5.Ídem anterior. Suposarem que tindrem cotxes de diferents marques, 
però no sabem d'entrada quines marques són. La primera paraula serà 
sempre la marca. En aquest cas. 
Hauràs de fer un with dintre d’un altra with, el de dintre serà el 
d’escriptura amb ruta variable. Hauràs de fer servir append. 
"""
#abans d'executar elimianr els fitxers creats a l'anterior exercici
import os
os.chdir(os.path.dirname(__file__))
with open("cotxes.txt", mode="r") as f:
    marques = []
    for line in f:
        cotxe = line.split()[0]
        with open(cotxe.split()[0] + ".txt", mode="a") as cotxe:
            cotxe.write(line)
            marques.append(cotxe)