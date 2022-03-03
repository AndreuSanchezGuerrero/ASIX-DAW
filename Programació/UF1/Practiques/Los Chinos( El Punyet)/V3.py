import random as rd
rd.seed()
nplay = int(input("Introdueix el numero de jugadors: "))
#l'utilitzo per a cantitat jugador pero els jugadors son eliminats per tant els len sha de utilitzar alguna altra variable

#def per saber si un jugador ha estat eliminat
def eliminat():
    if 
#def de la quantitat de pedres que vol jugar cadascun
def pajug(pm):
    for i in range(1,nplay+1):
        pm[i] = int(input(f"Jugador {i}, cuantes pedres vols jugar: "))
        if pm[i] > 3 or pm[i] < 0:
            print("Has fet trampa, eliminat")
            #eliminar el jugador del diccionari

#def de cuantes pedres creuen que hi ha en total
def pecreus(x,pm,pe):
    print("Rescorda q el numero maxim de pedres que hi ha en joc son:",nplay*3)
    for i in range(1,nplay+1):
        pe[i] = int(input(f"Jugador {i} cuantes pedres creus q hi ha: "))
        if pe[i] > (len(pm)*3) or pe[i] < pm[i]:# or pe[i] == pe[2]:
            print("Has fet trampa, eliminat")
            #eliminar el jugador del diccionari

#guanyador de la ronda
def guanyaron(x,pe,pu):
    pet = sum(pm.values())
    for i in range(1,nplay+1):
        if pe[i] == pet:
            pu[i] = pu[i] + 1
            print(f"Punt per al jugador {i}, hi havia {pet} pedres")
    else:
        print(f"Cap jugador ha encertat, hi havia {pet} pedres")
    x = x + 1

#guanyador del joc
def guanyador(pu):
    for i in range(1,nplay+1):
        if pu[i] == 3:
            print("Ha guanyat el jugador",i)
        #fer un llistat amb els punts de tots els jugadors

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
#n ronda
x = 1

while pu[1] != 3 and pu[2] != 3: #sha de canviar per a nombre de jugadors variable
    print("Ronda:",x)
    pajug(pm)
    pecreus(x,pm,pe) 
    guanyaron(x,pe,pu)
guanyador(pu)