p = input("Introdueix una paraula: ")
for i in range(0,len(p)//2):
    if p[i].lower() == p[-(i+1)].lower():
        cc = True
    else:
        print("La paraula no es capicua")
        exit()
print("La paraula es Capicua")
