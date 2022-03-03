loc = 0
vis = 0
punt = ""
while 1+1 == 2:
    print(f"{'-'*24}\nLocal    {loc}:{vis}   Visitant\n{'-'*24}")
    punt = str(input("Anotació: "))
    if punt == "fi" or punt == "FI":
        exit()
    elif punt[0] == "l" or punt[0] == "L":
        loc = loc + int(punt[1])
    elif punt[0] == "v" or punt[0] == "V":
        vis = vis + int(punt[1])
    else:
        print("Anotació incorrecte reintrodueix quan es demani")