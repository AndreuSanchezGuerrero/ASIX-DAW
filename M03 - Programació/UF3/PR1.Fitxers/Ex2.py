#2.Ens mostri per pantalla tots els Renaults.
import os
os.chdir(os.path.dirname(__file__))
with open("cotxes.txt", mode="r") as f:
    for line in f:
        if "Renault" in line:
            print(line)