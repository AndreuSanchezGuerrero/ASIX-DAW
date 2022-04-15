from curses import window
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from datetime import *
from omplir import *
from clases import *

menu = Tk()
menu.geometry("500x600")
menu.resizable(0, 0)
menu.columnconfigure(2, weight=4)
menu.title("Sa Palomera")

# Botons
na = Button(
    text="Nou Alumne",
    command=menu.newA).grid(row=0, column=0, sticky=NSEW)
ea = Button(
    text="Eliminar Alumne",
    command=menu.newAD).grid(row=0, column=1, sticky=NS)
nm = Button(
    text="Nova Materia",
    command=menu.newM).grid(row=1, column=0, sticky=NS)
em = Button(
    text="Eliminar Materia",
    command=menu.newMD).grid(row=1, column=1, sticky=NS)

# Scrollbar (no he trobat com fer q es recarregui amb els canvis)
menu.scrollbar = Scrollbar().grid(row=0, column=3, sticky=W)
menu.listbox = Listbox()
for i in alumnes:
    a = alumnes[i]
    menu.listbox.insert(END,
                        "Codi: " + str(a.Codia),
                        "Nom: " + str(a.Nom),
                        "Cognom: " + str(a.Cognom),
                        "Data Naixement: " + str(a.DataNaixement),
                        "="*20)
menu.listbox.grid(row=0, column=2, rowspan=4, sticky=NSEW)
