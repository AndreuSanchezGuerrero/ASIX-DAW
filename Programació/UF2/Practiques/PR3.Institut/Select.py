from tkinter import *
from tkinter import ttk

class Main(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        b1 = Button(self, text="Nou Alumne", command = self.newA)
        b1.pack(side="top", padx=40, pady=40)
        b2 = Button(self, text="Nova Materia", command = self.newM)
        b2.pack(side="top", padx=40, pady=40)
        self.count = 0

    #Finestra amb el formulari per crear nous alumnes
    def newA(self):
        self.count += 1
        window = Toplevel(self).grab_set()
        a = Label(window, text="Codi:" % self.count).grid(row=0, column=0)
        a1= Entry(window).grid(row=0, column=1)
        b = Label(window, text="Nom:" % self.count).grid(row=1, column=0)
        b2= Entry(window).grid(row=1, column=1)
        c = Label(window, text="Cognom:" % self.count).grid(row=2, column=0)
        c2= Entry(window).grid(row=2, column=1)
        #desegable per triar la data de naixement
        d = Label(window, text="Data de naixement:" % self.count).grid(row=3, column=0)
        d2= Entry(window).grid(row=3, column=1)

    #Finestra amb el formulari per crear noves materies
    def newM(self):
        self.count += 1
        window = Toplevel(self).grab_set()
        label = Label(window, text="Nova Materia" % self.count)
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

if __name__ == "__main__":
    root = Tk()
    Main(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

