import pickle

class alumne: 
    def __init__(self,nom,cognom): 
        self.Nom = nom 
        self.Cognom = cognom


entrada = open("dades",'rb')

dades = pickle.load(entrada)
print(dades)

a1 = pickle.load(entrada)
print(a1.Nom)

entrada.close()
