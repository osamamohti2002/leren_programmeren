getal1 = 50
getal2 = 50

antwoord = 50

while antwoord < 1000:
    getal1 = getal1 + 1

    getal2 = f"{getal2} + {getal1}"

    antwoord = antwoord + getal1

    print(f"{getal2} = {antwoord}")