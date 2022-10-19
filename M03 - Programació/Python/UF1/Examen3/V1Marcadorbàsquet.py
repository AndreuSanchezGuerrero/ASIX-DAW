import re
loc = 0
vis = 0
punt = ""
while 1+1 == 2:
    print(f"{'-'*24}\nLocal    {loc}:{vis}   Visitant\n{'-'*24}")
    punt = str(input("Anotació: "))
    if re.search("fi|FI",punt):
        exit()
    elif re.search("^l|L",punt):
        loc = loc + int(punt[1])
    elif re.search("^(v|V)",punt):
        vis = vis + int(punt[1])
    else:
        print("Anotació incorrecte reintrodueix quan es demani")