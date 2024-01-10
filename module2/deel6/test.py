from random import shuffle

namen = ['osama', 'lithe', 'omar', 'ali']

print('Voer minimaal 3 namen in')
while True:
    unieke_naam = input('Voer een naam in en typ "stop" wanneer je wilt stoppen: ')
    if unieke_naam == 'stop':
        if len(namen) >= 3:
            break
        else:
            print('Je moet minimaal 3 namen invoeren')
    elif unieke_naam not in namen:
        namen.append(unieke_naam)
    else:
        print('Ongeldige invoer')

while True:
    lootjes = [] + namen
    shuffle(lootjes)

    dubbel_check = False
    for i in range(len(namen)):
        if namen[i] == lootjes[i]:
            dubbel_check = True
            break

    if not dubbel_check:
        break
    else:
        print("Iemand heeft zijn/haar eigen lootje getrokken. Opnieuw proberen...")

print("\nLootjes trekken gelukt! Uitslag blijft geheim.")

# Uitbreiding: Toewijzing van lootjes opvragen
while True:
    vraag_naam = input('Voer een naam in om de toewijzing van het lootje te zien, of typ "stop" om te eindigen: ')
    if vraag_naam == 'stop':
        break
    elif vraag_naam in namen:
        index = namen.index(vraag_naam)
        toegewezen_naam = lootjes[index]
        print(f"{vraag_naam} heeft lootje van {toegewezen_naam}")
    else:
        print('Ongeldige naam. Probeer opnieuw.')
