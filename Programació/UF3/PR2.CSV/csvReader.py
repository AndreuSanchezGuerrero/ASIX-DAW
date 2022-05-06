#Prova csv, necessitem el modul csv
import csv

#Obrim el fitxer alumnes.csv per lectura
'''
Contingut fitxer alumnes.csv
La primera fila seria la que indica els camps
Les altres files corresponen als registres
Cada camp/valor va separat per coma, però enlloc de coma podria ser punt i coma o altre símbol

Nom,Cognom1,Cognom2,DataNaixement
Dolores,Fuertes De Cabeza,02/01/1900
Ether,Colero,Lleno,01/01/2001
Esther,Illa,de Caña,03/03/1993
Enrique,Cido,Dudoso,04/04/1994
Carmen,Tolado,Fresa,05/05/2005

'''
import os
os.chdir(os.path.dirname(__file__))
with open("alumnes.csv") as f:
    #Muntem un lector sobre el fitxer, que tractarà cada fila del csv com un diccionari
    ''' cada element del reader(llista d'elements) serà un diccionari com el següent

       {'Nom': 'Dolores', 'Cognom1': 'Fuertes De Cabeza', 'Cognom2': '02/01/1900', 'DataNaixement': None}

       Les claus seran les propietats dels csv, primera fila ( Nom, Cognom1, ...) i els valors seran les dades de
       cada alumne, un alumne per fila del reader.
    '''
    reader = csv.DictReader(f,delimiter=",")#Indiquem el delimintardor de camps, per defecte es la coma.
    for alumne in reader:
        print(alumne["Nom"]) #Mostrem el nom de cada alumne
