from functions import *

print("Welkom In onze Rekenmachine")
acties = """"
A) getallen optellen
B) getallen aftrekken
C) getallen vermenigvuldigen
D) getallen delen
E) getallen ophogen
F) getallen verlagen
G) getallen verdubblen
H) getallen halveren
'I) nits'

"""


eerste_ronde = False

while True:
    print(acties)
    vraag = stel_vraag('wat wil je kiezen? ').lower()
    nummer1 = float(stel_vraag('welke getal? '))
    nummer2 = float(stel_vraag(f'welke getal {vraag} bij nummer {nummer1}? '))
    choice, n1, n2 = actie_kiezen(vraag, nummer1, nummer2)
    # nummer1 = choice
    print(f'de antwoord is {choice}')
    eerste_ronde = True
    if eerste_ronde:
        acties += 'I) nits'
        if vraag == 'i':
            print('eind programma')
            break





