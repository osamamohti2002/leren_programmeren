PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de floowchart na
leeftijd = int(input('Hoe oud ben je?'))
if leeftijd > 18:
    naam = input('Wat is je naam')
    if naam in VIP_LIST:
        print('je naam staat in de vip lijst je kan lekker door')
        if leeftijd >= 21:
            print('je krijgt een blouwe bandje')
            drank = input('wat wil je drinken')
        else:
            print('je krijgt een rode bandje')
            drank = input('wat wil je drinken')
    else:
        if leeftijd >= 21:
            print('je krijgt van mij een stempeltje')
        else:
            drank = input('wat wil je drinken')

else:
    print('je mag niet naar binnen')
    print('probeer over aantal jaar nog eens')
