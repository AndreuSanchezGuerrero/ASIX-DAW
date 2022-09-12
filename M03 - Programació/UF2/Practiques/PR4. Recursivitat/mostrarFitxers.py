#Prova FileSystem
from FileSystem import *

def mostrarFitxers(ruta,tipus):
    
    fitxers = llistaItems(ruta,"F")
    carpetes = llistaItems(ruta,"D")
    for f in fitxers:
        slices = f.Nom.split(".")
        if len(slices)>1:
            extensio = slices[-1]
            if extensio.lower() == tipus.lower():
                print(f"{ruta}/{f.Nom}")
    for c in carpetes:
        rutaNova = f"{ruta}/{c.Nom}"
        mostrarFitxers(rutaNova,tipus)
        
def comptarFitxers(ruta):
    fitxers = llistaItems(ruta,"F")
    carpetes = llistaItems(ruta,"D")
    print(f"{ruta}: {len(fitxers)}")
    for c in carpetes:
        rutaNova = f"{ruta}/{c.Nom}"
        comptarFitxers(rutaNova)
    
def comptarFitxersV2(ruta):
    fitxers = llistaItems(ruta,"F")
    carpetes = llistaItems(ruta,"D")
    total = len(fitxers)
    for c in carpetes:
        rutaNova = f"{ruta}/{c.Nom}"
        total = total + comptarFitxersV2(rutaNova)
    print(f"{ruta}: {total}")
    
    return total
    

mostrarFitxers("/home","txt")
comptarFitxers("/home")
comptarFitxersV2("/home")
