#5. Fes un mètode al que li passarem una ruta, i ens dirà la mida total de cada fitxer que hi ha a cada carpeta( mida només dels fitxers de la carpeta) i subcarpetes(recursivament) que hi hagi a la ruta.
def calcularmida(ruta,tab):
    import os
    global mida
    suma =  0
    for i in os.listdir(ruta):
        if os.path.isfile(os.path.join(ruta, i)):
            mida = os.path.getsize(os.path.join(ruta, i))
            suma = suma + mida
        else:
            calcularmida(os.path.join(ruta, i),tab+"\t")
    print(tab,ruta,suma)
mida = 0
tab = ""
calcularmida("/home/tursu/GitHub/ASIX1",tab)
#El desplegable esta invertit