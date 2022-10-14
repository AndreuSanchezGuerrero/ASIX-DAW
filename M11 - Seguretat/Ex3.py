"""
Exercici 3 (mostra les captures de pantalla i justifica correctament el procés) (4 punts)

4.1.	Amb Python, obté el codi SHA256 de les següents paraules:
•	hello
•	hola
•	12345
•	El teu nom
•	La teva data de naixement en format de 6 dígits (2 per al dia, 2 per al mes, 2 per a l’any)
•	Una frase



4.2.	Utilitza el següent codi Python  https://github.com/Starwarsfan2099/Python-Hash-Cracker per provar la força de les contrasenyes anteriors. Quan temps tarda en desxifrar cadascuna? N’hi ha alguna que no trobi?



4.3.	En el cas de la data de naixement, prova a rebentar-la mitjançant la opció numèrica del codi Python anterior. L’aconsegueix trobar? Quan temps ha necessitat?



4.4.	En lloc del diccionari Wordlist.txt que ve per defecte, busca altres diccionaris que s’acostumin a utilitzar per rebentar contrasenyes. Fes una llista dels més habituals i prova almenys un. Quina diferència hi ha entre ells?
"""

#4.1 
import hashlib

def hash_sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

print(hash_sha256("hello"))
print(hash_sha256("hola"))
print(hash_sha256("12345"))
print(hash_sha256("El teu nom"))
print(hash_sha256("04/07/2003"))
print(hash_sha256("Una frase inventada per mi"))


