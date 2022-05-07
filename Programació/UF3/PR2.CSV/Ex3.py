"""
Un fitxer csv per a cada grup d’alumnes ASX1A.csv, ASIX2A.csv, ... 
que tingui els següents camps: Grup,Cognom1,Cognom2, Nom, 
NomCompte, Password
Mira si pots aconseguir que cada fitxer estigui ordenat per 
Cognom1,Cognom2,Nom
"""

import csv
import os
os.chdir(os.path.dirname(__file__))

with open('ASIX1.csv',"w") as ASIX1, open('ASIX2.csv',"w") as ASIX2:
    