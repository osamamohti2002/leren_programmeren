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
    drank = input('wat wil je drinken')
    if drank not in DRANKJES:
        print('sorry geen idee wat je bedoeld, hier een glasje water')
        print('Einde Programma')
    else:
        if drank in DRANKJES[0] and naam in VIP_LIST:
            drank = DRANKJES[0]
            prijs = PRIJS_COLA









else:
    print('sorry je mag niet naar binnen')
    restende_jaren = 19 - leeftijd
    print(f'Probeer het in {restende_jaren} jaar nog eens')
# bij drank gebleven