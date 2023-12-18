import random

scoor = 0
rondes = 20
poging = 10

while rondes > 0:
    geheime_getal = random.randint(1, 1000)
    print(geheime_getal)
    while poging > 0:
        gok = int(input('gok een getal '))
        verschil = abs(geheime_getal - gok)
        if gok == geheime_getal:
            scoor += 1
            rondes -= 1
            poging -= poging
            print(f'je hebt de eerste ronde gewonnen je hebt nog {rondes} rondes te gaan, je scoor is {scoor}')
            # break is duidelijker
        elif gok < geheime_getal:
            print('hoger')
        elif gok > geheime_getal:
            print('lager')

        if verschil < 20 and gok != geheime_getal:
            print('je bent heel warm')
        elif verschil < 50 and gok != geheime_getal:
            print('je bent warm')

        poging -= 1
        if poging == 0:
            print('je hebt de dit ronde verloren')
            rondes -= 1
            print(f'de geheime getal was {geheime_getal}')

    opnieuw = input('wil je stoppen? ')
    poging += 10
    if opnieuw == 'ja':
        print(f'goed gespeeld je scoor is {scoor}')
        break

    if rondes == 0 and scoor == 20:
        print('je hebt de 20 rondes gewonnen je bent een goat')
    elif rondes == 0 and scoor > 0:
        print(f'je hebt goed gespeeld je scoor is {scoor} ')
