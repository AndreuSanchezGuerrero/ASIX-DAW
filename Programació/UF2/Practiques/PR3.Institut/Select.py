from tkinter import *
from tkinter import ttk
from datetime import *
from omplir import *
from clases import *
from Institut import *

class Main(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        b1 = Button(self, text="Nou Alumne", command = self.newA).grid(row=0, column=0)
        b2 = Button(self, text="Nova Materia", command = self.newM).grid(row=0, column=1)

    #Finestra amb el formulari per crear nous alumnes
    def newA(self): 
        window = Toplevel(self).grab_set()
        a = ""
        c = Label(window, text="Codi:").grid(row=0, column=0)
        Codia = Entry(window).grid(row=0, column=1)
        n = Label(window, text="Nom:").grid(row=1, column=0)
        Nom= Entry(window).grid(row=1, column=1)
        co = Label(window, text="Cognom:").grid(row=2, column=0)
        Cognom= Entry(window).grid(row=2, column=1)
        #desegable per triar la data de naixement
        d = Label(window, text="Data de naixement:").grid(row=3, column=0)
        d2= Entry(window).grid(row=3, column=1)
        a = alumne(Codia,Nom,Cognom,d2)
        e = Button(window, text="Acceptar", command = self.alumnes.update({Codia:a})).grid(row=4, column=0)

    #Finestra amb el formulari per crear noves materies
    def newM(self):
        window = Toplevel(self).grab_set()
        m = ""
        global codim
        n = Label(window, text="Nom:").grid(row=0, column=0)
        Nom = Entry(window).grid(row=0, column=1)
        m = materia(codim, Nom)
        e = Button(window, text="Acceptar", command = self.materies.update({codim:m})).grid(row=1, column=0)

if __name__ == "__main__":
    root = Tk()
    Main(root)
    root.mainloop()

