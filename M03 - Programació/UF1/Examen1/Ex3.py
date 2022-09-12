n = input("Introdueix el teu nom:")
p = float(input("Introdueix el teu pes (kg):"))
a = float(input("introdueix la teva alçada (cm)"))
p1 = p/0.45359237
a1 = int(a//30)
a2 = int((a%30)/2.54)
print(f"Hola {n}, peses {p1:.2f} Lbs i tens una alçada de {a1}'{a2}",end='"')