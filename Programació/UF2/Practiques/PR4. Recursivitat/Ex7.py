#7. Fes un mètode al que li passem una llista d’Alumnes (CodiAlumne,Nom,Cognom 1,Cognom 2) i el codi de l’alumne, ens torni l’alumne corresponent al codi passat.
#V1 Sequential search
c = 7000
from time import *
from llistaalumnes import *

def alumne1(llista, codi):
    for i in llista:
        if i.Codi == codi:
            global timeI
            timeI = time() - timeI
            print(llistaAlumnes[i])
    return timeI

#V2 Bynary search
def alumne2(llista, codi):
    meitat = len(llista)//2
    if codi < llista[meitat].Codi:
        alumne2(llista[:meitat], codi)
    elif codi > llista[meitat].Codi:
        alumne2(llista[meitat:], codi)
    else:
        global timeI
        timeI = time() - timeI
        
    return timeI

timeVF1 = 0
timeVF2 = 0

for i in range(1000):
    timeI = time()
    timeVF1 += alumne2(llistaAlumnes, c)
    timeI = time()
    timeVF2 += alumne2(llistaAlumnes, c)
print("Sequencuial:",timeVF1/i)
print("Binaria:    ",timeVF2/i)
