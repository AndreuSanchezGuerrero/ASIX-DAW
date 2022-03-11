from datetime import *
import re
from os import system, name
class pacient:
    dataNaixement:date
    sexe:str #H,D
    estat:str #Lleu,Greu,UCI,mort
    iniciContagi:date
    fiContagi:date
    def __init__(self,Codi:str):
        self.Codi = Codi

def escullOpcio(n):
    patro = "^\d{1,}$"
    while True:
        o = input("Opció: ")
        if re.search(patro,o):
            if n>=int(o) and int(o)!=0:
                return o
        
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#Metodes edicio Pacients
def nouPacient():
    

opcions = ("Mostrar Pacients","Afegir","Canviar l'estat","Calcular edat","Sortir")
fi = False
pacients = []
p = pacient(Codi)
p.estat = ""

while not fi:
    clear() 
    for i,opcio in enumerate(opcions):
        print(f"{i+1:2}. {opcio}")
    #Escollir opcio
    opcio = escullOpcio(len(opcions))
    if opcio == "1":
        #mostrar tots els pacients
        mostrarPacients(pacient)
        input("Presiona intro per continuar... ")
    elif opcio == "2":
        #Afegir Pacient"
        afegirPacient(pacient)
        input("Presiona intro per continuar... ")
    elif opcio == "3":
        eliminarPacient(pacient)
        input("Presiona intro per continuar... ")
    elif opcio == "4":
        #Modificar Pacient
        pass
    elif opcio == "5":
        fi = True