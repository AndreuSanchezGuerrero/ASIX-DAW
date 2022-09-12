#per evitar complicacions assumire que mai s'intrduira el mateix numero dos cops
n1 = float(input("Primer numero:"))
n2 = float(input("Segon número:"))
print(f"Format amb dos decimals: {n1:.2f} i {n2:.2f}")
print(f"Format amb 0 decimals i agrupant milers: {n1:,.0f} i {n2:,.0f}")
if n1 < n2:
    p = n1
    g = n2
    #aqui
elif n1 > n2:
    p = n2
    g = n1
    #o aqui
print("Numeros ordenats""\n""--------------------------------------""\n"f"Més petit:       {p:.3f}""\n"f"Mes gran:        {g:.3f}")