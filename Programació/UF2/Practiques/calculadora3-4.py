#esriu de dreta a esquerra

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from functools import partial

finestra = Tk()
finestra.geometry("+{0}+{1}".format(200,300))
btSor = Button(finestra,text='Sortir',width=8,command=quit)
btSor.grid(row=0,column=0)

#Display
entRes = Entry(finestra)
entRes.grid(row=0,column=1,columnspan=2)
entRes.place(x=75,y=2,width=150, height=24)
entRes.configure(state='readonly')

#Calculs
def afegirOperacio(op):
    if str(entRes.get())[-1] not in ope:
        l = len(entRes.get())
        entRes.configure(state='normal')
        entRes.insert(l,op)
        entRes.configure(state='readonly')

def afegirDigit(d):
    l = len(entRes.get())
    entRes.configure(state='normal')
    entRes.insert(l,d)
    entRes.configure(state='readonly')

def calcula():
    try:
        res = float(eval(entRes.get()))
        entRes.configure(state='normal')
        entRes.delete(0,END)
        entRes.insert(0,str(res))
    except ValueError:
        messagebox.showwarning("Error","N1 i N2 han de ser números")
    except ZeroDivisionError:
        messagebox.showwarning("Error","No es pot dividir per 0")
    except:
        messagebox.showwarning("Error","Error variat")
    entRes.configure(state='readonly')

btig = Button(finestra,text='=',width=9, command=calcula)
btig.grid(row=5,column=2)

#Eliminar Tot
def clearDisplay():
    entRes.configure(state='normal')
    entRes.delete(0,END)
    entRes.configure(state='readonly')
btce = Button(finestra,text='CE',width=9,command=clearDisplay)
btce.grid(row=5,column=0)

#Eliminar Digit
def popDisplay():
    l = len(entRes.get())-1
    entRes.configure(state='normal')
    entRes.delete(l,END)
    entRes.configure(state='readonly')
btdd = Button(finestra,text='<-',width=4,command=popDisplay)
btdd.grid(row=0,column=3)

#Numeros
r = 1
c = 0
for i in range(0,10):
    x = i
    if i % 3 == 0:
        r = r + 1
        c = 0
    if x == 9:
        c = 1
        x = -1
    ttk.Button(text=x+1,command=partial(afegirDigit,x+1)).grid(row=r,column=c)
    c = c + 1

#Operacions
ope = ["(",")","+","-","*","/"]
for i in range(0,6):
    if i <= 1:
        ttk.Button(text=ope[i],width=4,command=partial(afegirOperacio,ope[i])).grid(row=0,column=i+4)
    else:
        ttk.Button(text=ope[i],width=18,command=partial(afegirOperacio,ope[i])).grid(row=i,column=3,columnspan=3)

res = ""
mainloop()



