lletres = str(input("introdueix una cadena de lletres: "))
p=""
for char in lletres:
    if char not in p:
        p=p+char
print(sorted(list(p)))
