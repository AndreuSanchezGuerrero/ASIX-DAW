p = input("Introdueix la paraula: ").upper()
p1 = {}
for i in range(len(p)):
    p1[i] = "-"
p2 = ("".join(p1.values()))

while "-" in p2:
    print("La paraula es: ",p2,"\n")
    l = input("Introdueix una lletra: ").upper()
    for i in range(len(p)):
        if p[i] == l:
            p1[i] = l
    p2 = ("".join(p1.values()))
print("L'has encertat, la paraula es: ",p2)