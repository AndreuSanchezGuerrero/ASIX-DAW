from random import randint
#random int list generator
llista = []
x = 10
for i in range(x):
    rint = randint(0, x)
    if rint not in llista:
        llista.append(rint)