def getPersonCashInGold(person_cash: dict) -> float:

    # Conversieratio's

    rates = {

        'platinum': 25,

        'gold': 1,

        'silver': 0.2,

        'copper': 0.1

    }

    total_gold = 0

    # Itereer over de gegeven valuta in de dictionary

    for currency, amount in person_cash.items():

        # Controleer of de valuta in de conversieratio's staat

        if currency in rates:

            # Converteer de hoeveelheid naar de equivalentie in goud en voeg toe aan het totaal

            total_gold += amount * rates[currency]

        else:

            print(f"Conversieratio voor {currency} is niet gedefinieerd.")

    return total_gold
