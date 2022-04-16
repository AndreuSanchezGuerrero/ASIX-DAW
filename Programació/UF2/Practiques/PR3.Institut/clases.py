# Classes
from datetime import date

class alumne:
    def __init__(self, Codia: int, Nom: str, Cognom: str, DataNaixement: date):
        self.Codia = Codia
        self.Nom = Nom
        self.Cognom = Cognom
        self.DataNaixement = DataNaixement
        # self.Materies és un diccionari que tindrà com a Key el codi de MAtèria, i com a value la nota que ha tret l'alumnes de la matèria
        self.Materies = {}


class materia:
    def __init__(self, Codim: int, Nom: str):
        self.Codim = Codim
        self.Nom = Nom
        # self.Alumnes és una nalumne que contindrà els alumnes que estan matriculats de cada matèria. Han de ser els alumnes(Clss Alumne), no els codis d'alumnes
        self.Alumnes = []
