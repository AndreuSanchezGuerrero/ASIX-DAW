#Codi per a crear materies, alumnes, matricular alumnes a materies i possarlis nota, tot aleatoriament
from random import *
from clases import *
from datetime import *

#llista amb noms catalans:
noms = ["Abel","Adam","Adrià","Aidé","Aimar","Aitor","Alan","Albà","Aleix","Aleu","Aniol","Aram","Aran","Aria","Arnau","Artal","Artur","Asier","Benet","Biel","Blai","Boi","Bru","Cai","Cesc","Damià","Dan","David","Drac","Dídac","Edgar","Elian","Elm","Eloi","Eneko","Enric","Enzo","Feliu","Garbí","Gaël","Genís","Gerai","Gil","Grau","Guim","Guiu","Hug","Ian","Iol","Isaac","Iu","Izan","Jan","Joan","Joel","Jofre","Josep","Juli","Jòrdi","Júlia","Lleó","Llop","Lluc","Magí","Manel","Marc","Maria","Martí","Matèu","Max","Nel","Nico","Nil","Noel","Nofre","Olau","Oriol","Ot","Otger","Oto","Oña","Pau","Pep","Pere","Pol","Quel","Quer","Quim","Roc","Roger","Sam","Sergi","Sol","Tom","Ton","Uriel","Xavi","Àlex","Àxel","Èric"]
cognoms = ["Bladé","Blanquer","Bobé","Bober","Boher","Boter","Bové","Bover","Bubé","Fabra","Fàbraga","Fabre","Fabré","Fàbrega","Fàbregas","Fàbregues","Fabrer","Farré","Farrer","Febre","Febrer","Ferré","Ferrer","Mercadé","Mercader","Moliner","Ollé","Oller","Ollers","Ollés","Sastre","Ullé","Uller","Ullés"]
nomsmateries = ["Matemàtiques","Ciències","Llenguatge","Idiomes","Socials","Art","Música","Teatre","Tecnologia","Física","Informàtica"]

# alumnes és un diccionari que tindrà com a Key el codi de l'alumne, i com a Value al propi alumne
alumnes = {}
# materies és un diccionari que tindrà com a Key el codi de la materia i com a value la pròpia matèria
materies = {}

inicio = datetime(1996, 1, 1) 
final = datetime(2003, 12, 31) 

codia = 0
datanaix = 0

#bucle per crear materies
for i in range(0,len(nomsmateries)):
    m = materia(i,nomsmateries[i])
    materies.update({i:m})
    print(m.Codim,m.Nom)

#bucle per a crear alumnes
for i in range(0,20):
    datanaix = ((inicio + (final - inicio) * random()).date())
    a = alumne(i,choice(noms),choice(cognoms),datanaix)
    for j in range(0,len(materies)):
        m = materies[j]
        if j%randint(1,len(materies)) != 0:
            a.Materies.update({m.Codim:randint(0,9)})
            m.Alumnes.append(a)
        else:
            a.Materies.update({m.Codim:"No matriculat"})
    alumnes.update({i:a})
    print(a.Codia,a.Nom,a.Cognom,a.DataNaixement)

#Codi per fer un print dels alumnes de cada materia
for i in range(0,len(materies)):
    m = materies[i]
    print(m.Codim,m.Nom)
    for j in range(0,len(m.Alumnes)):
        print(m.Alumnes[j].Codia)



# Els codis s'ha de fer q si selimina un el seguent afegit vaigi alla i tal

codia = len(alumnes)
codim = len(materies)