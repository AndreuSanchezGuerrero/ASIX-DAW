import os
from datetime import datetime
from stat import *

class Item:
    def __init__(self,nom,ruta,tipus,dataCreacio,dataModificacio,dataUltimAcces,mida):
        self.Nom = nom
        self.Ruta = ruta
        self.Tipus = tipus
        self.DataCreacio = dataCreacio
        self.DataModificacio = dataModificacio
        self.DataUltimAcces = dataUltimAcces
        self.Mida = mida

def llistaItems(ruta,filtre):
    filtre=filtre.upper()
    llista=[]
    if filtre in ("F","D"):
        for nom in os.listdir(ruta):
            rutaFill = f"{ruta}/{nom}"
            if (filtre=="F" and os.path.isfile(rutaFill)) or \
               (filtre=="D" and os.path.isdir(rutaFill)):
                f = os.stat(rutaFill)
                nouItem = Item(nom,
                               ruta,
                               filtre,
                               datetime.fromtimestamp(f.st_mtime),
                               datetime.fromtimestamp(f.st_ctime),
                               datetime.fromtimestamp(f.st_atime),
                               f.st_size
                               )
                llista.append(nouItem)       
    return llista

