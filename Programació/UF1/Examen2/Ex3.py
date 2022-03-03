n = input("Nom:")
ts = int(input("Tensió Sistòlica: "))
td = int(input("Tensió Disastòlica: "))
if ts > 180 or td > 110:
    nt = "Crisi Hipertensiva"
elif ts >= 160 or td >= 100:
    nt = "Hipertensió Grau 2(HTA2)"
elif ts in range(140,159) or td in range(90,99):
    nt = "Hipertensió Grau 1(HTA1)"
elif ts in range(120,139) or td in range(80,89):
    nt = "Prehipertensió"
elif ts in range(80,119) and td in range(60,79):
    nt = "Normal"
elif ts < 80 or td < 60:
    nt = "Hipotensió"
print("Nivell de tensió:",nt)