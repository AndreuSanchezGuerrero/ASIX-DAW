def taula():
    e = " "*25
    g = "-"*57
    #si hi ha mes de 9 pacients de un tipus donara error pero com q no nhi han a la llista introduïda no passarà
    print(f"Nivell de Tensió{e}Núm. de pacients\n{g}")
    print("Hipotensió",HP,sep=" "*40)
    print("Normal",N,sep=" "*44)
    print("Prehipertensió",PH,sep=" "*36)
    print("Hipertensió Grau 1(HTA1)",HTA1,sep=" "*26)
    print("Hipertensió Grau 2(HTA2)",HTA2,sep=" "*26)
    print("Crisi Hipertensiva",CH,sep=" "*32)

pacients = [["Joan",145,75],["Marta",128,74],["Paco",120,60],["Maria",185,95],["Anna",165,90]]
CH = 0
HTA1 = 0
HTA2 = 0
PH = 0
N = 0
HP = 0

for x in range(len(pacients)):
    pacient = pacients[x]
    ts = pacient[1]
    td = pacient[2]
    if ts > 180 or td > 110:
        CH = CH + 1
    elif ts >= 160 or td >= 100:
        HTA2 = HTA2 + 1
    elif ts in range(140,159) or td in range(90,99):
        HTA1 = HTA1 + 1
    elif ts in range(120,139) or td in range(80,89):
        PH = PH + 1
    elif ts in range(80,119) and td in range(60,79):
        N = N + 1
    elif ts < 80 or td < 60:
        HP = HP + 1

print(taula())