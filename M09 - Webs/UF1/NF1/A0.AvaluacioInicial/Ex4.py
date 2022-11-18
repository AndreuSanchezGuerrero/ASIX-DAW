def isprime(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False

n = int(input("num: "))

if isprime(n) == False:
    print("no es primer")
else:
    print("es primer")