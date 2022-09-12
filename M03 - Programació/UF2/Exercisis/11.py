import re
def eliminaAccents(nom):
    nomNet = ""
    for i in range(0, len(nom)):
        if re.search("[a-z]",nom[i]):
            nomNet = nomNet + nom[i]
        else:
            if nom[i] == "ç":
                nomNet = nomNet + "c"
            if nom[i] == "ñ":
                nomNet = nomNet + "n"