from contactes import contacte
def mostrarContactes(contactes):
    print(f"{'Nom':30}{'Telefon':>12}")
    print("="*42)
    for c in contactes:
        print(f"{c.nom:30}{c.telefon:>12}")


contactes=[contacte("Joan","666555555"),contacte("Maria","999999999")]
mostrarContactes(contactes)
