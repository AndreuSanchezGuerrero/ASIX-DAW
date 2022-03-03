#Si repeteixes la lletra es desconta vida
import random
random.seed()
idioma = input("Idioma (catala, castella o angles): ").lower()
f = open(idioma+".txt")
li = f.readlines()
n1 = random.randint(1,len(li))
p = li[n1]
n = int(input("nivell de dificultat de l'1 al 5: "))-1
v = [10,8,7,6,5]
v = v[n]
ld = set()
p1 = {}
for i in range(len(p)):
    p1[i] = "-"
p2 = ("".join(p1.values()))
print("La paraula es: ",p2,"\n")

while "-" in p2 and v > 0:
    v1 = 0
    l = input("Introdueix una lletra: ").upper()
    for i in range(len(p)):
        if p[i] == l:
            p1[i] = l
            v1 = v1 + 1
        ld.add(l)
    if v1 == 0:
        v = v - 1
    p2 = ("".join(p1.values()))
    print("Lletres dites: ",set(ld),"\n",p2,"\n",f"et queden {v} vides","\n","_"*20,"\n")
if v == 0:
    print("T'has quedat sense vides, la paraula era: ",p)
else:
    print("L'has encertat, la paraula es: ",p2)