llista = []
frase = str(input("Frase: "))
for i in range(0,len(frase)):
    if frase[i].lower() not in llista:
        llista.append(frase[i].lower())
print (f"Les lletres de la frase: {frase} són:\n{llista}")