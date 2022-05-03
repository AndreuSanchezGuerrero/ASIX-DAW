"""6. Ídem anterior, però que a cada carpeta mare li sumi les mides de les subcarpetes filles. Per exemple, si copieu l’estructura del Ondrive de la carpeta Institut, ens haurà de dir el següent:

Institut\Asix1\Cursa de Sant Jordi: 13216 bytes

Institut\Asix1\Sortida 1r Trimestre: 6608 bytes

Institut\Asix1: 39648 bytes

Institut\Asix2\M6: 6641 bytes

Institut\Asix2\M7: 18040 bytes

Institut\Asix2\M8: 57535 bytes

Institut\Asix2: 169768 bytes

Institut: 227459 bytes"""

def listarsuma(ruta, tab):
    import os
    suma = 0
    for i in os.listdir(ruta):
        if os.path.isfile(os.path.join(ruta, i)):
            suma += os.path.getsize(os.path.join(ruta, i))
        else:
            suma += listarsuma(os.path.join(ruta, i), tab+"\t")
    print(tab,ruta,suma)
    return suma
tab = ""

listarsuma("/home/tursu/GitHub/ASIX1", tab)