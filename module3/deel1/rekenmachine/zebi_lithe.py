from functions import *
import time

nummer1 = True
nummer2 = False

print("Welkom in de Rekenmachine")
time.sleep(1)

diensten = """A) getallen optellen
B) getallen aftrekken
C) getallen vermenigvuldigen
D) getallen delen
E) getallen ophogen
F) getallen verlagen
G) getallen verdubbelen
H) getallen halveren
"""

first_round = True
while True:
    vraag = stel_vraag(diensten).lower()
    nummer2 = 0
    if first_round:
        nummer1 = float(stel_vraag("Welke getal? "))
        diensten += 'I) niks '

    if vraag == 'i':
        print("Einde  van het programma.")
        break

    elif vraag in ['a', 'b', 'c', 'd']:
        nummer2 = float(int(stel_vraag(f"Welke getal wil je {vraag} met {nummer1}? ")))

    resultaat = actie_kiezen(vraag, nummer1, nummer2)
    print(resultaat)
    nummer1 = resultaat
    first_round = False




