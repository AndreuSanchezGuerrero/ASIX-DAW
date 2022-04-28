#1. Mètode iteratiu al que li passarem una llista d’enters i ens retornarà la suma de tots els seus elements

from random import randint

#random int list generator
llista = []
x = 10
for i in range(x):
    rint = randint(0, x)
    if rint not in llista:
        llista.append(rint)

def sumar(llista):
    suma = 0
    for i in llista:
        suma += i
    return suma

print(sumar(llista))

#2. Fes que el mètode anterior sigui recursiu, de tal manera que calculi la suma del primer element de la llista mes la suma dels elements restants.
def sumarRecursiu(llista):
    suma = llista[0]
    for i in llista[1:]:
        suma = suma + i
    return suma

print(sumarRecursiu(llista))

#3. Fes que el mètode anterior sigui recursiu, però que vagi particionant la llista per la meitat, en dos subllistes, i calculi la suma de les 2 subllistes.
def sumarRecursiu2(llista):
    if len(llista) == 1:
        return llista[0]
    else:
        return sumarRecursiu2(llista[:len(llista)//2]) + sumarRecursiu2(llista[len(llista)//2:])

print(sumarRecursiu2(llista))

#4. Fes un mètode al que li passarem la ruta d’una carpeta i ens mostrarà tots els fitxer que hi ha a la ruta passada i a les seves subcarpetes
def listar(ruta):
    import os
    for i in os.listdir(ruta):
        if os.path.isfile(os.path.join(ruta, i)):
            print(i)
        else:
            listar(os.path.join(ruta, i))

print(listar("."))

#5. Fes un mètode al que li passarem una ruta, i ens dirà la mida total de cada fitxer que hi ha a cada carpeta( mida només dels fitxers de la carpeta) i subcarpetes(recursivament) que hi hagi a la ruta.



"""6. Ídem anterior, però que a cada carpeta mare li sumi les mides de les subcarpetes filles. Per exemple, si copieu l’estructura del Ondrive de la carpeta Institut, ens haurà de dir el següent:

Institut\Asix1\Cursa de Sant Jordi: 13216 bytes

Institut\Asix1\Sortida 1r Trimestre: 6608 bytes

Institut\Asix1: 39648 bytes

Institut\Asix2\M6: 6641 bytes

Institut\Asix2\M7: 18040 bytes

Institut\Asix2\M8: 57535 bytes

Institut\Asix2: 169768 bytes

Institut: 227459 bytes"""

def mida2(ruta):
    import os
    for i in os.listdir(ruta):
        suma = 0
        ruta2 = os.path.join(ruta, i)
        if os.path.isdir(ruta2):
            
            print(ruta2, suma)

mida2("./")

#7. Fes un mètode al que li passem una llista d’Alumnes (CodiAlumne,Nom,Cognom 1,Cognom 2) i el codi de l’alumne, ens torni l’alumne corresponent al codi passat.
from llistaalumnes import *
def alumne(llista, codi):
    for i in llista:
        if i.codialumne == codi:
            return i
    return None