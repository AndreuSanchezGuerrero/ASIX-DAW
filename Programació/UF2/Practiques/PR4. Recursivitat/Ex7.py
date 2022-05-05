#7. Fes un mètode al que li passem una llista d’Alumnes (CodiAlumne,Nom,Cognom 1,Cognom 2) i el codi de l’alumne, ens torni l’alumne corresponent al codi passat.
#V1 Sequential search
c = 7000
from time import *
from llistaalumnes import *

def alumne1(llista, codi):
    for i in llista:
        if i.Codi == codi:
            return i

#V2 Bynary search
def alumne2(llista, codi):
    meitat = len(llista)//2
    if codi < llista[meitat].Codi:
        alumne2(llista[:meitat], codi)
    elif codi > llista[meitat].Codi:
        alumne2(llista[meitat:], codi)
    elif codi == llista[meitat].Codi:
        return llista[meitat]

print(alumne1(llistaAlumnes, c))
print(alumne2(llistaAlumnes, c))

for i in range(1000):
    timeI = time()
    alumne2(llistaAlumnes, c)
    timeVI = time() - timeI
    timeI = time()
    alumne2(llistaAlumnes, c)
    timeVII = time() - timeI
print("Sequencuial:",timeVI/i)
print("Binaria:    ",timeVII/i)
