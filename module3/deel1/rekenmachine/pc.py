from functions import *


nummer2 = False
print("Welkom In onze Rekenmachine")
vraag = stel_vraag('A) getallen optellen\n'
                   'B) getallen aftrekken\n'
                   'C) getallen vermenigvuldigen\n'
                   'D) getallen delen\n'
                   'E) getallen ophogen\n'
                   'F) getallen verlagen\n'
                   'G) getallen verdubblen\n'
                   'H) getallen halveren\n'
                   'kies: ').lower()
if vraag in ['e', 'f', 'g', 'h']:
    nummer1 = float(int(stel_vraag('welke getal')))
else:
    nummer1 = float(int(stel_vraag('welke getal')))
    nummer2 = float(int(stel_vraag(f'welke getal met {nummer1}')))
choice = actie_kiezen(vraag, nummer1, nummer2)
print(choice)
while True:
    vraag = stel_vraag(f'wat wil je met {choice} doen\n'
                       f'A) iets optellen\n'
                       f'B) iets aftrekken\n'
                       f'C) met iets vermenigvuldigen \n'
                       f'D) ergens door delen\n'
                       f'E) ophogen\n'
                       f'F) verlagen\n'
                       f'G) verdubbelen \n'
                       f'H) halveren \n'
                       f'I) niets?\n'
                       f'kies: ')
    if vraag == 'i':
        print('eind het programma')
        break
    elif vraag in ['e', 'f', 'g', 'h']:
        nummer1 = choice
    else:
        nummer2 = float(int(stel_vraag(f'welke getal met {choice}')))
    choice = actie_kiezen(vraag, choice, nummer2)
    print(choice)

