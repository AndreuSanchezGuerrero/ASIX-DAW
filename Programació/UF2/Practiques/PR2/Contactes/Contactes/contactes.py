#Contactes
from datetime import date
class contacte:
    dataNaixement : date
    def __init__(self,nom:str,telefon:str):
        self.nom = nom
        self.telefon = telefon
