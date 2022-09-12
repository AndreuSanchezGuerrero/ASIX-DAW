nplay = int(input("Introdueix el numero de jugadors: "))
while nplay < 2:
    print("Número de jugadors no valid")
    nplay = int(input("Introdueix el numero de jugadors: "))
nplay1 = nplay

#def de la quantitat de pedres que vol jugar cadascun
def pajug(pm,nplay):
    for i in range(1,nplay+1):
        if i not in el:
            pm[i] = int(input(f"Jugador {i}, cuantes pedres vols jugar: "))
            if pm[i] > 3 or pm[i] < 0:
                el.append(i)
                print("Has fet trampa, eliminat")
                nplay1 = nplay1 - 1
                pu[i] = 0
                pm[i] = 0
                pe[i] = 0

#def de cuantes pedres creuen que hi ha en total
def pecreus(pm,pe,nplay,nplay1):
    print("Rescorda q el numero maxim de pedres que hi ha en joc son:",nplay1*3)
    for i in range(1,nplay+1):
        if i not in el:
            pe[i] = int(input(f"Jugador {i} cuantes pedres creus q hi ha: "))
            if pe[i] > (len(pm)*3) or pe[i] < pm[i]:# or pe[i] == pe[2]:
                el.append(i)
                print("Has fet trampa, eliminat")
                nplay1 = nplay - 1
                pu[i] = 0
                pm[i] = 0
                pe[i] = 0

#guanyador de la ronda
def guanyaron(pe,pu,nplay):
    pet = sum(pm.values())
    for i in range(1,nplay+1):
        if i not in el:
            if pe[i] == pet:
                pu[i] = pu[i] + 1
                print(f"Punt per al jugador {i}, hi havia {pet} pedres")
            else:
                print(f"El jugador {i} no ha encertat")

#guanyador del joc
def guanyador(pu):
    for i in range(1,nplay+1):
        if pu[i] == 3:
            print("Ha guanyat el jugador",i)
        #fer un llistat amb els punts de tots els jugadors

#llista amb els jugadors eliminats
el = []
#diccionari de variables amb les pedres q es creuen en total
pe = {}
#pedres que hi ha en total
for i in range(1,nplay+1):
    pe[i] = 0
#diccionari amb els punts
pu = {}
#punts de cada jugador
for i in range(1,nplay+1):
    pu[i] = 0
#diccionari amb les pedres a jugar
pm = {}
#pedres que vols jugar
for i in range(1,nplay+1):
    pm[i] = 0
#diccionari amb les variables de l'estat del joc

#n ronda
x = 1

while pu[1] != 3 and pu[2] != 3: #sha de canviar per a nombre de jugadors variable
    print("Ronda:",x)
    pajug(pm,nplay,nplay1)
    pecreus(pm,pe,nplay,nplay1) 
    guanyaron(pe,pu,nplay)
    x = x + 1
guanyador(pu)