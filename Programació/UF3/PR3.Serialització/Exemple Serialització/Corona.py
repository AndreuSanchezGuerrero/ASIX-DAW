#Copy of Corona.py but saves the data in a json file instead of ram

from datetime import *
import re
from Pacient import *
from os import system, name
import json
from dumpJson import *

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
    iniciC = datetime.strptime(iniciStr,'%d%m%Y').date()
    while iniciC < p.dataNaixement:
        iniciStr = input("Inici Contagi (diamesany):  ")
        iniciC = datetime.strptime(iniciStr,'%d%m%Y').date()
    p.iniciContagi = iniciC
    contagiStr = input("Fi Contagi (diamesany) O 'NULL' si està en curs:  ").upper()
    if contagiStr != "NULL":
        p.fiContagi = datetime.strptime(contagiStr,'%d%m%Y').date()
    else:
        p.fiContagi = "NULL"
    cercarPacient(pacients,codi,0)
    codi = codi + 1

def mostrarPacients(l:list):
    cap()
    for p in l:
        printda(p)

def cercarPacient(l:list,codi,opcio):
    if codi > len(l)+1:
        print("Aquest pacient no existeix") 
    else:
        n = 0
        for p in l:
            if p.Codi == codi:
                if opcio == 0:
                    cap()
                    printda(p)
                elif opcio == 1:
                    canviEstatPacient(p)
                elif opcio == 2:
                    edat(p,input("Edat a la data (diamesany): "))
                n = 1
        if n == 0:
            print("Aquest pacient no existeix") 

def canviEstatPacient(p:pacient):
    estat = int(input("Estat (0=Lleu 1=Greu 2=UCI 3=Mort): ")) #TE opcions fora de la llista
    p.estat = estats[estat]
    cercarPacient(pacients,p.Codi,0)

def edat(p:pacient,dataStr:date): #TE per a possibles edats negatives i per a dates mes grans a l'actual canviar el temps del verb
    data = datetime.strptime(dataStr,'%d%m%Y').date()
    edat = data.year - p.dataNaixement.year - ((data.month, data.day) < (p.dataNaixement.month, p.dataNaixement.day))
    if data > date.today():
        verb = "tindrà"
    elif data < date.today():
        verb = "tenia"
    elif data == date.today():
        verb = "té"
    print(f"el pacient {p.Codi} {verb} {edat} anys el {data}")

def pacientsEstat(l:list,estats:list):
    n=0
    estat = estats[int(input("Estat (0=Lleu 1=Greu 2=UCI 3=Mort): "))] #TE opcions fora de la llista
    cap()
    for p in l:
        if p.estat == estat:
            printda(p)
            n=1
    if n == 0:
        clear()
        print("No hi ha cap pacient en aquest estat")

def pacientsData(l:list):
    n=0
    data = datetime.strptime(input("Data Naixement (diamesany): "),'%d%m%Y').date()
    cap()
    for p in l:
        if p.iniciContagi == data:
            printda(p)
            n=1
    if n == 0:
        clear()
        print("No hi ha cap pacient contagiat en aquesta data")

def pacientsEstatData(l:list):#Es pot simplificar molt fent us dels altres dos metodes i amb un parametre per escollir entre les 3 opcions
    n=0
    estat = estats[int(input("Estat (0=Lleu 1=Greu 2=UCI 3=Mort): "))] #TE opcions fora de la llista
    data = datetime.strptime(input("Data Naixement (diamesany): "),'%d%m%Y').date()
    cap()
    for p in l:
        if p.iniciContagi == data and p.estat == estat:
                printda(p)
                n=1
    if n == 0:
        clear()
        print("No hi ha cap pacient contagiat en aquesta data")

#Codi per omplenar la llista de pacients aleatoriament
pacients = {}
codi = 0
sexes= ["H","D"]
estats= ["Lleu","Greu","UCI ","Mort"]

inicio = datetime(1967, 1, 1) 
final = datetime(2003, 12, 31) 

inicio1 = datetime(2020, 1, 1) 
final1 = datetime(2022, 12, 31) 

#Creacio de pacients
for i in range(0, 40000):
    datenaix = inicio + (final - inicio) * random.random()
    datecontagi = inicio1 + (final1 - inicio1) * random.random()
    p = pacient(codi)
    p.dataNaixement = datenaix.date()
    p.sexe = random.choice(sexes)
    p.estat = random.choice(estats)
    p.iniciContagi = datecontagi.date()
    p.fiContagi = "NULL"
    p1 = dict_to_obj(convert_to_dict(p))
    json.dump(p1, "data.json", sort_keys=True, indent=4)
    "data.json".close()
    codi += 1

opcions = ("Mostrar Pacients","Cercar Pacient","Afegir","Canviar l'estat","Calcular edat","Pacients en estat X","Pacients Contagiats dia X","Pacients en Estat i Data","Sortir")
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
        pacientsEstat(pacients,estats) #L'estat no li passem, el demanarà dins
    elif opcio == "7":
        pacientsData(pacients)
    elif opcio == "8":
        pacientsEstatData(pacients)
    elif opcio == "9":
        fi = True
