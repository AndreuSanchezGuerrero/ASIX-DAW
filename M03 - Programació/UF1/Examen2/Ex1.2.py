#comprovar si les paraules aturada funcionen upper, down or amb accents
x = 0
p = ""
f = []
paraulesdAturada = ["Stop","Parar","Aturar","Arrêter","Haltu"]

while x <= 10:
    p = input("Introdueix una paraula: ")
    for x in range(len(paraulesdAturada)):
        if p == paraulesdAturada[x]:
            quit
    f.append(p)
    x = x + 1
print(" ".join(f))