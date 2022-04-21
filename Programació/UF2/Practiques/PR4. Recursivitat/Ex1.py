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
        suma = suma + i
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