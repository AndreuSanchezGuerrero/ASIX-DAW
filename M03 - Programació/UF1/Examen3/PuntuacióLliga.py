import re
pp = {}
res = [["Barça",2,"Espanyol",3], ["Betis",1,"Sevilla",0], ["Espanyol",2,"Betis",2], ["Sevilla",0,"Barça",1],["Betis",3,"Barça",2], ["Espanyol",1,"Sevilla",1]]
for i in range(0,len(res)):
    grup = res[i]
    for i in range(0,len(grup)):
        equip = ""
        if grup[i] not in pp:
            if i%2 == 0:
                pp[grup[i]] = 0
        if i%2 != 0:
            equip = grup[i-1]
            pp[equip] = pp[equip] + grup[i]
print (pp)

print(f"Equip    Punts\n{'-'*12}")
for i in range(0,len(pp)):
    print(pp[i],"     ",)