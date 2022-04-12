from tkinter import *
from tkinter import ttk
from datetime import *
from tkinter.scrolledtext import ScrolledText
from omplir import *
from clases import *

#Finestra amb el formulari per crear nous alumnes
class NewA(Toplevel): 
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        a = ""
        c = Label(self, text="Codi:").grid(row=0, column=0)
        Codia = Entry(self).grid(row=0, column=1)
        n = Label(self, text="Nom:").grid(row=1, column=0)
        Nom= Entry(self).grid(row=1, column=1)
        co = Label(self, text="Cognom:").grid(row=2, column=0)
        Cognom= Entry(self).grid(row=2, column=1)
        #desegable per triar la data de naixement
        d = Label(self, text="Data de naixement:").grid(row=3, column=0)
        d2= Entry(self).grid(row=3, column=1)
        a = alumne(Codia,Nom,Cognom,d2)
        e = Button(self, text="Acceptar", command = alumnes.update({Codia:a})).grid(row=4, column=0)

#Finestra amb el formulari per crear noves materies
class NewM(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        m = ""
        global codim
        n = Label(self, 
                text="Nom:").grid(row=0, column=0)
        Nom = Entry(self).grid(row=0, column=1)
        m = materia(codim, Nom)
        e = Button(self,
                    text="Acceptar", 
                    command = materies.update({codim:m})).grid(row=1, column=0)

class Menu(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x500")
        self.resizable(0, 0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=1)
        self.scrollbar = Scrollbar(self).grid(row=0, column=3)
        self.listbox = Listbox(self)
        for i in alumnes:
            a = alumnes[i]
            self.listbox.insert(END, 
                                "Codi: " + str(a.Codia), 
                                "Nom: " + str(a.Nom), 
                                "Cognom: " + str(a.Cognom), 
                                "Data Naixement: " + str(a.DataNaixement),
                                "="*20)
        self.listbox.grid(row=0, column=2)
        self.title("Sa Palomera")
        Button(self, 
                text="Nou Alumne", 
                command = self.newA).grid(row=0, column=0)
        Button(self, 
                text="Nova Materia", 
                command = self.newM).grid(row=0, column=1)
    def newA(self):
        window = NewA(self)
        window.grab_set()
    def newM(self):
        window = NewM(self)
        window.grab_set()

if __name__ == "__main__":
    menu = Menu()
    menu.mainloop()


# Els codis s'ha de fer q si selimina un el seguent afegit vaigi alla i tal

codia = len(alumnes)
codim = len(materies)

# Funcions que heu de programar

def mostrarAlumnes():
    llistaAlumnes = Listbox(menu)
    for i in alumnes:
        a = alumnes[i]
        llistaAlumnes.insert(a.Codia,a.Nom,a.Cognom,a.DataNaixement)

def novaMateria():
    global codim
    m = materia(codim, input("Nom de la materia: "))
    codim = codim + 1
    return m

#potser aquestes dos es poden incloure en una funció perque no es necessari repetir
def afegirAlumne(a: alumne):
    # Afegirà l'alumne a al diccionaru alumnes
    global codia
    a = alumne()
    alumnes.update({a.codia: a})


def afegirMateria(m: materia):
    # Afegirà la materia m al diccionaru materies
    materies.update({m.codim: m})


def eliminarAlumne(codiAlumne: int):
    # Elimina del diccionary alumnes, l'alumne que té com a codi codiAlumne
    # Ha de eliminar-lo també de totes les materies que estigui matriculat
    # Deletes the alumn from the dictionary and delete him from all the subjects he is enrolled
    # shuara de eliminar el codi tmb i per tant fer un buscador de codis vuits o be canviar el codi de tots els alumnes a un menys
    # tmb es podria fer un metoide per afegir un alumne a un codi q ja exiteix movent tots els sltres una posicio
    if codiAlumne in alumnes:
        a = alumnes[codiAlumne]
        for m in a.materies:
            materies[m].Alumnes.remove(a)
        alumnes.pop(codiAlumne)
    else:
        print("No existeix aquest alumne")


def eliminarMateria(codiMateria: int):
    # Eliminar la materia amb codiMateria del diccionari materies,
    # i també del diccionari a.materies de tots els alumnes que estaven matriculats d'aquella matèria
    if codiMateria in materies:
        m = materies[codiMateria]
        for a in m.Alumnes:
            a.materies.pop(codiMateria)
        materies.pop(codiMateria)


def matriculaAlumne(codiAlumne: int, codiMateria: int):
    # agafarà l'alumne a, que té com a codi codiAlumne del dicc alumnes
    # agafarà la materia m, que té com a codi codiMateria del dicc materies
    # afegirà el coidiMateria a alumne a, per tant, l'afegirà al diccionai a.Materies, amb value buit, el value serà la nota
    # afegirà l'alumne a la materia m, l'afegirà a la llista m.Alumnes
    # Tot l'anterior sempre comprovant que existeixen l'alumne i la materia
    if codiexists(codiAlumne,codiMateria) != False:
        #mirar si ja esta matriculat
        a = alumnes[codiAlumne]
        m = materies[codiMateria] #amb tkinter potser posar q surti al costat de la pantalla
        a.materies.update({codiMateria: "No avaluat"})
        m.Alumnes.append(a) #potser reduir a nomes codi per estalviar espai (mitrar mostrar notes)


def desmatriculaAlumne(codiAlumne: int, codiMateria: int):
    # Ha de fer el contrari que el métode anterior
    if codiexists(codiAlumne,codiMateria) != False:
        a = alumnes[codiAlumne]
        m = materies[codiMateria]
        a.materies.pop(codiMateria)
        m.Alumnes.remove(a)


def estaMatriculat(codiAlumne: int, codiMateria: int):
    # retornarà True si l'alumne ja està matriculat de la materia i false sinó està matriculat
    if codiexists(codiAlumne,codiMateria) != False:
        a = alumnes[codiAlumne]
        m = materies[codiMateria]
        if m in a.materies:
            return True
        else:
            return False


def posarNota(codiAlumne: int, codiMateria: int, nota: int):
    # Servirà per posar nota a l'alumne a
    # Comprovarà que l'alumne està matriculat de la materia, i després li possarà nota
    # a[codiMateria]=nota
    if codiexists(codiAlumne,codiMateria) != False:
        if estaMatriculat(codiAlumne,codiMateria) == True:
            a = alumnes[codiAlumne]
            a.materies[codiMateria] = input("Nota: ") #potser posar nota de: materia



def mostrarNotesMateria(codiMateria: int):
    # Li passarem el codi d'una Matèria i ens mostrarà per pantalla un llistat amb les següents columnes:
    # Nom Materia  CodiAlumne  NomAlumne Nota
    # Si l'alumne no té nota, mostrarà 2 guionets --
    if codiMateria in materies:
        m = materies[codiMateria]
        for a in m.Alumnes:
            print(m.nom, a.codia, a.nom, a.materies[codiMateria])
    else:
        print("No existeix aquesta materia")


def mostrarNotesAlumne(codiAlumne: int):
    # Li passarem el codi d'un alumne i ens mostrarà per pantalla un llistat amb les següents columnes:
    # Nom Materia  Nota
    # Si l'alumne no té nota, mostrarà 2 guionets --
    if codiAlumne in alumnes:
        a = alumnes[codiAlumne]
        for m in a.materies:
            print(materies[m].nom, a.materies[m].nota)
    else:
        print("No existeix aquest alumne")


def codiexists(codia: int,codim: int):
        if codia not in materies:
            print("l'alumne no existeix")
            return False
        elif codim not in materies:
            print("la materia no existeix")
            return False