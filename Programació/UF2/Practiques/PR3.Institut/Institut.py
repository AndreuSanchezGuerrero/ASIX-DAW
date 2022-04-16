from curses import window
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from datetime import *
from omplir import *
from clases import *


# Finestra amb el formulari per crear nous alumnes
def nouAlumne():
    #avisar de quin codi se li ha assignat
    #sha de fer el buscador de codis vuits
    pass

def NewA():
    window = Toplevel()
    window.columnconfigure(1, weight=2)
    Label(window, text="Nom:").grid(row=1, column=0)
    Nom = Entry(window).grid(row=1, column=1)
    Label(window, text="Cognom:").grid(row=2, column=0)
    Cognom = Entry(window).grid(row=2, column=1)
    # desegable per triar la data de naixement
    Label(window, text="Data de naixement:").grid(row=3, column=0)
    d2 = Entry(window).grid(row=3, column=1)
    Button(window, text="Acceptar", command=lambda: nouAlumne(Nom,Cognom,d2)).grid(row=4, column=0)

# Finestra per eliminar alumnes
def eliminarAlumne(Codii):
    Codi = int(Codii.get())
    if Codi in alumnes:
        for m in materies:
            materies[m].Alumnes.pop(Codi)
        alumnes.pop(Codi)
        showinfo(title="Info", message="Alumne eliminat")
        update()
    else:
        showerror(title="ERROR", message="No s'ha trobat aquest codi")
    Codii.delete(0, END)

def delAl():
    window = Toplevel()
    Label(window, text="Codi de l'alumne:").grid(row=0, column=0, sticky=N)
    Codi = Entry(window)
    Codi.grid(row=0, column=2, sticky=N)
    Button( window,
            text="Eliminar",
            command=lambda: eliminarAlumne(Codi)).grid(row=1, column=0)

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
def eliminarMateria(Codii):
    Codi = int(Codii.get())
    if Codi in materies:
        for a in alumnes:
            alumnes[a].Materies.pop(Codi)
        materies.pop(Codi)
        showinfo(title="Info", message="Alumne eliminat")
        update()
    else:
        showerror(title="ERROR", message="No s'ha trobat aquest codi")
    Codii.delete(0, END)

def delM():
    window = Toplevel()
    Label(window, text="Codi de la materia:").grid(row=0, column=0, sticky=N)
    Codi = Entry(window)
    Codi.grid(row=0, column=2, sticky=N)
    Button( window,
            text="Eliminar",
            command=lambda: eliminarMateria(Codi)).grid(row=1, column=0)

#Finestra per a matricular alumnes a les materies
def matricular(Codia, Codim):
    Codi = int(Codia.get())
    Codi2 = int(Codim.get())
    if Codi in alumnes:
        if Codi2 in materies:
            a = alumnes[Codi]
            alumnes[Codi].Materies.update({Codi2: "Null"})
            if a not in materies[Codi2].Alumnes:
                materies[Codi2].Alumnes.append(a)
                showinfo(title="Info", message="Alumne matriculat")
                update()
            else:
                showwarning(title="WARNING", message="Aquest alumne ja esta matriculat a aquesta materia")
        else:
            showerror(title="ERROR", message="No s'ha trobat aquest codi de materia")
    else:
        showerror(title="ERROR", message="No s'ha trobat aquest codi de Alumne")
    Codia.delete(0, END)
    Codim.delete(0, END)

def matA():
    #potser posar un panell amb les materies
    window = Toplevel()
    Label(window, text="Codi de l'alumne:").grid(row=0, column=0, sticky=N)
    Label(window, text="Codi de la materia:").grid(row=1, column=0, sticky=N)
    Codia = Entry(window)
    Codia.grid(row=0, column=1, sticky=N)
    Codim = Entry(window)
    Codim.grid(row=1, column=1, sticky=N)
    Button(window,
            text="Matricular",
            command=lambda: matricular(Codia, Codim)).grid(row=2, column=0)


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
    command=delAl).grid(row=0, column=1, sticky=NS)
nm = Button(
    text="Nova Materia",
    command=NewM).grid(row=1, column=0, sticky=NS)
em = Button(
    text="Eliminar Materia",
    command=delM).grid(row=1, column=1, sticky=NS)
ma = Button(
    text="Matricular Alumne",
    command=matA).grid(row=2, column=0, sticky=NS)

# Scrollbar (no he trobat com fer q es recarregui amb els canvis)
scrollbar = Scrollbar(menu).grid(row=0, column=3, sticky=W)
llista = Text(menu)
def update():
    llista.configure(state=NORMAL)
    llista.delete(1.0, END)
    for i in alumnes:
        a = alumnes[i]
        llista.insert(INSERT, ("Codi: " + str(a.Codia) + "\nNom: " + str(a.Nom) + "\nCognom: " + str(a.Cognom) + "\nData Naixement: " + str(a.DataNaixement) + "\n" + "="*25 + "\n"))
    llista.configure(state=DISABLED)
    llista.grid(row=0, column=2, rowspan=4, sticky=NSEW)

update()

if __name__ == "__main__":
    menu = Menu()
    menu.mainloop()
