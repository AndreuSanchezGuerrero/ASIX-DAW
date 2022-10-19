#%%
for x in range (1, 11):
    print("#%%""\n""#Ex"+str(x)+("\n"*2))

#%%
MC = ["Seat", "Renault", "Volkswaguen", "Citroën", "Opel", "Peugeot", "Fiat", "BMW", "Mercedes", "Škoda", "Mini", "Smart", "Alfa Romeo", "Lancia", "Kia", "Hiundai", "Dacia", "Toyota", "Honda", "Misubishi", "Jeep", "Tesla"]

#%%
#Ex1
for x in range (1, 5):
    print(MC[x])

#%%
#Ex2
for x in range (len(MC)-3, len(MC))[::-1]:
    print(MC[x])

#%%
#Ex3
for x in range (1, len(MC), 2):
    print(MC[x])

#%%
#Ex4
for x in range (0, len(MC), 2):
    print(MC[x])

#%%
#Ex5
for x in range (0, 3*2, 2):
    print(MC[x])

#%%
#Ex6
for x in range (len(MC)-6, len(MC))[::-2]:
    print(MC[x])

#%%
#Ex7


#%%
#Ex8
for x in range (0, len(MC)):
    if "o" in MC[x]:
        print(MC[x])

#%%
#Ex9
for x in range (0, len(MC)):
    if len(MC[x]) > 7:
        print(MC[x])

#%%
#Ex10
v1 = []
n = 1
v = ["a","e","i","o","u"]
for x in range (0, len(MC)):
    for i in range (0, len(MC[x])):
        p = MC[x]
        if p[i] in v:
            v1.insert(n, p[i])
            n = n + 1
    if len(v1) >= 3:
        print(MC[x])
    v1.clear()

# %%
