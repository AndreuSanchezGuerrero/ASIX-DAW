from datetime import *
import re
from pacient import *
from os import system, name

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

#Metodes Pacients
def nouPacient():    
    #Demanarà per teclat les dades del nou pacient
    codi = codi+1
    p = pacient(codi)
    dataStr = input("Data Naixement: ")
    p.dataNaixement = datetime.strptime(dataStr,'%d/%m/%Y')
    p.sexe = input("Sexe: ")
    p.estat = input("Estat : ")
    iniciStr = input("Inici Contagi: ")
    p.iniciContagi = datetime.strptime(dataStr,'%d/%m/%Y')
    return p

#def eliminarPacient(): 
    

def canviEstatPacient(p:pacient,estat:str):
    p.estat=estat

def mostrarPacients(l:list):
    for p in l:
        print(f"{p.Codi}-{p.dataNaixement}-{p.estat}")

def cercarPacient(l:list,codi:str):
    for p in l:
        if p.Codi==codi:
            return p
    return None

codi = 
opcions = ("Mostrar Pacients","Afegir","Canviar l'estat","Calcular edat","Sortir")
fi = False
pacients = []

while not fi:
    clear() 
    for i,opcio in enumerate(opcions):
        print(f"{i+1:2}. {opcio}")
    #Escollir opcio
    opcio = escullOpcio(len(opcions))
    if opcio == "1":
        #mostrar tots els pacients
        mostrarPacients(pacient)
    elif opcio == "2":
        #Afegir Pacient"
        p = nouPacient()
        pacients.append(p)
    elif opcio == "3":
        #Modificar Pacient
        codi = input("Codi pacient que li vols canviar l'estat: ")
        p = cercarPacient(pacients,codi)
        if p:
            #mostrar pacient
            estat = input("Nou Estat: ")
            canviEstatPacient(p,estat)
    elif opcio == "4":
        codi = input("Codi pacient que li vols calcular la edat: ")
    elif opcio == "5":
        fi = True