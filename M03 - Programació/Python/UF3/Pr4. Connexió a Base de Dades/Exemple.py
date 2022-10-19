import mysql.connector
from datetime import datetime

institutDB = mysql.connector.connect(
    host="192.168.100.214",
    user="perepi",
    password="pastanaga",
    database="ProgramacioInstitut"
)

cursor = institutDB.cursor()
#Creem la taula alumnes
commandataula = "CREATE TABLE IF NOT EXISTS alumnes (idalu INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(50), cognom1 VARCHAR(50), cognom2 VARCHAR(50), dataNaixement DATE)"
cursor.execute(commandataula)

class alumne:
    def __init__(self, nom, cognom1, cognom2, dataN):
        self.nom = nom
        self.cognom1 = cognom1
        self.cognom2 = cognom2
        self.dataN = dataN


def nouAlumne1():
    nom = input("Nom: ")
    cognom1 = input("1r Cognom: ")
    cognom2 = input("2n Cognom: ")
    dataN = datetime.strptime(input("Data Naixement: "), '%d/%m/%Y').date()
    return alumne(nom, cognom1, cognom2, dataN)

def nouAlumne():
    nom = "a"
    cognom1 = "as"
    cognom2 = "as"
    dataN = datetime.strptime("09/09/2018", '%d/%m/%Y').date()
    return alumne(nom, cognom1, cognom2, dataN)


a1 = nouAlumne()

comandaInsert = f'''INSERT INTO alumnes (Nom,Cognom1,Cognom2,DataNaixement)
                    VALUES ('{a1.nom}','{a1.cognom1}','{a1.cognom2}','{a1.dataN}');'''

cursor.execute(comandaInsert)
comandaSelect = "SELECT * FROM alumnes;"
cursor.execute(comandaSelect)

alumne = cursor.fetchone()
while alumne:
    print(alumne)
    alumne = cursor.fetchone()

cursor.execute(comandaSelect)
alumnes = cursor.fetchall()
for alumne in alumnes:
    print(alumne)


institutDB.commit()
cursor.close()
institutDB.close()
