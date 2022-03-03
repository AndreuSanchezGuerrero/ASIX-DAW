n = input("Introdueix el teu nom:")
p = float(input("Introdueix el teu pes:"))
a = float(input("introdueix la teva alçada"))
IMC = p/(a*a)
if IMC >= 25:
    f = "Vigila! Segurament tinguis sobrepés"
elif  IMC <= 18.5:
    f = "Vigila! Segurament hagis de menjar més"
else:
    f = "El teu pes esta dintre del que es considera normal"
print(f"Hola {n} el teu índex de massa corporal és {IMC:.2f}""\n"f"{f}")