from datetime import datetime
class alumne:
    def __init__(self,Codi:int,Nom:str,Cognom:str,DataNaixement:datetime):
        self.Codi=Codi
        self.Nom=Nom
        self.Cognom=Cognom
        self.DataNaixement=DataNaixement
        #self.Materies és un diccionari que tindrà com a Key el codi de MAtèria, i com a value la nota que ha tret l'alumnes de la matèria
        self.Materies={}

llistaAlumnes=[]
for i in range(100000):
    a = alumne(i,f"Nom{i}","Cognoms{i}",datetime(2000,1,1))
    llistaAlumnes.append(a)
