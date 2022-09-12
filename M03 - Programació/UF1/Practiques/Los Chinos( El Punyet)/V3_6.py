#posar q no hi hagi jugador 1
nplay = int(input("Introdueix el numero de jugadors: "))
while nplay < 2:
    print("Número de jugadors no valid")
    nplay = int(input("Introdueix el numero de jugadors: "))

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
x = 1
#variable per determinar si algun jugador ha guanyat la ronda
punt = 0
#llista per a mirara q pe no estigui repetit
pe1 = []
#numero de jugador
nju = -1

while 3 not in pu and nplay >= 2: 
    print("Ronda:",x)
    #per a determinar el numero de pedres que volen jugar
    for i in range(0,nplay):
        pm[i] = int(input(f"Jugador {i}, quantes pedres vols jugar: "))
        if pm[i] > 3 or pm[i] < 0:
            print("Has fet trampa, eliminat")
            nplay = nplay - 1
            pm.pop(i)
    #per a determinar quantes pedres creuen q hi han
    print("Recorda que el numero màxim de pedres que hi ha en joc son:",nplay*3)
    for i in range(0,nplay):
        nju = i + x - 1
        pe[i] = int(input(f"Jugador {nju} quantes pedres creus que hi ha: "))#mirara la operacio de num jugador(no reseteja a 0)
        if pe[i] > (nplay*3) or pe[i] < pm[i] or pe[i] in pe1:
            print("Has fet trampa, eliminat")
            nplay1 = nplay - 1
            pm.pop(i)
            pe.pop(i)
        pe1.append(pe[i])
    pe1 = []
    pet = sum(pm)
    if x != 1:
        pe = pe[-1:] + pe[:-1]#possible error
    for i in range(0,nplay):
        if pe[i] == pet:
            pu[i] = pu[i] + 1
            punt = punt + 1
            print(f"Punt per al jugador {i}, hi havia {pet} pedres")
        pe[i] = 0
    if punt == 0:
        print(f"Cap jugador ha encertat, hi havia {pet} pedres")
    x = x + 1
    punt = 0

#diu el guanyador i genera una llista amb els punts
for i in range(0,nplay):
    if pu[i] == 3:
        print("Ha guanyat el jugador",i)
    print("jugador",i," "*10,pu[i])