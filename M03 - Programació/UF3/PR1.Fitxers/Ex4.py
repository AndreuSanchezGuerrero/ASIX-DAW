"""
Generi un nou fitxer per a cada marca amb els cotxes corresponenst a la 
marca: «Seat.txt», «Renault.txt», «Lanborgini.txt», «Ferrari.txt», ... 
Suposarem que només tindrem cotxes d'aquestes 4 marques.
"""
import os
os.chdir(os.path.dirname(__file__))
with open("cotxes.txt", mode="r") as f, open("Seat.txt", mode="w") as f2, open("Renault.txt", mode="w") as f3, open("Lanborghini.txt", mode="w") as f4, open("Ferrari.txt", mode="w") as f5:
    for line in f:
        if "Seat" in line:
            f2.write(line)
        elif "Renault" in line:
            f3.write(line)
        elif "Lanborghini" in line:
            f4.write(line)
        elif "Ferrari" in line:
            f5.write(line)