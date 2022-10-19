def eliminaLletra(p,l):
    novaparaula = ""
    for i in range(0,len(p)):
        if p[i] == l:
            novaparaula = novaparaula + "*"
        else:
            novaparaula = novaparaula + p[i]
    return novaparaula

p = str(input("Paraula:"))
l = "a"
print(eliminaLletra(p,l))