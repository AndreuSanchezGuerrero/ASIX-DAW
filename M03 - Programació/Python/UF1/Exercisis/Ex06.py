#%%
for x in range (1, 24):
    print("#%%""\n""#Ex"+str(x)+"\n")

#%%
#Ex1
edat = int(input("Introdueix la edat"))
if edat >=18:
    print("es major de edat")
else:
    print("es menor de edat")

#%%
#Ex2
edat = int(input("Introdueix la edat"))
if edat <18:
    print("et falten "+str(18-edat)+" anys per a ser major de edat")
elif edat == 18:
    print("T’acabes d’estrenar en la majoria d’edat")
elif edat >18:
    print("Fa "+str(edat-18)+" anys que ets major d’edat")

#%%
#Ex3
edat = int(input("Introdueix la edat"))
if (18-edat)==1 or (edat-18)==1:
    any = "any"
    falta = "falta"
else:
    any = "anys"
    falta = "falten"
if edat <18:
    print("et {falta} "+str(18-edat)+f" {any} per a ser major de edat")
elif edat == 18:
    print("T’acabes d’estrenar en la majoria d’edat")
elif edat >18:
    print("Fa "+str(edat-18)+f" {any} que ets major d’edat")

#%%
#Ex4
n1 = input("numero 1")
n2 = input("numero 2")
if n1 == n2:
    print(f"{n1} i {n2} son el mateix numero")
elif n1 < n2:
    print(f"{n2} es mes gran que {n1}")
elif n1 > n2:
    print(f"{n1} es mes gran que {n2}")

#%%
#Ex5
n1 = input("numero 1")
n2 = input("numero 2")
n3 = input("numero 3")
if n1 == n2 and n2 == n3:
    print(f"{n1} i {n2} i {n3} son el mateix numero")
elif n1 >= n2 and n1 >= n3:
    print(f"{n1} es el mes gran")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} es el mes gran")
elif n3 >= n1 and n3 >= n2:
    print(f"{n1} es el mes gran")

#%%
#Ex6
nom = input("Introdueix un nom")
sexe = input("Introdueix el teu sexe M o F")
if sexe == "M":
    s = "Benvolgut"
elif sexe == "F":
    s = "Benvolguda"
else:
    print("el sexe introdüit no es valid")
print(f"{s} {nom}")

#%%
#Ex7
paraula = input("Paraula")
if paraula[:1] == "b":
    print("Comença per b")
else:
    print("no comença per b")

#%%
#Ex8
p = input("Paraula")
l = p[0].lower()
if l == "a" or l== "e" or l == "i" or l== "o" or l== "u":
    print(f"{p} comença per vocal")
else:
    print(f"{p} comença per consonant")

#%%
#Ex9
p1 = input("Primera paraula")
p2 = input("Segona paraula")
if p1[-3:] == p2[-3:]:
    print(f"{p1} i {p2} rimen")
else:
    print(f"{p1} i {p2} no rimen")

#%%
#Ex10
p = input("Introudeix una paraula de 3 lletres")
if len(p) != 3:
    print("Paraula no valida")
elif p[0] == p[2]:
    print("La paraula es Capicua")
else:
    print("no es cap i cua")

#%%
#Ex11
p = input("Introudeix una paraula de 1-5 lletres")
p1 = p[::-1]
n = int(len(p)/2)
if len(p) > 5:
    print("Paraula no valida")
elif p == p1:
    print("La paraula es Capicua")
else:
    print("La paraula no es capicua")

#%%
#Ex12
dia = int(input("Introdueix la teva data de naixement numericament, dia"))
mes = int(input("mes"))
any = int(input("any"))
dia1 = int(input("introdueix la data actual numericament, dia"))
mes1 = int(input("mes"))
any1 = int(input("any"))
if dia-dia1<0 and mes-mes1<0:
    print(f"El teu aniversari vas ser el {dia}/{mes}/{any1}")
elif dia-dia1 ==0 and mes-mes1==0:
    print("El teu aniversari es avui")
elif dia-dia1 >0 and mes-mes1>0:
    print(f"El teu aniversari serà el {dia}/{mes}/{any1}")
else:
    print("jaja no k pasao")

#%%
#Ex13
edat = int(input("Introdueix la teva edat:"))
if edat >= 0:
    print(f"Tens {edat//5} lustres")
else:
    print("l'edat no es valida")

#%%
#Ex14
edat = int(input("Introdueix la edat del nen/a"))
if edat >=0 and edat<18:
    print("l'edat es valida")
else:
    print("l'edat no es valida ja que es surt del rang establert")

#%%
#Ex15
c1 = float(input("Intrudueix el que mesuren els costats del triangle, d'un en un"))
c2 = float(input("Costat 2"))
c3 = float(input("Costat 3"))
if c1==c2 and c2==c3:
    print(f"El triangle es equilater ja que tots els seus costats mesuren {c1}cm")
else:
    print("El triangle no es equilater")

#%%
#Ex16
c1 = float(input("Intrudueix el que mesuren els costats del triangle, d'un en un"))
c2 = float(input("Costat 2"))
c3 = float(input("Costat 3"))
if c1>0 and c2>0 and c3>0:
    if c1==c2 and c2==c3:
        print(f"El triangle es equilater ja que tots els seus costats mesuren {c1}cm")
    else:
        print("El triangle no es equilater")
else:
    print("Les mesures no son valides")

#%%
#Ex17
c1 = float(input("Intrudueix el que mesuren els costats del triangle, d'un en un"))
c2 = float(input("Costat 2"))
c3 = float(input("Costat 3"))
if c1>0 and c2>0 and c3>0: #triangle valid
    if c1==c2 and c2==c3: #equilater
        print(f"El triangle es equilater ja que tots els seus costats mesuren {c1}cm")
    elif c1==c2 and c1>c3 or c2==c3 and c2>c1 or c3==c1 and c3>c1: #isósceles
        print("El triangle es isósceles")
    else:
        print("El triangle es escalé")
else:
    print("Les mesures no son valides")

#%%
#Ex18
paraula1 = input("Primera paraula: ")
paraula2 = input("Segona paraula: ")
if paraula1<paraula2:
    print(f"{paraula1}\n{paraula2}")
else:
    print(f"{paraula2}\n{paraula1}")

#%%
#Ex19
any = int(input("Introdueix un any"))
if (any%400)==0:
    print(f"{any} es un any de trespàs")
elif (any%4)==0 and (any%100)!=0:
    print(f"{any} es un any de trespàs")
else:
    print(f"{any} no es un any de trespàs")

#%%
#Ex20
Setmana = {
    "0": "Diumenge",
    "1": "Dilluns",
    "2": "Dimarts",
    "3": "Dimecres",
    "4": "Dijous",
    "5": "Divendres",
    "6": "Dissabte",
}
dia = int(input("Introdueix el dia"))
mes = int(input("Introdueix el mes"))
any = int(input("Introdueix l'any"))
a = (14 - mes) // 12
y = any - a
m = mes + 12 * a - 2

if dia in range(4, 17) and mes==10 and any==1582:
    print("Aquesta data no existeix jaja salu2")
elif any==1582:
    if dia in range(1, 4) and mes in range(1, 10): #calendari Gregorià
        d = (dia + y + y/4 - y/100 + y/400 + (31*m)/12) % 7
        d = int(d)
        d = str(d)
        set = Setmana[d]
        print(f"El {dia}/{mes}/{any} es un {set}")
    elif dia in range(17, 31) and mes in range(10, 12): #calendari Julià
        d = (5 + dia + y + y/4 + (31*m)/12) % 7
        d = int(d)
        d = str(d)
        set = Setmana[d]
        print(f"El {dia}/{mes}/{any} es un {set}")
    else:
        print("error1")
else:
    if any>1582:
        d = (dia + y + y/4 - y/100 + y/400 + (31*m)/12) % 7
        d = int(d)
        d = str(d)
        set = Setmana[d]
        print(f"El {dia}/{mes}/{any} es un {set}")
    elif any<1582:
        d = (5 + dia + y + y/4 + (31*m)/12) % 7
        d = int(d)
        d = str(d)
        set = Setmana[d]
        print(f"El {dia}/{mes}/{any} es un {set}")
    else:
        print("error2")

#%%
#Ex21


#%%
#Ex22


#%%
#Ex23