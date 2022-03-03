voc = []
resta = []
frase = str(input("Frase: "))
for i in range(0,len(frase)):
    if frase[i].lower() in ("a","e","i","o","u"):
        if (frase[i].lower()) not in voc:
            voc.append(frase[i].lower())
    else:
        if (frase[i].lower()) not in resta:
            resta.append(frase[i].lower())
print (f"Les vocals de la frase: {frase} són:\n{voc}\nLa resta de caracters de la frase: {frase} són:\n{resta}")