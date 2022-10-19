n = input("Introdueix el teu nom:")
p = float(input("Introdueix el teu pes:"))
a = float(input("introdueix la teva alçada"))
IMC = p/(a*a)
f = "El teu pes es considera normal"
f1 = "Vigila! Pot ser que tinguis:"
f2 = ""
if IMC < 15:
    f2 = "primesa molt severa"
elif  IMC < 16:
    f2 = "primesa severa"
elif  IMC < 18.5:
    f2 = "primesa"
elif IMC < 25:
    f1 = ""
elif  IMC <30:
    f2 = "obesitat moderada"
elif  IMC <35:
    f2 = "obesitat severa"
elif  IMC <40:
    f2 = "obesitat mòrbida"
print(f"Hola {n} el teu índex de massa corporal és {IMC:.2f}""\n"f"{f}{f1} {f2}")