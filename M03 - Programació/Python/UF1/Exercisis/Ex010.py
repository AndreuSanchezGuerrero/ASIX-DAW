#%%
for x in range (1, 16):
    print("#%%""\n""#Ex"+str(x)+("\n"*2))

#%%
NacionalitatMarca = {
    "Seat":         "Espanya",
    "Renault":      "França",
    "Volkswaguen":  "Alemanya",
    "Citroën":      "França",
    "Opel":         "Alemanya",
    "Peugeot":      "França",
    "Fiat":         "Itàlia",
    "BMW":          "Alemanya",
    "Mercedes":     "Alemanya",
    "Škoda":        "Txèquia",
    "Mini":         "Regne Unit",
    "Smart":        "Alemanya",
    "Alfa Romeo":   "Itàlia",
    "Lancia":       "Itàlia",
    "Kia":          "Corea del Sud",
    "Hiundai":      "Corea del Sud",
    "Dacia":        "Rumania",
    "Toyota":       "Japó",
    "Honda":        "Japó",
    "Misubishi":    "Japó",
    "Jeep":         "EEUU",
    "Tesla":        "EEUU"
}

Aules = {"1A","1B","1C","2A","2B","2C","3A","3B","4A","4B","A1","A2","A3","A4"}
AulesOcupades = {"1A","1C","2A","3A","3B","4A"}
AulesDiversitat1 = {"1A","2A","3A","4A"}
AulesDiversitat2 = {"1B","2B","3B","4B"}

AulesSMX = {"A1","A3","A4"}
AulesASIX = {"A2","A3"}

MC = ["Seat", "Renault", "Volkswaguen", "Citroën", "Opel", "Peugeot", "Fiat", "BMW", "Mercedes", "Škoda", "Mini", "Smart", "Alfa Romeo", "Lancia", "Kia", "Hiundai", "Dacia", "Toyota", "Honda", "Misubishi", "Jeep", "Tesla"]
#%%
#Ex1
print("Aules lliures:")
for x in Aules:
    if x not in AulesOcupades:
        print(x)

#%%
#Ex2
print(AulesDiversitat2 | AulesDiversitat1)

#%%
#Ex3
print(AulesASIX & AulesSMX)

#%%
#Ex4
print(len(Aules))

#%%
#Ex5
MC.append("Ferrari")
print(MC)
#%%
#Ex6
print(NacionalitatMarca["Mini"])

#%%
#Ex7
NacionalitatMarca["Mini"] = "Alemanya"

#%%
#Ex8
NacionalitatMarca["Ferrari"] = "Italia"
print(NacionalitatMarca)

#%%
#Ex9


#%%
#Ex10


#%%
#Ex11


#%%
#Ex12


#%%
#Ex13


#%%
#Ex14


#%%
#Ex15



