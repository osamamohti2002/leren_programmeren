
import random

scoor = 0
rondes = 20
poging = 10

while rondes > 0:
    geheime_getal = random.randint(1, 1000)
    while poging > 0:
        gok = int(input('gok een getal'))
        print(geheime_getal)
        verschil = abs(geheime_getal - gok)
        if gok == geheime_getal:
            scoor += 1
            rondes -= 1
            poging -= 10
            print(f'je hebt de eerste ronde gewonnen {scoor}')
            print(poging)
        elif verschil < 20:
            poging -= 1
            print(poging)
            print('je bent heel warm')
        elif verschil < 50:
            poging -= 1
            print(poging)
            print('je bent warm')
        elif gok < geheime_getal:
            poging -= 1
            print(poging)
            print('hoger')
        else:
            poging -= 1
            print(poging)
            print('lager')
    else:
        print('je hebt de eerste ronde verloren')
        rondes -= 1
        print(f'de geheime getal was {geheime_getal}')
        opnieuw = input('wil je stoppen')
        poging += 10
        if opnieuw == 'ja':
            break
    if rondes == 0:
        print('je hebt de 20 rondes gewoneen je bent een lagend')

        # else:
        #     print('fuck')
    # print('einde ')

