#1. Mètode iteratiu al que li passarem una llista d’enters i ens retornarà la suma de tots els seus elements
from RDL import *
def sumar(llista):
    suma = 0
    for i in llista:
        suma += i
    return suma

print(sumar(llista))