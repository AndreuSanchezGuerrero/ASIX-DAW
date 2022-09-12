#posar q no hi hagi jugador 1
#acabar de arreglar q no doni error cuan hi ha trampa amb un if als bucles q comprovi la llista

nplay = int(input("Introdueix el numero de jugadors: "))
while nplay < 2:
    print("Número de jugadors no valid")
    nplay = int(input("Introdueix el numero de jugadors: "))
nplay1 = nplay 

#diccionari de variables amb les pedres q es creuen en total
pe = []
for i in range(0, nplay):
    pe.append(0)
#diccionari amb els punts
pu = []
for i in range(0, nplay):
    pu.append(0)
#diccionari amb les pedres a jugar
pm = []
for i in range(0, nplay):
    pm.append(0)
#n ronda
x = 0
#variable per determinar si algun jugador ha guanyat la ronda
punt = 0
#llista per a mirar q pe no estigui repetit
pe1 = []
#numero de jugador
nju = 0

while 3 not in pu and nplay >= 2: 
    print("Ronda:",x + 1)
    #per a determinar el numero de pedres que volen jugar
    for i in range(0,nplay):
        if pu[i] < 999:
            pm[i] = int(input(f"Jugador {i}, quantes pedres vols jugar: "))
            if pm[i] > 3 or pm[i] < 0:
                print("Has fet trampa, eliminat")
                pm[i] = 0
                pu[i] = 999
                nplay1 = nplay1 - 1
    #per a determinar cuantes pedres creuen q hi han
    print("Recorda que el numero màxim de pedres que hi ha en joc son:",nplay1*3)
    for i in range(0,nplay):
        if i != 0:
            nju = nju + 1
        if nju >= nplay:
            nju = 0
        if pu[nju] < 999:
            pe[i] = int(input(f"Jugador {nju} quantes pedres creus que hi ha: "))#es conten les del jugador eliminat en aquesta part de codi
            if pe[i] > (nplay*3) or pe[i] < pm[i] or pe[i] in pe1:
                print("Has fet trampa, eliminat")
                pe[i] = 0
                pu[i] = 999
                nplay1 = nplay1 - 1
            else:
                pe1.append(pe[i])
    nju = x + 1
    pe1 = []
    pet = sum(pm)
    if x != 0:
        pe = pe[-x:] + pe[:-x]
    for i in range(0,nplay):
        if pe[i] == pet:
            pu[i] = pu[i] + 1
            punt = punt + 1
            print(f"Punt per al jugador {i}, hi havia {pet} pedres")
        pm[i] = 0
    if punt == 0:
        print(f"Cap jugador ha encertat, hi havia {pet} pedres")
    x = x + 1
    punt = 0

#diu el guanyador i genera una llista amb els punts
for i in range(0,nplay):
    if pu[i] == 3:
        print("Ha guanyat el jugador",i)
    if pu[i] < 999:
        print("Jugador",i," "*10,pu[i])