import random

rondes = 20
scoor = 0



for ronde in range(1, 21):
    geheime_getal = random.randint(1, 1000)
    print(geheime_getal)
    gok = int(input('gok een getal tussen 1 en 1000'))
    verschil = abs(geheime_getal - gok)
    if gok == geheime_getal:
        rondes -= 1
        scoor += 1
        print(f'goed gedaan je hebt nog {rondes} rondes over en je scoor is {scoor}')
        opnieuw = input('wil je stoppen')
        if opnieuw == 'ja':
            break
    elif verschil < 20:
        print('je bemn heel warm')
    elif verschil < 50:
        print('je bent warm')
    elif gok < geheime_getal:
        print('hoger')
    else:
        print('lager')
    if ronde == 10 and scoor == scoor:
        print('je hebt verloren ')
        break
    elif rondes == 0:
        print('je bent legend je hebt alles geraden')
        print(f'je scoor {scoor}')
        break
