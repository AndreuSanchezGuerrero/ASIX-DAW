#Copy of Corona.py but saves the data in a json file instead of ram
import random
from datetime import *
import re
from Pacient import *
from os import system, name
from json import *
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

#Metodes Pacients
def nouPacient(codi):
    #Demanarà per teclat les dades del nou pacient
    dataStr = input("Data Naixement (diamesany): ")
    pdataNaixement = datetime.strptime(dataStr,'%d%m%Y').date()
    sexe = int(input("Sexe (0=H 1=D): "))
    psexe = sexes[sexe]
    estat = int(input("Estat (0=Lleu 1=Greu 2=UCI 3=Mort): ")) #afegir try except per a opcions fora de la llista i de les dates
    pestat = estats[estat]
    iniciStr = input("Inici Contagi (diamesany):  ")
    iniciC = datetime.strptime(iniciStr,'%d%m%Y').date()
    while iniciC < pdataNaixement:
        iniciStr = input("Inici Contagi (diamesany):  ")
        iniciC = datetime.strptime(iniciStr,'%d%m%Y').date()
    piniciContagi = iniciC
    contagiStr = input("Fi Contagi (diamesany) O 'NULL' si està en curs:  ").upper()
    if contagiStr != "NULL":
        pfiContagi = datetime.strptime(contagiStr,'%d%m%Y').date()
    else:
        pfiContagi = "NULL"
    p = pacient(codi,pdataNaixement,psexe,pestat,piniciContagi,pfiContagi)
    pacients.append(p)
    cercarPacient(pacients,codi,0)
    codi = codi + 1
    data = open("Programació/UF3/PR3.Serialització/Exemple Serialització/data.json","w")
    fpacients = []
    for p in pacients:
        fpacients.append(convert_to_dict(p))
    dump(fpacients, data, sort_keys=True, indent=4)
    data.close()

def cap():
    print(f"codi | Data Naixement | Sexe | Estat | Inici Contagi | Fi Contagi")

def printda(p):
    espai = (" "*(5-len(str((p.codi)))))
    print(f"{p.codi}{espai}-   {p.dataNaixement}   -  {p.sexe}   -  {p.estat} -  {p.iniciContagi}   -   {p.fiContagi}")

def mostrarPacients(pacients:list):
    cap()
    print("-"*65)
    for p in pacients:
        printda(p)

def cercarPacient(l:list,codi,opcio):
    if codi > len(l)+1:
        print("Aquest pacient no existeix") 
    else:
        n = 0
        for p in l:
            if codi == codi:
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
    estat = estats[estat]
    cercarPacient(pacients,codi,0)

def edat(p:pacient,dataStr:date): #TE per a possibles edats negatives i per a dates mes grans a l'actual canviar el temps del verb
    data = datetime.strptime(dataStr,'%d%m%Y').date()
    edat = data.year - dataNaixement.year - ((data.month, data.day) < (dataNaixement.month, dataNaixement.day))
    if data > date.today():
        verb = "tindrà"
    elif data < date.today():
        verb = "tenia"
    elif data == date.today():
        verb = "té"
    print(f"el pacient {codi} {verb} {edat} anys el {data}")

def pacientsEstat(l:list,estats:list):
    n=0
    estat = estats[int(input("Estat (0=Lleu 1=Greu 2=UCI 3=Mort): "))] #TE opcions fora de la llista
    cap()
    for p in l:
        if estat == estat:
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
        if iniciContagi == data:
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
        if iniciContagi == data and estat == estat:
                printda(p)
                n=1
    if n == 0:
        clear()
        print("No hi ha cap pacient contagiat en aquesta data")

#codi per omplenar la llista de pacients aleatoriament
fpacients = []
codi = 0
sexes= ["H","D"]
estats= ["Lleu","Greu","UCI ","Mort"]

inicio = datetime(1967, 1, 1) 
final = datetime(2003, 12, 31) 

inicio1 = datetime(2020, 1, 1) 
final1 = datetime(2022, 12, 31) 

format_code = '%Y-%m-%d'
data = open("Programació/UF3/PR3.Serialització/Exemple Serialització/data.json","w")

#Creacio de pacients
for i in range(0, 4000):
    datenaix = inicio + (final - inicio) * random.random()
    datecontagi = inicio1 + (final1 - inicio1) * random.random()
    dataNaixement = (datenaix.date()).strftime(format_code)
    sexe = random.choice(sexes)
    estat = random.choice(estats)
    iniciContagi = (datecontagi.date()).strftime(format_code)
    fiContagi = "NULL"
    p = pacient(codi, dataNaixement, sexe, estat, iniciContagi, fiContagi)
    fpacients.append(convert_to_dict(p))
    codi += 1
dump(fpacients, data, sort_keys=True, indent=4)
data.close()

opcions = ("Mostrar Pacients","Cercar Pacient","Afegir","Canviar l'estat","Calcular edat","Pacients en estat X","Pacients Contagiats dia X","Pacients en Estat i Data","Sortir")
fi = False

fpacients = load(open("Programació/UF3/PR3.Serialització/Exemple Serialització/data.json","r"))
pacients = []
for p in fpacients:
    pacients.append(dict_to_obj(p))
data.close()

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
