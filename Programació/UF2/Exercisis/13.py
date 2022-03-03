def agrupaFactors(n):
    i = 2
    factors = []
    diccionari = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    for i in range(0,len(factors)):
        if factors[i] in diccionari:
            diccionari[factors[i]] += 1
        else:
            diccionari[factors[i]] = 1
    return diccionari
print(agrupaFactors(80))