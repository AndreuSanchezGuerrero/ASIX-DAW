#Copy of Corona.py but saves the data in a json file instead of ram
import random
from datetime import *
import re
from os import system, name
from json import *

class pacient: 
    def __init__(self,codi:int,dataNaixement:str,sexe:str ,estat:str,iniciContagi:str,fiContagi:str ): 
        self.codi = codi 
        self.dataNaixement = dataNaixement
        self.sexe = sexe
        self.estat = estat
        self.iniciContagi = iniciContagi
        self.fiContagi = fiContagi


def convert_to_dict(obj):
    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }
    obj_dict.update(obj.__dict__)
    return obj_dict

def dict_to_obj(our_dict):
    if "__class__" in our_dict:
        class_name = our_dict.pop("__class__")
        module_name = our_dict.pop("__module__")
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj


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
    pdataNaixement = datetime.strptime(dataStr,'%d%m%Y').date().strftime(format_code)
    sexe = int(input("Sexe (0=H 1=D): "))
    psexe = sexes[sexe]
    estat = int(input("Estat (0=Lleu 1=Greu 2=UCI 3=Mort): ")) #afegir try except per a opcions fora de la llista i de les dates
    pestat = estats[estat]
    iniciStr = input("Inici Contagi (diamesany):  ")
    iniciC = datetime.strptime(iniciStr,'%d%m%Y').date().strftime(format_code)
    while iniciC < pdataNaixement:
        print("La data de inici de contagi no pot ser anterior a la data de naixement")
        iniciStr = input("Inici Contagi (diamesany):  ")
        iniciC = datetime.strptime(iniciStr,'%d%m%Y').date().strftime(format_code)
    piniciContagi = iniciC
    contagiStr = input("Fi Contagi (diamesany) O 'NULL' si està en curs:  ").upper()
    if contagiStr != "NULL":
        pfiContagi = datetime.strptime(contagiStr,'%d%m%Y').date().strftime(format_code)
    else:
        pfiContagi = "NULL"
    p = pacient(codi,pdataNaixement,psexe,pestat,piniciContagi,pfiContagi)
    pacients.append(p)
    cercarPacient(pacients,codi,0)
    codi += 1
    data = open("Programació/UF3/PR3.Serialització/data.json","w")
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
            if p.codi == codi:
                if opcio == 0:
                    cap()
                    printda(p)
                elif opcio == 1:
                    canviEstatPacient(p,l)
                elif opcio == 2:
                    edat(p,input("Edat a la data (diamesany): "))
                n = 1
        if n == 0:
            print("Aquest pacient no existeix") 

def canviEstatPacient(p:pacient,pacients):
    estat = int(input("Estat (0=Lleu 1=Greu 2=UCI 3=Mort): ")) #TE opcions fora de la llista
    p.estat = estats[estat]
    data = open("Programació/UF3/PR3.Serialització/data.json","w")
    fpacients = []
    for p in pacients:
        fpacients.append(convert_to_dict(p))
    dump(fpacients, data, sort_keys=True, indent=4)
    data.close()
    cercarPacient(pacients,codi,0)

def edat(p:pacient,dataStr:date): #TE per a possibles edats negatives i per a dates mes grans a l'actual canviar el temps del verb
    data = datetime.strptime(dataStr,'%d%m%Y').date().strftime(format_code)
    edat = data.year - p.dataNaixement.year - ((data.month, data.day) < (p.dataNaixement.month, p.dataNaixement.day))
    if data > date.today():
        verb = "tindrà"
    elif data < date.today():
        verb = "tenia"
    elif data == date.today():
        verb = "té"
    print(f"el pacient {p.codi} {verb} {edat} anys el {data}")

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
    data = datetime.strptime(input("Data Naixement (diamesany): "),'%d%m%Y').date().strftime(format_code)
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
    data = datetime.strptime(input("Data Naixement (diamesany): "),'%d%m%Y').date().strftime(format_code)
    cap()
    for p in l:
        if p.iniciContagi == data and estat == estat:
                printda(p)
                n=1
    if n == 0:
        clear()
        print("No hi ha cap pacient contagiat en aquesta data")

sexes= ["H","D"]
estats= ["Lleu","Greu","UCI ","Mort"]
format_code = '%Y-%m-%d'
#Creacio de pacients
def CPacient():
    global codi
    fpacients = []
    inicio = datetime(1967, 1, 1) 
    final = datetime(2003, 12, 31) 
    inicio1 = datetime(2020, 1, 1) 
    final1 = datetime(2022, 12, 31) 
    data = open("Programació/UF3/PR3.Serialització/data.json","w")
    for i in range(0, 4000):
        datenaix = inicio + (final - inicio) * random.random()
        datecontagi = inicio1 + (final1 - inicio1) * random.random()
        dataNaixement = (datenaix.date()).strftime(format_code)
        sexe = random.choice(sexes)
        estat = random.choice(estats)
        iniciContagi = (datecontagi.date()).strftime(format_code)
        fiContagi = "NULL"
        p = pacient(codi, dataNaixement, sexe, estat, iniciContagi, fiContagi)
        pacients.append(p)
        fpacients.append(convert_to_dict(p))
        codi += 1
    dump(fpacients, data, sort_keys=True, indent=4)
    data.close()

opcions = ("Mostrar Pacients","Cercar Pacient","Afegir","Canviar l'estat","Calcular edat","Pacients en estat X","Pacients Contagiats dia X","Pacients en Estat i Data","Sortir","Autogenrear Pacients")
fi = False
codi = 0
try:
    data = open("Programació/UF3/PR3.Serialització/data.json","r")
    fpacients = load(data)
    data.close()
except:
    fpacients = []

pacients = []
for p in fpacients:
    pacients.append(dict_to_obj(p))


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
    elif opcio == "10":
        CPacient()
