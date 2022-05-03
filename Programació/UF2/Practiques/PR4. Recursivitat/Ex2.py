#2. Fes que el mètode anterior sigui recursiu, de tal manera que calculi la suma del primer element de la llista mes la suma dels elements restants.
from RDL import *
def sumarRecursiu(llista):
    suma = llista[0]
    for i in llista[1:]:
        suma = suma + i
    return suma

print(sumarRecursiu(llista))