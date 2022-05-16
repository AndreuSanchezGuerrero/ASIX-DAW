from datetime import * 

class pacient: 
    dataNaixement:date 
    sexe:str  #H,D 
    estat:str #Lleu,Greu,UCI,mort 
    iniciContagi:date 
    fiContagi:date 
    def __init__(self,codi:int): 
        self.Codi = codi 


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
