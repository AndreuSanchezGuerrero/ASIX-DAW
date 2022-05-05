#Generi un fitxer amb tots els Seat, anomenat «Seat.txt» 
import os
os.chdir(os.path.dirname(__file__))
with open("cotxes.txt", mode="r") as f, open("Seat.txt", mode="w") as f2:
    for line in f:
        if "Seat" in line:
            f2.write(line)
