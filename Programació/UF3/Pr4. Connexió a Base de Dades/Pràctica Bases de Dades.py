"""
Es tracta de fer un programa per la gestió completa de la taula alumnes amb els
següents campsd
Idalu(codi aumne) és la clau
nom
cognom1,cognom2,dataNaixement)
El programa tindrà un menú com el següent( si el feu amb consola sense el tkinter)
1. Nou alumne
Demanarà les dades d'un l'alumne i l'afegirà a la base de dades,
Si intentes insertar un alumne amb un idalu que ja existeix, la base de dades
generarà un error has de capturar l'errada i mostrar el missatge.
Si l'afegeix a la Base de Dades sense problemas, recorda que s'ha de fer un
Commit
2. Eliminar Alumne.
Ens demanarà el codi de l'alumne que volem eliminar. Si existeix, ens
mostrarà les dades de l'alumne i ens demanarà confirmació per eliminar-lo.
Record afer el commit.
3. Modificar Alumne.
Ens demanarà l'idalu d'un alumne, ens mostrarà les seves dades i anirà
preguntat d'una en una el seu valor nou, si cliquem intrp mantindrà l'antic
valor.
Ha de fer l'update i el commit
4. Mostrar alumnes( tindrà l'opció de mostrar diferentes consultes)
• Els alumnes que comencen per una lletra
• Els nascuts un any concret
• …..
"""
from sqlite3 import Cursor
import mysql.connector
import datetime
from os import system, name
import re

#conexió a la base de dades
institutDB = mysql.connector.connect(
    host="192.168.100.214",
    user="perepi",
    password="pastanaga",
    database="ProgramacioInstitut"
)

#Metodes
def nouAlumne():
    #Demanar les dades
    nom = input("Nom: ")
    cognom1 = input("Cognom1: ")
    cognom2 = input("Cognom2: ")
    dataNaixement = input("Data de naixement (dd/mm/yyyy): ")
    #Convertir la data
    dataNaixement = datetime.datetime.strptime(dataNaixement, "%d/%m/%Y")
    #Insertar a la base de dades
    cursor.execute("INSERT INTO alumnes (nom, cognom1, cognom2, dataNaixement) VALUES (%s, %s, %s, %s)", (nom, cognom1, cognom2, dataNaixement))
    try:
        institutDB.commit()
        print("Alumne afegit correctament")
    except:
        print("Error")

def eliminarAlumne():
    #Demanar el codi de l'alumne
    codi = input("Codi de l'alumne: ")
    #Comprovar que existeix
    cursor.execute(f"SELECT * FROM alumnes WHERE idalu = {codi}")
    al = cursor.fetchone()
    if al is None:
        print("L'alumne no existeix")
    else:
        #Mostrar les dades
        print("Alumne: ", al)
        #Confirmar l'eliminació
        confirmacio = input("Eliminar? (S/N) ")
        if confirmacio == "S":
            print("Eliminant...")
            cursor.execute(f"DELETE FROM alumnes WHERE idalu = {codi}")
            institutDB.commit()
            print("Alumne eliminat correctament")
        else:
            print("Eliminació cancel·lada")

def modificarAlumne():
    #Demanar el codi de l'alumne
    codi = input("Codi de l'alumne: ")
    #Comprovar que existeix
    cursor.execute(f"SELECT * FROM alumnes WHERE idalu = {codi}")
    al = cursor.fetchone()
    if al is None:
        print("L'alumne no existeix")
    else:
        #Mostrar les dades
        cursor.execute(f"SELECT * FROM alumnes WHERE idalu = {codi}")
        alumne = cursor.fetchone()
        print("Alumne: ", alumne)
        #Demanar els nous valors
        nom = input("Nom: ")
        cognom1 = input("Cognom1: ")
        cognom2 = input("Cognom2: ")
        dataNaixement = input("Data de naixement (dd/mm/yyyy): ")
        #Convertir la data
        dataNaixement = datetime.datetime.strptime(dataNaixement, "%d/%m/%Y")
        #Insertar a la base de dades
        cursor.execute("UPDATE alumnes SET nom = %s, cognom1 = %s, cognom2 = %s, dataNaixement = %s WHERE idalu = %s", (nom, cognom1, cognom2, dataNaixement, codi))
        institutDB.commit()
        print("Alumne modificat correctament")

def mostrarAlumnes():
    #Demanar la opció
    opcions1 = ["Alumnes que comencen per una lletra","Alumnes nascuts un any concret","Tots els alumnes"]
    for i,opcio in enumerate(opcions1):
        print(f"{i+1:2}. {opcio}")
    opcio = escullOpcio(len(opcions1))
    #Mostrar les dades
    if opcio == "1":
        #Mostrar els alumnes que comencen per una lletra
        lletra = input("Lletra: ")
        cursor.execute(f"SELECT * FROM alumnes WHERE nom LIKE '{lletra}%'")
    elif opcio == "2":
        #Mostrar els nascuts un any concret
        any = input("Any: ")
        cursor.execute(f"SELECT * FROM alumnes WHERE dataNaixement LIKE '%{any}%'")
    elif opcio == "3":
        #Mostrar tots els alumnes
        cursor.execute("SELECT * FROM alumnes")
    else:
        print("Opció incorrecta")
    #Mostrar les dades
    alumnes = cursor.fetchall()
    print("Alumnes:")
    for alumne in alumnes:
        print(alumne)

#Menu de selecció
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

opcions = ["Nou alumne","Eliminar alumne","Modificar alumne","Mostrar alumnes"]

fi = False

while not fi:
    input("Presiona enter per continuar")
    clear() 
    cursor = institutDB.cursor()
    for i,opcio in enumerate(opcions):
        print(f"{i+1:2}. {opcio}")
    #Escollir opcio
    opcio = escullOpcio(len(opcions))
    if opcio == "1":
        nouAlumne()
    elif opcio == "2":
        eliminarAlumne()
    elif opcio == "3":
        modificarAlumne()
    elif opcio == "4":
        mostrarAlumnes()
    else:
        fi = True
    cursor.close()

