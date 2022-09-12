def majorLlista(llista):
    majorLlista = 0
    for i in range(0,len(llista)):
        if majorLlista < llista[i]:
            majorLlista = llista[i]
    return majorLlista

llista = [2,5,9,0,67,4,6]

print(majorLlista(llista))