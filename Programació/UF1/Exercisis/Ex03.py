#Ex 1.
nom = input("Introdueix el teu nom")
print("hola",nom)
#Ex2
nom1 = input("introdueix el nom del primer alumne")
nom2 = input("introdueix el nom del segon alumne")
print(nom1)
print(nom2)
#Ex3
centimetres = float(input("Introdueix els cm"))
print(centimetres,"centimetres equivalen a",float(centimetres*0.39)," polzades")
#Ex4
num = int(input("Introdueix un numero"))
print("El doble del numero",num,"es igual a",num*2)
#Ex5
numero1 = int(input ("Primernúmero "))
numero2 = int(input ("Segonnúmero "))
resultat = numero1 + numero2
print(numero1,"+",numero2,"=", resultat)
#Ex6
num1 = int(input ("Primernúmero "))
num2 = int(input ("Segonnúmero "))
print(num1,"+",num2,"=",num1+num2)
print(num1,"*",num2,"=",num1*num2)
print(num1,"-",num2,"=",num1-num2)
print(num1,"/",num2,"=",num1/num2)
#Ex7
num1 = int(input ("Primernúmero "))
num2 = int(input ("Segonnúmero "))
print(num2,num1)
#Ex8
num1 = int(input ("Introdueix el numero "))
print(num1%2)
#Ex9
num1 = int(input ("Introdueix el numero "))
print(bool(num1%2))
#Ex10
num1 = int(input ("Introdueix el numero "))
print(int(not bool(num1%2)))
#Ex11
str1= input("introdueix una paraula")
str2= input("Introdueix una altra paraula")
print(str1+str2)
#Ex12
str1= input("introdueix una paraula")
str2= input("Introdueix una altra paraula")
print(str1 + str2)
#Ex13
edat= int(input("introdueix la teva edat"))
print("Et falten",int(18)-edat,"anys per ser major d'edat")
#Ex14
chr1 = input("introdueix una lletra")
print(chr1*20)
#Ex15
chr1 = str(input("intrudueix una tecla"))
print(ord(chr1))
#Ex16
lletra = input("Lletra: ")
codi = ord(lletra)
print(codi)
#Ex17
num1 = int(input("Numero 1"))
num2 = int(input("Numero 2"))
if(num1>num2):
    print(num1)
elif(num2>num1):
    print(num2)
#Ex18
num1 = input("Introdueix un numero de dos xifres")
num1 = num1[-1] + num1[:-1]
print(num1)
#Ex19
num1 = int(input("Introdueix un numero de tres xifres"))
u = str(num1%10)
dc = num1//10
d = str(dc%10)
c = str(dc//10)
print(u+d+c)
#Ex20
import math
print("Problema del cargol\n")
H = int(input("itrodueix la altura"))
A = int(input("introdueix els metres q puja cada dia"))
B = int(input("introdueix els metres q baixa cada dia"))
dies = math.ceil((H-B)/(A-B))
print(f"El cargol trigarà {dies}")