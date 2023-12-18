PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

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
    if (drank == 'cola' and naam in VIP_LIST) or (drank == 'bier' and (leeftijd >= 21 and naam in VIP_LIST)):
        print('Alstublieft, complimenten van het huis')
    elif (drank == 'cola' and naam not in VIP_LIST) or (drank == 'bier' and (leeftijd >= 21 and naam not in VIP_LIST)) or\
            (drank == 'champagne' and leeftijd >= 21 and naam in VIP_LIST):
        if drank == 'cola':
            prijs = PRIJS_COLA
        elif drank == 'bier':
            prijs = PRIJS_BIER
        else:
            prijs = PRIJS_CHAMPAGNE
        print(f'alsjeblieft je {drank} dat is dan {prijs}')
    elif drank == 'bier' or drank == 'champagne' and leeftijd < 21:
        print('Sorry je mag geen alcohol bestellen onder de 21')
        leeftijd_berekenen = 21 - leeftijd
        print(f'Probeer het in {leeftijd_berekenen} jaar nog eens')
    elif drank == 'champagne' and naam not in VIP_LIST:
        print('sorry alleen vips mogen champagne bestellen')
    else:
        print('sorry geen idee wat je bedoeld, hier een glaasje water')

else:
    print('sorry je mag niet naar binnen')
    leeftijd_berekenen = 18 - leeftijd
    print(f'Probeer het in {leeftijd_berekenen} jaar nog eens')









