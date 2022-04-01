# Els cosis s'ha de fer q si selimina un el seguent afegit vaigi alla i tal
from datetime import *
from omplir import X

# Variables Globals
# alumnes és un diccionari que tindrà com a Key el codi de l'alumne, i com a Value al propi alumne
alumnes = {}
# materies és un diccionari que tindrà com a Key el codi de la materia i com a value la pròpia matèria
materies = {}
codia = 0
codim = 0

# Classes


class alumne:
    def __init__(self, Codia: str, Nom: str, Cognom: str, DataNaixement: date):
        self.Codia = Codia
        self.Nom = Nom
        self.Cognom = Cognom
        self.DataNaixement = DataNaixement
        # self.Materies és un diccionari que tindrà com a Key el codi de MAtèria, i com a value la nota que ha tret l'alumnes de la matèria
        self.Materies = {}


class materia:
    def __init__(self, Codim: str, Nom: str):
        self.Codim = Codim
        self.Nom = Nom
        # self.Alumnes és una llista que contindrà els alumnes que estan matriculats de cada matèria. Han de ser els alumnes(Clss Alumne), no els codis d'alumnes
        self.Alumnes = []

# Funcions que heu de programar


def nouAlumne():
    global codia
    Nom = input("Nom: ")
    Cognom = input("Cognom: ")
    # es podria fer graficament la seleccio de dates
    dataStr = input("Data Naixement (diamesany): ")
    DataNaixement = datetime.strptime(dataStr, '%d%m%Y').date()
    a = alumne(codia, Nom, Cognom, DataNaixement)
    codia = codia + 1
    return a


def novaMateria():
    global codim
    m = materia(codim, input("Nom de la materia"))
    codim = codim + 1
    return m



def afegirAlumne(a: Alumne):
    # Afegirà l'alumne a al diccionaru alumnes
    alumnes.update({a.codia: a})


def afegirMateria(m: Materia):
    # Afegirà la materia m al diccionaru materies
    materies.update({m.codim: m})


def eliminarAlumne(codiAlumne: str):
    # Elimina del diccionary alumnes, l'alumne que té com a codi codiAlumne
    # Ha de eliminar-lo també de totes les materies que estigui matriculat
    # Deletes the alumn from the dictionary and delete him from all the subjects he is enrolled
    # shuara de eliminar el codi tmb i per tant fer un buscador de codis vuits o be canviar el codi de tots els alumnes a un menys
    # tmb es podria fer un metoide per afegir un alumne a un codi q ja exiteix movent tots els sltres una posicio
    pass


def eliminarMateria(codiMateria: str):
    # Eliminar la materia amb codiMateria del diccionari materies,
    # i també del diccionari a.materies de tots els alumnes que estaven matriculats d'aquella matèria
    pass


def matriculaAlumne(codiAlumne: str, codiMateria: str):
    # agafarà l'alumne a, que té com a codi codiAlumne del dicc alumnes
    # agafarà la materia m, que té com a codi codiMateria del dicc materies
    # afegirà el coidiMateria a alumne a, per tant, l'afegirà al diccionai a.Materies, amb value buit, el value serà la nota
    # afegirà l'alumne a la materia m, l'afegirà a la llista m.Alumnes
    # Tot l'anterior sempre comprovant que existeixen l'alumne i la materia
    a = alumnes[codiAlumne]
    a.materies.update({input("aaa"): "No avaluat"})


def desmatriculaAlumne(codiAlumne: str, codiMateria: str):
    # Ha de fer el contrari que el métode anterior
    pass


def estaMatriculat(codiAlumne: str, codiMateria: str):
    # retornarà True si l'alumne ja està matriculat de la materia i false sinó està matriculat
    pass


def posarNota(codiAlumne: str, codiMateria: str, nota: int):
    # Servirà per posar nota a l'alumne a
    # Comprovarà que l'alumne està matriculat de la materia, i després li possarà nota
    # a[codiMateria]=nota
    pass


def mostrarNotesMateria(codiMateria: str):
    # Li passarem el codi d'una Matèria i ens mostrarà per pantalla un llistat amb les següents columnes:
    # Nom Materia    CodiAlumne  NomAlumne Nota
    # Si l'alumne no té nota, mostrarà 2 guionets --
    pass


def mostrarNotesAlumne(codiAlumne: str):
    # Li passarem el codi d'un alumne i ens mostrarà per pantalla un llistat amb les següents columnes:
    # Nom Materia  Nota
    # Si l'alumne no té nota, mostrarà 2 guionets --
    pass


codi = 0
