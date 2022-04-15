from curses import window
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from datetime import *
from omplir import *
from clases import *


def eliminarAlumne(codiAlumne: int):
    if codiAlumne in alumnes:
        a = alumnes[codiAlumne]
        for m in a.materies:
            materies[m].Alumnes.remove(a)
        alumnes.pop(codiAlumne)
        showinfo(title="Info", message="Alumne eliminat")
    else:
        showerror(title="ERROR", message="No s'ha trobat aquest codi")

# Finestra amb el formulari per crear nous alumnes


def NewA():
    window = Toplevel()
    window.columnconfigure(1, weight=2)
    a = ""
    Label(window, text="Codi:").grid(row=0, column=0, sticky=N)
    Codia = Entry(window).grid(row=0, column=1, sticky=N)
    Label(window, text="Nom:").grid(row=1, column=0)
    Nom = Entry(window).grid(row=1, column=1)
    Label(window, text="Cognom:").grid(row=2, column=0)
    Cognom = Entry(window).grid(row=2, column=1)
    # desegable per triar la data de naixement
    Label(window, text="Data de naixement:").grid(row=3, column=0)
    d2 = Entry(window).grid(row=3, column=1)
    a = alumne(Codia, Nom, Cognom, d2)
    Button(window, text="Acceptar", command=alumnes.update(
        {Codia: a})).grid(row=4, column=0)

# Finestra per eliminar alumnes


def NewAD():
    window = Toplevel()
    Label(window, text="Codi de l'alumne:").grid(row=0, column=0, sticky=N)
    Codia = Entry(window).grid(row=0, column=1)
    Button( window,
            text="Eliminar",
            command=eliminarAlumne(Codia)).grid(row=1, column=0)

# Finestra amb el formulari per crear noves materies


def NewM():
    window = Toplevel()
    window.columnconfigure(1, weight=2)
    m = ""
    global codim
    Label(  window,
            text="Nom:").grid(row=0, column=0, sticky=N)
    Nom = Entry(window).grid(row=0, column=1, sticky=N)
    m = materia(codim, Nom)
    Button(window,                
            text="Acceptar",
            command=materies.update({codim: m})).grid(row=1, column=0)

# Finestra per eliminar materies


def NewMD():
    window = Toplevel()
    Label(window, text="Codi de la materia:").grid(row=0, column=0, sticky=N)
    Codim = Entry(window).grid(row=0, column=1, sticky=N)
    Button(window,
            text="Eliminar",
            command=materies.update({Codim: ""})).grid(row=1, column=0)

# Menu

menu = Tk()
menu.geometry("500x600")
menu.resizable(0, 0)
menu.columnconfigure(2, weight=4)
menu.title("Sa Palomera")

# Botons
na = Button(
    text="Nou Alumne",
    command=NewA).grid(row=0, column=0, sticky=NSEW)
ea = Button(
    text="Eliminar Alumne",
    command=NewAD).grid(row=0, column=1, sticky=NS)
nm = Button(
    text="Nova Materia",
    command=NewM).grid(row=1, column=0, sticky=NS)
em = Button(
    text="Eliminar Materia",
    command=NewMD).grid(row=1, column=1, sticky=NS)

# Scrollbar (no he trobat com fer q es recarregui amb els canvis)
scrollbar = Scrollbar().grid(row=0, column=3, sticky=W)
listbox = Listbox()
for i in alumnes:
    a = alumnes[i]
    listbox.insert(END,
                    "Codi: " + str(a.Codia),
                    "Nom: " + str(a.Nom),
                    "Cognom: " + str(a.Cognom),
                    "Data Naixement: " + str(a.DataNaixement),
                    "="*20)
listbox.grid(row=0, column=2, rowspan=4, sticky=NSEW)


if __name__ == "__main__":
    menu = Menu()
    menu.mainloop()
