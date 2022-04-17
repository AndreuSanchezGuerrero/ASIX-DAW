from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
from datetime import *
from omplir import *
from clases import *


# Finestra amb el formulari per crear nous alumnes

def nouAlumne(Nom, Cognom, d2):
    Codia = len(alumnes) + 1
    N = str(Nom.get())
    C = str(Cognom.get())
    D = str(d2.get())
    a = alumne(Codia, N, C, D)
    for i in range(0, len(alumnes)):
        if alumnes[i] == "Null":
            alumnes.update({i: a})
            showinfo(title="Info", message="Alumne creat amb codi " + str(i))
            break
        else:
            alumnes.update({Codia: a})
            showinfo(title="Info", message="Alumne creat")
        for j in materies:
            a.Materies.update({j: "Null"})
    Nom.delete(0, END)
    Cognom.delete(0, END)
    d2.delete(0, END)


def NewA():
    window = Toplevel()
    window.columnconfigure(1, weight=2)
    Label(window, text="Nom:").grid(row=1, column=0)
    Nom = Entry(window)
    Nom.grid(row=1, column=1)
    Label(window, text="Cognom:").grid(row=2, column=0)
    Cognom = Entry(window)
    Cognom.grid(row=2, column=1)
    # desegable per triar la data de naixement
    Label(window, text="Data de naixement:").grid(row=3, column=0)
    d2 = Entry(window)
    d2.grid(row=3, column=1)
    Button(window, text="Acceptar", command=lambda: nouAlumne(
        Nom, Cognom, d2)).grid(row=4, column=0)

# Finestra per eliminar alumnes

def eliminarAlumne(Codii):
    Codi = int(Codii.get())
    if Codi in alumnes:
        for m in materies:
            if Codi in materies[m].Alumnes:
                m = materies[m]
                m.Alumnes.pop(Codi)
        alumnes.pop(Codi)
        showinfo(title="Info", message="Alumne eliminat")
    else:
        showerror(title="ERROR", message="No s'ha trobat aquest codi")
    Codii.delete(0, END)


def delAl():
    window = Toplevel()
    Label(window, text="Codi de l'alumne:").grid(row=0, column=0, sticky=N)
    Codi = Entry(window)
    Codi.grid(row=0, column=2, sticky=N)
    Button(window,
            text="Eliminar",
            command=lambda: eliminarAlumne(Codi)).grid(row=1, column=0)


# Finestra amb el formulari per crear noves materies

def NewM():
    window = Toplevel()
    window.columnconfigure(1, weight=2)
    m = ""
    global codim
    Label(window,
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
            if Codi in alumnes[a].Materies:
                alumnes[a].Materies.pop(Codi)
        materies.pop(Codi)
        showinfo(title="Info", message="Alumne eliminat")
    else:
        showerror(title="ERROR", message="No s'ha trobat aquest codi")
    Codii.delete(0, END)


def delM():
    window = Toplevel()
    Label(window, text="Codi de la materia:").grid(row=0, column=0, sticky=N)
    Codi = Entry(window)
    Codi.grid(row=0, column=2, sticky=N)
    Button(window,
            text="Eliminar",
            command=lambda: eliminarMateria(Codi)).grid(row=1, column=0)


# Finestra per a matricular alumnes a les materies

def matricular(Codia, Codim):
    Codi = int(Codia.get())
    Codi2 = int(Codim.get())
    if Codi in alumnes:
        if Codi2 in materies:
            a = alumnes[Codi]
            alumnes[Codi].Materies.update({Codi2: "Null"})
            if a not in materies[Codi2].Alumnes:
                materies[Codi2].Alumnes.append(Codi)
                showinfo(title="Info", message="Alumne matriculat")
            else:
                showwarning(
                    title="WARNING", message="Aquest alumne ja esta matriculat a aquesta materia")
        else:
            showerror(title="ERROR",
                        message="No s'ha trobat aquest codi de materia")
    else:
        showerror(title="ERROR", message="No s'ha trobat aquest codi de Alumne")
    Codia.delete(0, END)
    Codim.delete(0, END)


def matA():
    # potser posar un panell amb les materies
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


# Finestra per desmatricular alumnes de les materies

def desmatricular(Codia, Codim):
    Codi = int(Codia.get())
    Codi2 = int(Codim.get())
    if Codi in alumnes:
        if Codi2 in materies:
            if Codi not in materies[Codi2].Alumnes or Codi2 not in alumnes[Codi].Materies:
                showwarning(title="WARNING",
                                message="Aquest alumne no esta matriculat a aquesta materia")
            else:
                alumnes[Codi].Materies.pop(Codi2)
                materies[Codi2].Alumnes.remove(Codi)
                showinfo(title="Info", message="Alumne desmatriculat")
                update()
        else:
            showerror(title="ERROR",
                        message="No s'ha trobat aquest codi de materia")
    else:
        showerror(title="ERROR", message="No s'ha trobat aquest codi de Alumne")
    Codia.delete(0, END)
    Codim.delete(0, END)


def DesmatA():
    # potser posar un panell amb les materies
    window = Toplevel()
    Label(window, text="Codi de l'alumne:").grid(row=0, column=0, sticky=N)
    Label(window, text="Codi de la materia:").grid(row=1, column=0, sticky=N)
    Codia = Entry(window)
    Codia.grid(row=0, column=1, sticky=N)
    Codim = Entry(window)
    Codim.grid(row=1, column=1, sticky=N)
    Button(window,
            text="Desmatricular",
            command=lambda: desmatricular(Codia, Codim)).grid(row=2, column=0)


#Finestra de les notes Alumnes
def updateNotes(window, nalumne):
    nalumne.configure(state=NORMAL)
    nalumne.delete(1.0, END)
    for i in alumnes:
        a = alumnes[i]
        nalumne.insert(INSERT, a.Nom + " " + a.Cognom + " "*(17-len(a.Nom)-len(a.Cognom)) + "Notes" + "\n")
        for j in a.Materies:
            m = materies[j]
            if a.Materies[j] == "No matriculat":
                nalumne.insert(INSERT, m.Nom + ":" + " "*(13-len(m.Nom)) + str(a.Materies[j]) + "\n")
            else:
                nalumne.insert(INSERT, m.Nom + ":" + " "*(19-len(m.Nom)) + str(a.Materies[j]) + "\n")
        nalumne.insert(INSERT, "="*28 + "\n") 
    nalumne.configure(state=DISABLED)
    window.after(5000, update)


def NotesA():
    #sha de fer el cercador de alumnes
    window = Toplevel()
    nalumne = Text(window)
    updateNotes(window, nalumne)
    nalumne.grid(row=0, column=2, rowspan=4, sticky=NS)
    scrollbar = Scrollbar(window, orient=VERTICAL, command=nalumne.yview)
    scrollbar.grid(row=0, column=3, rowspan=4, sticky=NSEW)
    nalumne["yscrollcommand"] = scrollbar.set



#Finestra de les notes Materies
def NotesM():
    pass


# Menu

menu = Tk()
menu.resizable(0, 0)
menu.geometry("700x400")
menu.title("Sa Palomera")


# Botons
na = Button(
        text="Nou Alumne",
        command=NewA).grid(row=0, column=0, sticky=NSEW)
ea = Button(
        text="Eliminar Alumne",
        command=delAl).grid(row=0, column=1, sticky=NSEW)
nm = Button(
        text="Nova Materia",
        command=NewM).grid(row=1, column=0, sticky=NSEW)
em = Button(
        text="Eliminar Materia",
        command=delM).grid(row=1, column=1, sticky=NSEW)
ma = Button(
        text="Matricular Alumne",
        command=matA).grid(row=2, column=0, sticky=NSEW)
dma = Button(
        text="Desmatricular Alumne",
        command=DesmatA).grid(row=2, column=1, sticky=NSEW)
noa = Button(
        text="Notes Alumne",
        command=NotesA).grid(row=3, column=0, sticky=NSEW)
nom = Button(
        text="Notes Materia",
        command=NotesM).grid(row=3, column=1, sticky=NSEW)


#llista autoactualitzable de alumnes (lo ideal seria que s'actualitzes a cada instant pero dona erors al fer scroll)
llista = Text(menu)
llista.grid(row=0, column=2, rowspan=4, sticky=NS)
scrollbar = Scrollbar(menu, orient=VERTICAL, command=llista.yview)
scrollbar.grid(row=0, column=3, rowspan=4, sticky=NSEW)
llista["yscrollcommand"] = scrollbar.set

def update():
    #potser posar aqui les altres llistes
    llista.configure(state=NORMAL)
    llista.delete(1.0, END)
    for i in alumnes:
        a = alumnes[i]
        llista.insert(INSERT, ("Codi: " + str(a.Codia) +
                                "\nNom: " + str(a.Nom) +
                                "\nCognom: " + str(a.Cognom) +
                                "\nData Naixement: " + str(a.DataNaixement) +
                                "\n" + "="*28 + "\n"))
    llista.configure(state=DISABLED)
    menu.after(5000, update)

update()

if __name__ == "__main__":
    menu = Menu()
    menu.mainloop()
