

def eliminarAlumne(codiAlumne: int):
    # Elimina del diccionary alumnes, l'alumne que té com a codi codiAlumne
    # Ha de eliminar-lo també de totes les materies que estigui matriculat
    # Deletes the alumn from the dictionary and delete him from all the subjects he is enrolled
    # shuara de eliminar el codi tmb i per tant fer un buscador de codis vuits o be canviar el codi de tots els alumnes a un menys
    # tmb es podria fer un metoide per afegir un alumne a un codi q ja exiteix movent tots els sltres una posicio
    if codiAlumne in alumnes:
        a = alumnes[codiAlumne]
        for m in a.materies:
            materies[m].Alumnes.remove(a)
        alumnes.pop(codiAlumne)
    else:
        print("No existeix aquest alumne")


def desmatriculaAlumne(codiAlumne: int, codiMateria: int):
    # Ha de fer el contrari que el métode anterior
    if codiexists(codiAlumne,codiMateria) != False:
        a = alumnes[codiAlumne]
        m = materies[codiMateria]
        a.materies.pop(codiMateria)
        m.Alumnes.remove(a)


def estaMatriculat(codiAlumne: int, codiMateria: int):
    # retornarà True si l'alumne ja està matriculat de la materia i false sinó està matriculat
    if codiexists(codiAlumne,codiMateria) != False:
        a = alumnes[codiAlumne]
        m = materies[codiMateria]
        if m in a.materies:
            return True
        else:
            return False


def posarNota(codiAlumne: int, codiMateria: int, nota: int):
    # Servirà per posar nota a l'alumne a
    # Comprovarà que l'alumne està matriculat de la materia, i després li possarà nota
    # a[codiMateria]=nota
    if codiexists(codiAlumne,codiMateria) != False:
        if estaMatriculat(codiAlumne,codiMateria) == True:
            a = alumnes[codiAlumne]
            a.materies[codiMateria] = input("Nota: ") #potser posar nota de: materia



def mostrarNotesMateria(codiMateria: int):
    # Li passarem el codi d'una Matèria i ens mostrarà per pantalla un llistat amb les següents columnes:
    # Nom Materia  CodiAlumne  NomAlumne Nota
    # Si l'alumne no té nota, mostrarà 2 guionets --
    if codiMateria in materies:
        m = materies[codiMateria]
        for a in m.Alumnes:
            print(m.nom, a.codia, a.nom, a.materies[codiMateria])
    else:
        print("No existeix aquesta materia")


def mostrarNotesAlumne(codiAlumne: int):
    # Li passarem el codi d'un alumne i ens mostrarà per pantalla un llistat amb les següents columnes:
    # Nom Materia  Nota
    # Si l'alumne no té nota, mostrarà 2 guionets --
    if codiAlumne in alumnes:
        a = alumnes[codiAlumne]
        for m in a.materies:
            print(materies[m].nom, a.materies[m].nota)
    else:
        print("No existeix aquest alumne")


def codiexists(codia: int,codim: int):
        if codia not in materies:
            print("l'alumne no existeix")
            return False
        elif codim not in materies:
            print("la materia no existeix")
            return False