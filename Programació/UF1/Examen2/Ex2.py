def taula():
    e = " "*5
    g = "-"*20
    e2 = " "*18
    e3 = " "*12
    #si hi ha mes de 9 nùmeros amb les mateixes xifres donara error pero com q no nhi han a la llista introduïda no passarà
    print(f"Xifres{e}Quantitat\n{g}\n1{e2}{x1}\n2{e2}{x2}\n3 o més{e3}{x3}\n")

llista = [1,34,56,789,6,789,23,23,244,67997,7896]
x1 = 0
x2 = 0
x3 = 0

for x in range(len(llista)):
    llista[x] = str(llista[x])
    if len(llista[x]) == 1:
        x1 = x1 + 1
    if len(llista[x]) == 2:
        x2 = x2 + 1
    if len(llista[x]) >= 3:
        x3 = x3 + 1

print(taula())