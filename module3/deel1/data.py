def name_age():
    name = input('wat is je naam')
    age = int(input('wat is je leeftijd'))
    city = input('waar woon je')

    result = {
        'naam': name,
        'leeftijd': age,
        'city': city
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


