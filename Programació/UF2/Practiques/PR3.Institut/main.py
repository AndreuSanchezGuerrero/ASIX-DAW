from tkinter import *
from tkinter import ttk

root = Tk()
root.title('SaPalomera')
root.geometry('600x400+50+50')
root.resizable(False, False)#treureho si ajustantla no es descuadra
icon=PhotoImage('Programació/UF2/Practiques/PR3.Institut/sapa.ico')#no funciona
root.iconphoto(True,icon)

root.mainloop()









opcions = ("Mostrar Pacients","Cercar Pacient","Afegir","Canviar l'estat","Calcular edat","Pacients en estat X","Pacients Contagiats dia X","Pacients en Estat i Data","Sortir")
fi = False

while not fi:
    pass
    input("Presiona enter per continuar")
    clear() 
    for i,opcio in enumerate(opcions):
        print(f"{i+1:2}. {opcio}")
    #Escollir opcio
    opcio = escullOpcio(len(opcions))
    if opcio == "1":
        #mostrar tots els pacients
        mostrarPacients(pacients)
    elif opcio == "2":
        cercarPacient(pacients,int(input("Introdueix el codi: ")),0)
    elif opcio == "3":
        #Afegir Pacient"
        p = nouPacient(codi)
    elif opcio == "4":
        #Modificar Estat
        cercarPacient(pacients,int(input("Introdueix el codi: ")),1)
    elif opcio == "5":
        cercarPacient(pacients,int(input("Introdueix el codi: ")),2)
    elif opcio == "6":
        pacientsEstat(pacients,estats) #L'estat no li passem, el demanarà dins
    elif opcio == "7":
        pacientsData(pacients)
    elif opcio == "8":
        pacientsEstatData(pacients)
    elif opcio == "9":
        fi = True