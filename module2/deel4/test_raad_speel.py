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
            print(f'je hebt dit ronde gewonnen en je moet nog {rondes} te gaan. je scoor is {scoor}')
        elif verschil < 20:
            poging -= 1
            print('je bent heel warm')
        elif verschil < 50:
            poging -= 1
            print('je bent warm')
        elif gok < geheime_getal:
            poging -= 1
            print('hoger')
        elif gok > geheime_getal:
            poging -= 1
            print('lager')
        else:
            print(f'je hebt dit ronde verloren je hebt nog {rondes} te gaan')
            rondes -= 1
            print(f'de geheime getal was {geheime_getal}')
    else:
        opnieuw = input('wil je stoppen')
        poging += 10
        if opnieuw == 'ja':
            break
    if rondes == 0:
        print(f'goed gespeeld je scoor is {scoor}')
    elif rondes == 0 and scoor == 20:
        print('je bent een lagend je hebt goed gewonne')

