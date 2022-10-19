#%%
n = int(input("Numero de exercisis")) + 1
for x in range (1, n):
    print("#%%""\n""#Ex"+str(x)+"\n"+"\n")

#%%
#Ex1
c1 = "-"
c2 = ""
while c1 != c2:
    print("introdueix la contrasenya dos cops")
    c1 = input("contrasenya:")
    c2 = input("contrasenya:")
print("contrasenya guardada")

#%%
#Ex2
c1 = "-"
c2 = ""
v = 3
while c1 != c2 and v > 0:
    print("introdueix la contrasenya dos cops")
    c1 = input("contrasenya:")
    c2 = input("contrasenya:")
    v = v - 1
if c1 == c2:
    print("contrasenya guardada")
else:
    print("s'hann esgotat els intents")

#%%
#Ex3
n = 0
while n >= 0 and n < 100:
    n = int(input("num"))

#%%
#Ex4
n1 = 1
n2 = -1
while n1 != 0:
    n2 = n1 + n2
    n1 = int(input("num"))
print(n2)

#%%
#Ex5
n1 = 1
n2 = -1
while n1 != 0:
    n2 = n1 * n2
    n1 = int(input("num"))
print(-n2)

#%%
#Ex6
n1 = 1
n2 = -1
n3 = 0
while n1 != 0 and n2 <= 100:
    n1 = int(input("num"))
    n2 = n1 + n2
print(n2)

#%%
#Ex7
n1 = 1
n2 = -1
n3 = 0
while n1 != 0 and n2 <= 100:
    n1 = int(input("num"))
    if n3 < n1:
        n3 = n1
    n2 = n1 + n2
print(f"la suma total equival a {n2} i el numero mes alt entrat es el {n3}")

#%%
#Ex8
x = 0
n2 = 0
n1 = int(input("introdueix un enter"))
sn1 = str(n1)
for i in range (0,len(sn1)):
    n2 = n2 + int(sn1[x])
    x = x + 1
print("la suma dels seus digits es",n2)

#%%
#Ex9
i = 0
v = 0
s = "s"
str1 = input("Introdueix una frase: ")
x = input("Introdueix una lletra")
while i < len(str1):
    if str1[i] == x:
        v = v + 1
    i = i + 1
if v == 1:
    s = ""
print(f"La paraula conte la lletra {v} cop{s}")

#%%
#Ex10
n = int(input("num"))
d = 1
x = 0
while n != x:
    if n%d == 0:
        d = d + 1
    x = x + 1
if d <= 2:
    print("es primer")
else:
    print("no es primer")


