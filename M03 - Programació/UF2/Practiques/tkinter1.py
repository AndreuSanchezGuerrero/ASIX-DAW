from tkinter import *
from functools import partial

def saludar(partDia):
    if partDia.lower() == "matí":
        iniciS = "Bon dia"
    elif partDia.lower() == "tarda":
        iniciS = "Bona tarda"
    else:
        iniciS ="Bona nit"       
    salutacio = f"{iniciS} {entNom.get()} {entCognoms.get()}"
    lbSalutacio.config(text=salutacio)

finestra = Tk()
finestra.title("Exemple Tkinter")
lbNom = Label(finestra,text="Nom")
lbCognoms = Label(finestra,text="Cognoms")
entNom = Entry(finestra)
entCognoms = Entry(finestra)
btMati = Button(finestra,text="Matí",command=partial(saludar,"matí"))
btTarda = Button(finestra,text="Tarda",command=lambda: saludar(btTarda.cget('text')))
btNit = Button(finestra,text="Nit",command=partial(saludar,"nit"))
lbSalutacio = Label(finestra,text="Aquí et saludaré")

lbNom.grid(row=0)
entNom.grid(row=0,column=1)
lbCognoms.grid(row=1)
entCognoms.grid(row=1,column=1)
btMati.grid(row=3,column=0)
btTarda.grid(row=3,column=1)
btNit.grid(row=3,column=2)
lbSalutacio.grid(row=4,columnspan=2)

mainloop()
