#%%
for x in range (1, 20):
    print("#%%""\n""#Ex"+str(x)+"\n"+"\n")

#%%
#Ex1
str1 = input("Paraula: ")
while str1.lower() != "fi":
    str1 = input("Paraula: ")
print("FI")

#%%
#Ex2
str1 = input("Paraula: ")
n = 0
while str1.lower() != "fi":
    n = n + 1
    str1 = input("Paraula: ")
print(f"Has introduit {n} paraules, FI")

#%%
#Ex3
p2 = " "
p1 = input("Paraula: ")
while p1 != p2:
    p2 = p1
    p1 = input("Paraula: ")
print("has repetit la paraula, FI")

#%%
#Ex4
import random
random.seed()
num = random.randint(1,10)
num1 = int(input("Introdueix un numero"))
while num != num1:
    num1 = int(input("Introdueix un numero"))
    print("no l'has encertat torna a provar")
print("has encertat el numero")

#%%
#Ex5
import random
random.seed()
i = 1
num = random.randint(1,10)
num1 = int(input("Introdueix un numero"))
while num != num1:
    print("no l'has encertat torna a provar")
    num1 = int(input("Introdueix un numero"))
    i = i + 1

if i != 1:
    s = "s"
else:
    s = ""
print(f"has encertat el numero despres de {i} intent{s}")

#%%
#Ex6
import random
random.seed()
i = 1
num = random.randint(1,10)
num1 = int(input("Introdueix un numero"))
while num != num1:
    if num1 > num:
        a = "mes petit"
    else:
        a = "mes gran"
    print(f"no l'has encertat torna a provar amb un numero {a}")
    num1 = int(input("Introdueix un numero"))
    i = i + 1

if i != 1:
    s = "s"
else:
    s = ""
print(f"has encertat el numero despres de {i} intent{s}")

#%%
#Ex7 
str1 = input("Introdueix una paraula")
spaces = 0
for i in range(0,len(str1)):
    if(str1[i] == ' '):
        spaces = spaces + 1
print("The number of spaces are: ",spaces)

#%%
#Ex8
str1 = input("Introdueix una paraula")
str2 = ""
chr1 = ""
for i in range(0,len(str1)):
    if(str1[i] >= "0" and str1[i] <= "9"):
        chr1 = str(str1[i])
        str2 = str2 + chr1
print(f"The introduced string is {str1} and the number is: {str2}")

#%%
#Ex9
import random
random.seed()
n = random.randint(1,100)
i = 2
while n != i:
    print(i)
    i = i + 1

#%%
#Ex10
import random
random.seed()
n1 = random.randint(1,100)
n2 = random.randint(1,100)
print(n1,n2)
if n2 < n1:
    print("mec")
else:
    n1 = n1 + 1
    while n1 != n2:
        print(n1)
        n1 = n1 + 1

#%%
#Ex11
import random
random.seed()
n1 = random.randint(1,100)
n2 = random.randint(n1,100)
print(n1,n2)
if n2 < n1:
    print("mec")
else:
    n1 = n1 + 1
    while n1 != n2:
        print(n1)
        n1 = n1 + 1

#%%
#Ex12
str2 = ""
str1 = input("Introdueix una frase: ")
for i in range(0,len(str1)):
    if str1[i] != " ":
        str2 = str2 + str1[i]
    else:
        print(str2)
        str2 = ""
print(str2)

#%%
#Ex13
import random
random.seed()
n1 = random.randint(1,10)
for i in range(1,n1):
    print(i*"*")
    print((i+1)*"+")

#%%
#Ex14
n = 0
str2 = ""
str3 = ""
str1 = input("Introdueix una frase: ")
while n < len(str1):
    str2 = str2 + str1[n]
    str3 = str3 + str1[n+1]
    n = n + 2
print(str2,str3)

#%%
#Ex15
i = 0
str1 = input("Introdueix una frase: ")
while i - 1 < len(str1) and str1[i] != " ":
    i = i + 1
print("l'espai es troba a la posició:",i + 1)

#%%
#Ex16
i = 0
e = 0
str1 = input("Introdueix una frase: ")
while i < len(str1) and e != 3:
    if str1[i] == " ":
        e = e + 1
    i = i + 1
print("el tercer espai es troba a la posició:",i + 1)

#%%
#Ex17
i = 0
a = 0
str1 = input("Introdueix una paraula: ")
while i < len(str1) and a < 4:
    if str1[i] == "a":
        a = a +1
    i = i + 1
if a >= 4:
    print("la paraula te 4 o mes vegades la vocal a")
else:
    print("la paraula te menys de 4 vegades la vocal a")

#%%
#Ex18
i = 0
v = 0
str1 = input("Introdueix una paraula: ")
while i < len(str1) and v < 5:
    if str1[i] in "aeiou":
        v = v + 1
    i = i + 1
if v >= 5:
    print("la paraula te les 5 vocals")
else:
    print("la paraula no te les 5 vocals")

#%%
#Ex19
import random
random.seed()
n1 = random.randint(1,100)
n2 = 0
v = 5
while n1 != n2:
    n2 = int(input("introdueix el numero:"))
    v = v - 1
    if v != 0:
        if n1 == n2:
            print("l'has encertat")
        elif n2 > n1:
            print("Introdueix un numero mes petit")
        elif n2 < n1:
            print("Introdueix un numero mes gran")
    else:
        n2 = n1
print("T'has quedat sense vides")
