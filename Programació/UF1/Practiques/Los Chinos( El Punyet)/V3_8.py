#La versió que sha de mirar es la VF però les comparteixo totes per si vols mirar com evoluciona
nplay = int(input("Introdueix el numero de jugadors: "))
while nplay < 2:
    print("Número de jugadors no valid")
    nplay = int(input("Introdueix el numero de jugadors: "))

#llista amb els jugadors eliminats
el = []
#diccionari de variables amb les pedres q es creuen en total
pe = {}
#diccionari amb els punts
pu = {}
for i in range(1,nplay+1):
    pu[i] = 0
#diccionari amb les pedres a jugar
pm = {}
#número de ronda
x = 1
#variable per determinar si algun jugador ha guanyat la ronda
punt = 0
#llista per a mirara q pe no estigui repetit
pe1 = []
#numero de jugador
nju = 0
#quants jugadors eliminats
nel = 0

while 3 not in pu.values() and nplay >= 2: 
    print("Ronda:",x,"\n","Recorda que el màxim de pedres que pots jugar són 3")
    #per a determinar el numero de pedres que volen jugar
    for i in range(1, nplay+1):
        if i not in el:
            pm[i] = int(input(f"Jugador {i}, quantes pedres vols jugar: "))
            if pm[i] > 3 or pm[i] < 0:
                print("Has fet trampa, eliminat (,les seves pedres tmb han estat eliminades)")
                pm[i] = 0
                el.append(i)
    #per a determinar quantes pedres creuen q hi ha
    print("Recorda que el numero màxim de pedres que hi ha en joc son:",(nplay-len(el))*3)
    nju = x - 1
    for i in range(1,nplay+1):
        if x - 1 in el:
            nju = nju + 1
        nju = nju + 1
        if nju > nplay:
            nju = 1
        if nju not in el:
            pe[nju] = int(input(f"Jugador {nju} quantes pedres creus que hi ha: "))
            if pe[nju] > (nplay*3) or pe[nju] < pm[nju] or pe[nju] in pe1:
                print("Has fet trampa, eliminat")
                pm[i] = 0
                pe[i] = 0
            else:
                pe1.append(pe[nju])
    pe1 = []
    pet = sum(pm.values())
    for i in range(1,nplay+1):
        if i not in el:
            if pe[i] == pet:
                pu[i] = pu[i] + 1
                punt = punt + 1
                print(f"Punt per al jugador {i}, hi havia {pet} pedres")
        pe[i] = 0
    if punt == 0:
        print(f"Cap jugador ha encertat, hi havia {pet} pedres")
    punt = 0
    x = x + 1

#diu el guanyador i genera una llista amb els punts (,inclosos eliminats)
for i in range(1,nplay+1):
    if pu[i] == 3:
        guanyador = i
    print("Jugador",i + 1," "*10,pu[i])
print("Ha guanyat el jugador",guanyador)