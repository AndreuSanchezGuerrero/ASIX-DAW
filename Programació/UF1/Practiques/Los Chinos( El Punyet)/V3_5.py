nplay = int(input("Introdueix el numero de jugadors: "))
while nplay < 2:
    print("Número de jugadors no valid")
    nplay = int(input("Introdueix el numero de jugadors: "))
nplay1 = nplay

#llista amb els jugadors eliminats
el = []
#diccionari de variables amb les pedres q es creuen en total
pe = []
#diccionari amb els punts
pu = []
#diccionari amb les pedres a jugar
pm = []
#n ronda
x = 1
#variable per determinar si algun jugador ha guanyat la ronda
punt = 0

while 3 not in pu and nplay1 >= 2: 
    print("Ronda:",x)
    #per a determinar el numero de pedres que volen jugar
    for i in range(0,nplay):
        if i not in el:
            if x == 1:
                pm.append(int(input(f"Jugador {i}, quantes pedres vols jugar: ")))
            else:
                pm[i] = int(input(f"Jugador {i}, quantes pedres vols jugar: "))
            if pm[i] > 3 or pm[i] < 0:
                el.append(i)
                print("Has fet trampa, eliminat")
                nplay1 = nplay1 - 1
                pm[i] = 0
    #per a determinar cuantes pedres creuen q hi han
    #sha de rotar la llista
    print("Recorda que el numero màxim de pedres que hi ha en joc son:",nplay1*3)
    for i in range(1,nplay+1):
        if i in el:
        else:
            if x == 1:
                pe.append(int(input(f"Jugador {i} cuantes pedres creus que hi ha: ")))
            else:
                pe = pe[1:] + pe[:1]
                pe[i] = int(input(f"Jugador {y} cuantes pedres creus que hi ha: "))
            if pe[i] > (nplay1*3) or pe[i] < pm[i] or pe[i] in pe:
                el.append(i)
                print("Has fet trampa, eliminat")
                nplay1 = nplay - 1
                pm[i] = 0
                pe[i] = 0
    pet = sum(pm)
    for i in range(1,nplay+1):
        if i not in el:
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
for i in range(1,nplay+1):
    if pu[i] == 3:
        print("Ha guanyat el jugador",i)
    #fer un llistat amb els punts de tots els jugadors