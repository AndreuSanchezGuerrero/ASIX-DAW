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
