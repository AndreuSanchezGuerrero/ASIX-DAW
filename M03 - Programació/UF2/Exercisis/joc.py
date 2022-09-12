import pygame as pg
import time
import random
random.seed()

class punt:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class serp:
    
    def __init__(self,p):
        self.cap = p
        self.cua = list()


def missatge():
    estilFont = pg.font.SysFont("arialblack",30)
    msgFormatat = estilFont.render("La cagaste",True,colors["vermell"])
    pantalla.blit(msgFormatat,[10,10])

def direccions(tecla):
    if tecla == pg.K_LEFT or tecla == pg.K_a:
        return {"x":-gruix,"y":0}
    elif tecla == pg.K_RIGHT or tecla == pg.K_s:
        return {"x":+gruix,"y":0}
    elif tecla == pg.K_UP or tecla == pg.K_w:
        return {"x":0,"y":-gruix}
    elif tecla == pg.K_DOWN or tecla == pg.K_d:
        return {"x":0,"y":+gruix}
    else:
        return None

def laPalmao(x,y):
    return x<0 or y<0 or x>amplada or y>alcada

def nouMenjar():
    x =random.randint(0,amplada-gruix)//gruix*gruix
    y =random.randint(0,alcada-gruix)//gruix*gruix
    return {"x":x,"y":y}

def nyamNyam(x,y,m):
    return x == m["x"] and y == m["y"]

def mostrarSerp(s):
    for x,y in s:
        pg.draw.rect(pantalla,colors["blau"],[x,y,gruix,gruix])

def serpEsMenja(s):
    cap = s[-1]
    cua = s[0:-1]
    return cap in cua
colors = {"blau"    : (0,0,255),
        "vermell" : (255,0,0),
        "blanc"   : (255,255,255)
        }



pg.init()

amplada = 600
alcada = 400
gruix = 20
velocitat = 10
vibora = []
longitudSerp = 1

temporitzador = pg.time.Clock()
pantalla = pg.display.set_mode((amplada,alcada))
pg.display.set_caption("La víbora")
pg.display.update()

x = amplada//2
y = alcada//2
deltaX=0
deltaY=0
fiJoc = False
menjar = nouMenjar()
while not fiJoc:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fiJoc = True
        if event.type == pg.KEYDOWN:
            d = direccions(event.key)
            if d:
                deltaX = d["x"]
                deltaY = d["y"]
    vibora.append([x,y])
    if len(vibora)>longitudSerp:
        vibora.pop(0)
    x += deltaX
    y += deltaY
    pantalla.fill(colors["blanc"])
    mostrarSerp(vibora)
    pg.draw.rect(pantalla,colors["vermell"],[menjar["x"],menjar["y"],gruix,gruix])

    if laPalmao(x,y) or serpEsMenja(vibora):
        missatge()
        fiJoc = True
    if nyamNyam(x,y,menjar):
        menjar = nouMenjar()
        longitudSerp += 1
        
    pg.display.update()
    temporitzador.tick(velocitat)

time.sleep(2)    
pg.quit()