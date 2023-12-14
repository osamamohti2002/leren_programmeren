PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

BERICHT_1 = 'Alstublieft, complimenten van het huis'
BERICHT_2 = 'Alsjebleif je drank dat is dan'
BERICHT_3 = 'Sorry je mag geen alcohol bestellen onder de 21'
BERICHT_4 = 'Probeer het over in jaar nog eens'

print("Start programma")
leeftijd = int(input("Hoe oud ben je? "))
if leeftijd > 18:
    naam = input('Wat is je naam? ')
    if naam in VIP_LIST:
        if leeftijd >= 21:
            bandje = 'blauw'
        else: 
            bandje = 'rood'
        print(f'Je krijgt van mij een {bandje} bandje')
    else:
        if leeftijd >= 21:
            print("Je krijgt van mij een stempel")
    drank = input("Wat wil je drinken? ")
    if drank in DRANKJES:
        if drank == 'cola':
            if naam in VIP_LIST:
                print(BERICHT_1) 
            else:
                print(BERICHT_2, PRIJS_COLA)
        if drank == 'bier':
            if naam in VIP_LIST and leeftijd >= 21:
                print(BERICHT_1)
            elif leeftijd >= 21:
                print(BERICHT_2, PRIJS_BIER)
            else:
                print(BERICHT_3)
                leeftijd_berkenen = 21 - leeftijd                       
                print(f'probeer over {leeftijd_berkenen} jaar nog eens')
        if drank == 'champagne':
            if naam in VIP_LIST and leeftijd >= 21:
                print(BERICHT_2, PRIJS_CHAMPAGNE)
            elif naam in VIP_LIST:
                print(BERICHT_3)
                leeftijd_berkenen = 21 - leeftijd
                print(f'probeer over {leeftijd_berkenen} jaar nog eens')
            else:
                print("Sorry alleen vips mogen champagne bestellen")
    else:
        print('Sorry geen idee wat je bedoeld, hier een glasje water')
else:
    print('Sorry je mag niet naar binnen')
    leeftijd_berkenen = 19 - leeftijd
    print(f'probeer over {leeftijd_berkenen} jaar nog eens')
print("Einde programma")
