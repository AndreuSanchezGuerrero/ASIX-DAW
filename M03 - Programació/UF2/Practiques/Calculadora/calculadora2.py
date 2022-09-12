from tkinter import *
from tkinter import messagebox
from functools import partial

def calcula(op):
    try:
        res = eval(str(entN1.get())+op+str(entN2.get()))
        entRes.configure(state='normal')
        entRes.delete(0,END)
        entRes.insert(0,str(res))
        entRes.configure(state='readonly')
    except ValueError:
        messagebox.showwarning("Error","N1 i N2 han de ser números")
    except ZeroDivisionError:
        messagebox.showwarning("Error","No es pot dividir per 0")
    except:
        messagebox.showwarning("Error","Error variat")


finestra = Tk()

lbN1 = Label(finestra,text='N1')
lbN1.grid(row=0)

lbN2 = Label(finestra,text='N2')
lbN2.grid(row=1)

lbRes = Label(finestra,text='Resultat')
lbRes.grid(row=2)

entN1 = Entry(finestra)
entN1.grid(row=0,column=1,columnspan=4)

entN2 = Entry(finestra)
entN2.grid(row=1,column=1,columnspan=4)

entRes = Entry(finestra)
entRes.grid(row=2,column=1,columnspan=4)
entRes.configure(state='readonly')

btSor = Button(finestra,text='Sortir',command=quit)
btSor.grid(row=3,column=0)

btSum = Button(finestra,text='+',command=partial(calcula,"+"))
btSum.grid(row=3,column=1)

btRes = Button(finestra,text='-',command=partial(calcula,"-"))
btRes.grid(row=3,column=2)

btMult = Button(finestra,text='*',command=partial(calcula,"*"))
btMult.grid(row=3,column=3)

btDiv = Button(finestra,text='/',command=partial(calcula,"/"))
btDiv.grid(row=3,column=4)

finestra.geometry("+{0}+{1}".format(200,300))
mainloop()



