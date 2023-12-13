PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

BERICHT_1 = 'Alstublieft, complimenten van het huis'
BERICHT_2 = 'Alsjebleif je drank dat is dan'
BERICHT_3 = 'Sorry je mag geen alcohol bestellen onder de 21'
BERICHT_4 = 'Probeer het over in jaar nog eens'

#bouw hieronder de floowchart na

leeftijd = int(input('hoe oud ben je?'))
if leeftijd > 18:
    naam = input('wat is je naam')
    if naam in VIP_LIST:
        if leeftijd >= 21:
            bandje = 'blauw'
        else:
            bandje = 'rood'
        print(f'je krijgt van mij een {bandje} bandje')
    else:
        if leeftijd >= 21:
            print('je krijgt van mij een stempel')
    drank = input('wat wil je drinken')
    if drank in DRANKJES:
        if DRANKJES == 'cola':
            if naam in VIP_LIST:









