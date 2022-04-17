def posarNota(codiAlumne: int, codiMateria: int, nota: int):
    # Servirà per posar nota a l'alumne a
    # Comprovarà que l'alumne està matriculat de la materia, i després li possarà nota
    # a[codiMateria]=nota
    if codiexists(codiAlumne,codiMateria) != False:
        if estaMatriculat(codiAlumne,codiMateria) == True:
            a = alumnes[codiAlumne]
            a.materies[codiMateria] = input("Nota: ") #potser posar nota de: materia
