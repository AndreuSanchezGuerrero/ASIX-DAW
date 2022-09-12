from RDL import *
#3. Fes que el mètode anterior sigui recursiu, però que vagi particionant la llista per la meitat, en dos subllistes, i calculi la suma de les 2 subllistes.
def sumarRecursiu2(llista):
    if len(llista) == 1:
        return llista[0]
    else:
        return sumarRecursiu2(llista[:len(llista)//2]) + sumarRecursiu2(llista[len(llista)//2:])

print(sumarRecursiu2(llista))