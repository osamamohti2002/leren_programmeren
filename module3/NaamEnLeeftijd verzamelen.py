def name_age():
    name = input('wat is je naam')
    age = int(input('wat is je leeftijd'))

    result = {
        'naam': name,
        'leeftijd': age
    }

    return result


def gegevens_verzamelen():
    gegevens = []
    while True:
        keuze = input('Toets (enter) om nog een persoon toe te voegen of (stop) om te stoppen').lower()
        if keuze == 'stop':
            break
        gegevens.append(name_age())
    return gegevens


informatie = gegevens_verzamelen()

for persoon in range(len(informatie)):
    print(f"{informatie[persoon]['naam']} is {informatie[persoon]['leeftijd']} jaar oud")

