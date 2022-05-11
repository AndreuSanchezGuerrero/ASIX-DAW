#Prova de csv, necessitem el modul csv
import csv
import re
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
with open("Gmail.csv","w",newline="") as Gmail, open('ASIX1.csv',"w",newline="") as ASIX1, open('ASIX2.csv',"w",newline="") as ASIX2, open("usuaris.csv","w",newline="") as usuaris, open("crearComptes.ps1","w",newline="") as nousComptes:
    camps = ["usuari","password"]
    camps1 = ["Grup","Cognom1","Cognom2","Nom","NomCompte","Password"]
    camps2 = ["Email Address","First name","Last Name","Password","Org Unit Path"]
    writer = csv.DictWriter(usuaris, fieldnames=camps)
    writer.writeheader()
    writer1 = csv.DictWriter(ASIX1, fieldnames=camps1)
    writer1.writeheader()
    writer2 = csv.DictWriter(ASIX2, fieldnames=camps1)
    writer2.writeheader()
    writer3 = csv.DictWriter(Gmail, fieldnames=camps2)
    writer3.writeheader()
    
    #Obrim el fitxer d'alumnes per consultar les seves dades
    
    with open("alumnes.csv") as alumnes:
        reader = csv.DictReader(alumnes,delimiter=",")#Indiquem el delimintardor de camps, per defecte es la coma.
        for alumne in reader:
            nomCompte = generaCompte(alumne)
            password = generaPassword(10)
            nom = alumne["Nom"]
            cognoms = f'{alumne["Cognom1"]} {alumne["Cognom2"]}'
            securePassword = f'ConvertTo-SecureString -String "{password}" -AsPlainText -Force'                                         
            """
            Un fitxer ps1 per crear els comptes d’usuari a l’Active Directory. A 
            New-ADUser afegeix els paràmetres Path, Description, DisplayName, 
            Enabled
            Description, serà la data de naixement de l’alumne
            Path serà la ruta on crearà l’alumne, en el nostre cas serà de la 
            forma
            “ou=asix1a, ou=alumnes, dc=sapalomera, dc=net” la primera ou 
            depèn del grup.
            DisplayName, serà el nom complet en format “Cognom1 
            Cognom2, Nom”
            Enabled, serà $true, en Powershell true és una constant i va 
            precedida de $
            """
            crearCompteAD = f'New-ADuser -Name {nomCompte} -GivenName "{nom}" -SurName "{cognoms}" -AccountPassword ({securePassword})\n'
            nousComptes.write(crearCompteAD)
            writer.writerow({'usuari':nomCompte,'password':password})
            #Utilitzem regex per comprobar si l'alumne és de l'ASIX1 o ASIX2 sense importar la llletra del final
            if re.search("^ASIX1",alumne["Grup"]):
                writer1.writerow({"Grup":alumne["Grup"],
                                "Cognom1":alumne["Cognom1"],
                                "Cognom2":alumne["Cognom2"],
                                "Nom":alumne["Nom"],
                                "NomCompte":nomCompte,
                                "Password":password})
            if re.search("^ASIX2",alumne["Grup"]):
                writer2.writerow({"Grup":alumne["Grup"],
                                "Cognom1":alumne["Cognom1"],
                                "Cognom2":alumne["Cognom2"],
                                "Nom":alumne["Nom"],
                                "NomCompte":nomCompte,
                                "Password":password})
            
            writer3.writerow({"Email Address":nomCompte+"@sapalomera.cat",
                                "First name":nom,
                                "Last Name":alumne["Cognom1"],
                                "Password":password,
                                "Org Unit Path":"/alumnes/"+alumne["Grup"].lower()})