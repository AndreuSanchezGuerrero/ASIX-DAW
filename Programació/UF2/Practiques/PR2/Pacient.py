from datetime import * 
import random
class pacient: 
    dataNaixement:date 
    sexe:str  #H,D 
    estat:str #Lleu,Greu,UCI,mort 
    iniciContagi:date 
    fiContagi:date 
    def __init__(self,codi:int): 
        self.codi = codi 

