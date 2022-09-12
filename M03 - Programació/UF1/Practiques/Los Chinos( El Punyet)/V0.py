#La versió que sha de mirar es la VF però les comparteixo totes per si vols mirar com evoluciona

#per a repetir la introdució de les variables en cas de no ser valides
def reppm(pm):
    if pm[1] > 3 or pm[2] > 3 or pm[1] < 0 or pm[2] < 0:
        print("1.Numero no valid, torna introduir:")
        return True
    else:
        return False

def reppe(pm,pe):
    if pe[1] > (len(pm)*3) or pe[2] > (len(pm)*3) or pe[1] == pe[2]:
        print("2.Numero no valid, torna introduir:")
        return True
    elif pe[1] < pm[1] or pe[2] < pm[2]:
        print("3.Numero no valid, torna introduir:")
        return True
    else:
        return False

#def de la quantitat de pedres que vol jugar cadascun
def pajug(pm):
    pm[1] = int(input("Jugador 1, cuantes pedres vols jugar: "))
    pm[2] = int(input("Jugador 2, cuantes pedres vols jugar: "))

#def de cuantes pedres creuen que hi ha en total
def pecreus(pe):
    if x//2 == 0:
        pe[1] = int(input("Jugador 1, cuantes pedres creus que hi ha en total: "))
        pe[2] = int(input("Jugador 2, cuantes pedres creus que hi ha en total: "))
    elif x//2 != 0:
        pe[2] = int(input("Jugador 2, cuantes pedres creus que hi ha en total: "))
        pe[1] = int(input("Jugador 1, cuantes pedres creus que hi ha en total: "))

#guanyador de la ronda
def guanyaron(pe,pu):
    pet = pm[1] + pm[2]
    if pe[1] == pet:
        pu[1] = pu[1] + 1
        print("Punt per al jugador 1")
    elif pe[2] == pet:
        pu[2] = pu[2] + 1
        print("Punt per al jugador 2")
    else:
        print("Cap jugador ha encertat")

#guanyador del joc
def guanyador(pu):
    if pu[1] == 3:
        print("Ha guanyat el jugador 1")
    elif pu[2] == 3:
        print("Ha guanyat el jugador 2")

#diccionari de variables amb les pedres q es creuen en total
pe = {}
#pedres que hi ha en total
pe[1] = 0
pe[2] = 0
#diccionari amb els punts
pu = {}
#punts de cada jugador
pu[1] = 0
pu[2] = 0
#diccionari amb les pedres a jugar
pm = {}
#pedres que vols jugar
pm[1] = 0
pm[2] = 0
#n ronda
x = 1

while pu[1] or pu[2] != 3:
    print("Ronda:",x)
    pajug(pm)
    while reppm(pm) == True:
        pajug(pm)
    pecreus(pe) 
    while reppe(pm,pe) == True:
        pecreus(pe)
    guanyaron(pe,pu)
    x = x + 1
guanyador(pu)