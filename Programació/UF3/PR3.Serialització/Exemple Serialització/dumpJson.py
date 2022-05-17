from datetime import * 

class pacient: 
    def __init__(self,codi:int,dataNaixement:str,sexe:str ,estat:str,iniciContagi:str,fiContagi:str ): 
        self.codi = codi 
        self.dataNaixement = dataNaixement
        self.sexe = sexe
        self.estat = estat
        self.iniciContagi = iniciContagi
        self.fiContagi = fiContagi


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
        class_ = getattr(module, class_name)
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj
