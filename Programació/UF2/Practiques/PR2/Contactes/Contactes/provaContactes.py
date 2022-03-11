from contactes import contacte
import re
from datetime import datetime
from os import system, name

def mostrarMenu(opcions):
    #Mostrara totes les opcions numerades
     for i,opcio in enumerate(opcions):
        print(f"{i+1:2}. {opcio}")

def sortir():
    print("Hasta luego Lucas")

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

def esperaTecla():
     input("Pulsa intro per continuar... ")

def mostrarContactes(contactes):
    print(f"{'Nom':30}{'Telefon':>12}")
    print("="*42)
    for c in contactes:
        print(f"{c.nom:30}{c.telefon:>12}")

def afegirContacte(contactes):
    #Demanar dades contacte
     patroNom = "^[ a-zA-ZÀ-ȗ]{3,}$"
     patroTelefon = "^\d{9,12}$"
     nom = input("Nom: ")
     telefon = input("Telefon: ")
     dataN = input("Data Naixement(d/m/a): ")
     if re.search(patroNom,nom) and re.search(patroTelefon,telefon):
          c = contacte(nom,telefon)
          contactes.append(c)
          try:
               data = datetime.strptime(dataN, '%d/%m/%Y')
               c.dataNaixement = data
          except:
               print("Data naixement no afegida")
     else:
          print("No hem pogut afegir el contacte. Dades incorrectes")
               
def buida(contactes):
     contactes.clear()

def eleiminarContacte(contactes):
     telefon = input("Telefon que vols eliminar: ")
     for i,c in enumerate(contactes):
          if c.telefon == telefon:
               print(f"Telefon: {c.telefon}")
               print(f"Nom: {c.nom}")
               resposta = input("Segur que vols eliminar-lo?(s/n)")
               if resposta.lower() == "s":
                    contactes.pop(i)
                    print("Contacte eliminat")
               return
     print("Contacte no trobat")
     
                    

opcions = ("Mostrar tots","Afegir","Eliminar","Modificar","Buidar tots","Sortir")
fi = False
contactes=[]


while not fi:
    clear() 
    mostrarMenu(opcions)
    #Escullir opcio
    opcio=escullOpcio(len(opcions))
    if opcio == "1":
        #mostrar tots el contactes
        mostrarContactes(contactes)
        esperaTecla()
    elif opcio == "2":
        #Afegir contacte"
        afegirContacte(contactes)
        esperaTecla()
    elif opcio == "3":
        eliminarContacte(contactes)
        esperaTecla()
    elif opcio == "4":
        #Modificar contacte
        pass
    elif opcio == "5":
        #Buidar contactes
        buidar(contactes)
        esperaTecla()
    elif opcio == "6":
        sortir()
        fi = True
    
