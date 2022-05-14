import json 

fitxer = open("pepe.json","w") 

class alumne: 

    def __init__(self,nom,cognom): 

        self.nom = nom 

        self.cognom =cognom 

 

def convert_to_dict(obj): 

  obj_dict = { 

 

    "__class__": obj.__class__.__name__, 

 

    "__module__": obj.__module__ 

 

  } 

  obj_dict.update(obj.__dict__) 

  return obj_dict 

 

def dict_to_obj(our_dict): 

    if "__class__" in our_dict: 

        class_name = our_dict.pop("__class__") 

        module_name = our_dict.pop("__module__") 

        module = __import__(module_name) 

        class_ = getattr(module,class_name) 

        obj = class_(**our_dict) 

    else: 

        obj = our_dict 

    return obj 

 

pepe = alumne("Pepe","González") 

pepeDict = convert_to_dict(pepe) 

 

json.dump(pepeDict, fitxer,sort_keys=True, indent=4) 

 

fitxer.close() 

 

fitxer = open("pepe.json","r") 

nouPepeJSON = json.load(fitxer) 

fitxer.close() 

nouPepe = dict_to_obj(nouPepeJSON) 

print(nouPepe.nom) 
