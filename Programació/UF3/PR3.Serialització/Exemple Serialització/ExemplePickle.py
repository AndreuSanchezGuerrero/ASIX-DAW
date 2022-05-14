import pickle

class alumne: 
    def __init__(self,nom,cognom): 

        self.Nom = nom 

        self.Cognom = cognom 

dades = {'a': [1, 2.0, 3, 4+6j], 

         'b': ('string', u'Unicode string'), 

         'c': None}

a1 = alumne("Pep","López")

sortida = open("dades",'wb')

pickle.dump(dades,sortida)
pickle.dump(a1,sortida)

sortida.close()
