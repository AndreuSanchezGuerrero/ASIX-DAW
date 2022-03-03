for x in range (1, 8):
    print("#Ex"+str(x))

#%%
#Ex1 
text0 = input("Introdueix el teu text")
text1 = (f"{text0:<80}")
text2 = (f"{text0:^80}")
text3 = (f"{text0:>80}")
print(text1)
print(text2)
print(text3)
#Ex2
num = float(input("Introudueix un numero amb decimals"))
numen = int(num)
num1 = str(num)
numde = num1.split('.')[1]
print("Part entera: "+numen)
print("Part decimal: 0."+numde)
#Ex3
preu = float(input("introdueix el preu de l'article"))
diners = float(input("Introdueix la cantitat donada"))
print("canvi: "+ str(diners - preu))
#Ex4
preu = float(input("introdueix el preu de l'article"))
diners = float(input("Introdueix la cantitat donada"))
canvi = diners - preu
canvi1 = canvi%5
canvi2 = preu%5 + canvi
print("Canvi:", canvi)
if canvi1 == 0:
    print("Canvi:", canvi)
else:
    print("Canvi arrodonit:", canvi2)
#Ex5
preu = float(input("introdueix el preu de l'article"))
diners = float(input("Introdueix la cantitat donada"))
can = diners - preu
print("Canvi:", canvi)
m100 = can//100
m50 = can%100//50
m20 = can%100%50//20
m10 = can%100%50%20//10
m5 = can%100%50%20%10//5
print("monedes de 100= ",int(m100))
print("monedes de 50=",int(m50))
print("monedes de 20",int(m20))
print("monedes de 100= ",int(m10))
print("monedes de 100= ",int(m5))
#Ex6
"NO"
#Ex7
v1 = float(input("KG"))
v2 = v1*2.20462
print(v1,"kg equivalen a:",v2,"lliures")

v1 = input("euros")
v2 = v1*0.85
print(v1,"euros equivalen a:",v2,"lliures")

v1 = float(input("graus"))
v2 = v2*1.8+32
v3 = v1 + 273.15
print(v1,"graus equivalen a:",v2,"fahrenheit, i a:",v3,"kelvin")

v1 = input("hora en format HH:MM:SS")
v2 = 3600*int(v1[:2])
v3 = 60*int(v1[3:5])
v4 = int(v1[-2:])
v5 = v2+v3+v4
print(v1,"equival a:",v5,"segons")

v1 = int(input("segons"))
h = str(v1//3600)
min = str(v1%3600//60)
s = str(v1%3600%60)
x = f"{h:0>2}:{min:0>2}:{s:0>2}"
print(v1,"segons equivalen a:",x)