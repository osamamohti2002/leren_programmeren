from fruitmand2 import fruitmand

beschiekbare_kleuren = []

for fruit in fruitmand:
    if fruit['color'] not in beschiekbare_kleuren:
        beschiekbare_kleuren.append(fruit['color'])

while True:
    gekozen_kleur = input('voer een kleur in ').lower()
    if gekozen_kleur in beschiekbare_kleuren:
        print(f'je hebt gekozen voor de kleur {gekozen_kleur}')
        break
    else:
        print(f'de kleur {gekozen_kleur} zit er niet in de fruitmand')

aantal_ronde = 0
aantal_niet_ronde = 0

for fruit in fruitmand:
    if fruit['color'] == gekozen_kleur:
        if fruit['round']:
            aantal_ronde += 1
        else:
            aantal_niet_ronde += 1

if aantal_ronde > aantal_niet_ronde:
    verschil = aantal_ronde - aantal_niet_ronde
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
elif aantal_ronde < aantal_niet_ronde:
    verschil = aantal_niet_ronde - aantal_ronde
    print(f"Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
else:
    print(f"Er zijn {aantal_ronde} ronde vruchten en {aantal_niet_ronde} niet ronde vruchten in de kleur {gekozen_kleur}")

