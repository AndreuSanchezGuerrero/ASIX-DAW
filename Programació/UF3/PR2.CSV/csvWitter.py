#Prova de csv, necessitem el modul csv
import csv
import string
from unicodedata import normalize
from random import *
import os
os.chdir(os.path.dirname(__file__))
'''
Mètode que genera un nom  de compte d'alumne, no comprova la existencia
'''
def generaCompte(alumne):
    aleatori = randint(100,999)
    compte = (alumne["Nom"][0]+"."+str(normalize('NFKD', alumne["Cognom1"]).encode('ASCII', 'ignore'))+str(aleatori)).replace(" ","").lower()
    return compte

'''
Mètode que genera un password segur, li passem la longitud
'''
def generaPassword(longitud):
    if longitud < 8:
        longitud = 8
    all = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = "".join(sample(all,longitud))
    return password

#Generem un nou fitxer amb els comptes d'usuaris en format csv
with open("usuaris.csv","w",newline="") as usuaris, open("crearComptes.ps1","w",newline="") as nousComptes:
    camps = ["usuari","password"]
    writer = csv.DictWriter(usuaris, fieldnames=camps)#Obrim el escriptor amb format DictWriter
    writer.writeheader()#Escribim la primera línia del fitxer csv, la dels noms dels camps
    
    #Obrim el fitxer d'alumnes per consultar les seves dades
    with open("alumnes.csv") as alumnes:
        reader = csv.DictReader(alumnes,delimiter=",")#Indiquem el delimintardor de camps, per defecte es la coma.
        for alumne in reader:
            nomCompte = generaCompte(alumne)
            password = generaPassword(10)
            nom = alumne["Nom"]
            cognoms = f'{alumne["Cognom1"]} {alumne["Cognom2"]}'
            securePassword = f'ConvertTo-SecureString -String "{password}" -AsPlainText -Force'                                         
            crearCompteAD = f'New-ADuser -Name {nomCompte} -GivenName "{nom}" -SurName "{cognoms}" -AccountPassword ({securePassword})\n' 
            nousComptes.write(crearCompteAD)
            writer.writerow({'usuari':nomCompte,'password':password})

