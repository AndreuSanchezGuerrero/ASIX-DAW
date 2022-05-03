"""
8.Programa els següents mètodes d’ordenació en Python:
Iteratiu: Bubble Sort o Insert Sort 
Recursiu: Merge Sort o QuickSort, el que vulguis
Comprova cronometrant el temps quin és més ràpid, compara’ls amb el sort de python que fa servir el TrimSort
"""

def bubbleSort(llista):
    for i in range(len(llista)-1):
        for j in range(len(llista)-1-i):
            if llista[j] > llista[j+1]:
                llista[j], llista[j+1] = llista[j+1], llista[j]
    return llista

def insertionSort(llista):
    for i in range(1,len(llista)):
        j = i
        while j > 0 and llista[j] < llista[j-1]:
            llista[j], llista[j-1] = llista[j-1], llista[j]
            j -= 1
    return llista

def mergeSort(llista):
    if len(llista) < 2:
        return llista
    else:
        meitat = len(llista)//2
        return merge(mergeSort(llista[:meitat]), mergeSort(llista[meitat:]))

def merge(llista1, llista2):
    llista = []
    while len(llista1) > 0 and len(llista2) > 0:
        if llista1[0] < llista2[0]:
            llista.append(llista1.pop(0))
        else:
            llista.append(llista2.pop(0))
    llista += llista1
    llista += llista2
    return llista

def quickSort(llista):
    if len(llista) < 2:
        return llista
    else:
        pivot = llista[0]
        menor = [i for i in llista[1:] if i <= pivot]
        major = [i for i in llista[1:] if i > pivot]
        return quickSort(menor) + [pivot] + quickSort(major)

#random int list generator
def llistai():
    llista = []
    x = 333
    while len(llista) < x:
        rint = randint(1,x)
        if rint not in llista:
            llista.append(rint)
    return llista


#Per comprovar quin de tots es el mes ràpid
timeBubble = 0
timeInsertion = 0
timeMerge = 0
timeQuick = 0

#Se q aquesta part es pot reduir.
for k in range(1000):
    timeI = time()
    llistab = bubbleSort(llistai())
    timeBubble += time() - timeI
    timeI = time()
    llistain = insertionSort(llistai())
    timeInsertion += time() - timeI
    timeI = time()
    llistam = mergeSort(llistai())
    timeMerge += time() - timeI
    timeI = time()
    llistaq = quickSort(llistai())
    timeQuick += time() - timeI

print("BubbleSort:",(timeBubble/k)*1000)
print("Insertion :",(timeInsertion/k)*1000)
print("MergeSort :",(timeMerge/k)*1000)
print("QuickSort :",(timeQuick/k)*1000)