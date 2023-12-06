PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de floowchart na

leeftijd = int(input('hoe oud ben je?'))
if leeftijd > 18:
    naam = input('wat is je naam?')
    if naam in VIP_LIST:
        if leeftijd >= 21:
            bandje = 'Blauw'
        else:
            bandje = 'rood'
        print(f'je krijgt van mij een {bandje} bandje')
    else:
        if leeftijd >= 21:
            print('je krijgt van mij een stempel')
        else:
            print('je krijgt geen stempel')
    drank = input('wat wil je drinken')
    if drank in DRANKJES[0] and naam in VIP_LIST:
        prijs = PRIJS_COLA
    elif drank in DRANKJES[1]:
        prijs = PRIJS_BIER
        if naam in VIP_LIST or leeftijd >= 21:
            if naam in VIP_LIST:
        print('cola')





else:
    print('sorry je mag niet naar binnen')
    restende_jaren = 19 - leeftijd
    print(f'Probeer het in {restende_jaren} jaar nog eens')
# bij drank gebleven