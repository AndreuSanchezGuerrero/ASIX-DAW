#el codi autoincrmen tal coincideix amb les altres variables codi, sh'ha de canviar
from datetime import *
import re
from Pacient import *
from os import system, name

def escullOpció(n):
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

def cap():
    print(f"Codi | Data Naixement | Sexe | Estat | Inici Contagi | Fi Contagi")
    print("-"*65)

def printda(p):
    espai = (" "*(5-len(str((p.Codi)))))
    print(f"{p.Codi}{espai}-   {p.dataNaixement}   -  {p.sexe}   -  {p.estat} -  {p.iniciContagi}   -   {p.fiContagi}")

#Metodes Pacients
def nouPacient(codi):    
    #Demanarà per teclat les dades del nou pacient
    p = pacient(codi)
    dataStr = input("Data Naixement (diamesany): ")
    p.dataNaixement = datetime.strptime(dataStr,'%d%m%Y').date()
    sexe = int(input("Sexe (0=H 1=D): "))
    p.sexe = sexes[sexe]
    estat = int(input("Estat (0=Lleu 1=Greu 2=UCI 3=Mort): ")) #afegir try except per a opcions fora de la llista i de les dates
    p.estat = estats[estat]
    iniciStr = input("Inici Contagi (diamesany):  ")
    p.iniciContagi = datetime.strptime(iniciStr,'%d%m%Y').date()
    contagiStr = input("Fi Contagi (diamesany) O Enter si està en curs:  ").upper()
    if contagiStr != "NULL":
        p.fiContagi = datetime.strptime(contagiStr,'%d%m%Y').date()
    else:
        p.fiContagi = "NULL"
    codi = codi + 1
    pacients.append(p)
    cercarPacient(pacients,codi)

def mostrarPacients(l:list):
    cap()
    for p in l:
        printda(p)

def cercarPacient(l:list,codi,opcio):
    for p in l:
        if p.Codi == codi:
            if opcio == 0:
                cap()
                printda(p)
            elif opcio == 1:
                canviEstatPacient(p)
            elif opcio == 2:
                edat(p,input("Data Naixement (diamesany): ")
    print("Aquest pacient no existeix") #fer q no faci un print per cada pacient no trobat(potser una variable q retorni none?)

def canviEstatPacient(p:pacient):
    estat = int(input("Estat (0=Lleu 1=Greu 2=UCI 3=Mort): ")) #afegir try except per a opcions fora de la llista i de les dates
    p.estat = estats[estat]

def edat(p:pacient,dataStr:date):
    data = datetime.strptime(dataStr,'%d%m%Y').date()
    edat = data.year - p.dataNaixement.year - ((data.month, data.day) < (p.dataNaixement.month, p.dataNaixement.day))
    print(f"el pacient {p.Codi} tenia {edat} anys el {data}")

#Codi per omplenar la llista de pacients aleatoriament
pacients = []
codi = 0
sexes= ["H","D"]
estats= ["Lleu","Greu","UCI ","Mort"]

inicio = datetime(1967, 1, 1) 
final = datetime(2003, 12, 31) 

inicio1 = datetime(2021, 1, 1) 
final1 = datetime(2022, 12, 31) 

#Creacio de pacients
for i in range(0, 40):
    datenaix = inicio + (final - inicio) * random.random()
    datecontagi = inicio1 + (final1 - inicio1) * random.random()
    p = pacient(codi)
    p.dataNaixement = datenaix.date()
    p.sexe = random.choice(sexes)
    p.estat = random.choice(estats)
    p.iniciContagi = datecontagi.date()
    p.fiContagi = "NULL"
    codi = codi + 1
    pacients.append(p) 

opcions = ("Mostrar Pacients","Cercar Pacient","Afegir","Canviar l'estat","Calcular edat","Sortir")
fi = False

while not fi:
    input("Presiona enter per continuar")
    clear() 
    for i,opcio in enumerate(opcions):
        print(f"{i+1:2}. {opcio}")
    #Escollir opcio
    opcio = escullOpcio(len(opcions))
    if opcio == "1":
        #mostrar tots els pacients
        mostrarPacients(pacients)
    elif opcio == "2":
        cercarPacient(pacients,int(input("Introdueix el codi: ")),0)
    elif opcio == "3":
        #Afegir Pacient"
        p = nouPacient(codi)
    elif opcio == "4":
        #Modificar Estat
        cercarPacient(pacients,int(input("Introdueix el codi: ")),1)
    elif opcio == "5":
        cercarPacient(pacients,int(input("Introdueix el codi: ")),2)
    elif opcio == "6":
        fi = True
