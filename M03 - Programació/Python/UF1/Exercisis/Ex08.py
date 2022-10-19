#%%
for x in range (9, 26):
    print("#%%""\n""#Ex"+str(x)+"\n"+"\n")

#%%
#Ex1
for x in range (1, 21):
    print(x)

#%%
#Ex2
for x in range (2, 51, 2):
    print(x)

#%%
#Ex3
for x in range (20, 0, -1):
    print(x)

#%%
#Ex4
for x in range (1, 21, 2):
    print(x)
for x in range (20, 41, 2):
    print(x)

#%%
#Ex5
import random
random.seed()
n1 = random.randint(1,101)
n2 = random.randint(1,101)
print(n1, n2)
for x in range (n1, n2+1):
    print(x)

#%%
#Ex6
import random
random.seed()
n1 = random.randint(1,101)
n2 = random.randint(1,101)
n = 1
print(n1, n2)
if n1 > n2:
    n = -1
for x in range (n1, n2, n):
    print(x)
#%%
#Ex7
str1 = input("paraula")
for x in range (0, len(str1)):
    print(str1[x])

#%%
#Ex8
str1 = input("paraula")
for x in range (1, len(str1), 2):
    print(str1[x])

#%%
#Ex9
str1 = input("paraula")
for x in range (0, len(str1))[::-1]:
    print(str1[x])

#%%
#Ex10
str1 = input("paraula")
n = range(0,10)
n1 = [str(x) for x in n]
for x in range (0, len(str1)):
    if str1[x] not in n1: 
        print(str1[x])

# %%
