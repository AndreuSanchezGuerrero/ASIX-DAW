#4. Fes un mètode al que li passarem la ruta d’una carpeta i ens mostrarà tots els fitxer que hi ha a la ruta passada i a les seves subcarpetes
tab = ""
def listar(ruta, tab):
    import os
    for i in os.listdir(ruta):
        if os.path.isfile(os.path.join(ruta, i)):
            print(tab,os.path.join(ruta, i))
        else:
            listar(os.path.join(ruta, i), tab + "\t")

listar(".",tab)