from tkinter import *
from tkinter import ttk
from datetime import *
from omplir import *
from clases import *
from Institut import *

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
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=6)
        self.title("Sa Palomera")
        Button(self, 
                text="Nou Alumne", 
            command = self.newA).grid(row=0, column=0)
        Button(self, 
                text="Nova Materia", 
            command = self.newM).grid(row=0, column=1)
        Scrollbar(self,
        orient='vertical',
        command=llistaAlumnes.yview
        ).grid(row=0, column=2)
    def newA(self):
        window = NewA(self)
        window.grab_set()
    def newM(self):
        window = NewM(self)
        window.grab_set()

if __name__ == "__main__":
    menu = Menu()
    menu.mainloop()

