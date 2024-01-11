from random import *
import os

namen = ['osama', 'lithe', 'omar', 'ali']

print('voer minimaal 3 namen in')
while True:
    uniqeu_naam = input('voer een naam in en geef aan wanneer je wilt stoppen met (stop)')
    if uniqeu_naam == 'stop':
        if len(namen) >= 3:
            break
        else:
            print('je moet minimaal 3 namen invoeren')
    elif uniqeu_naam not in namen:
        namen.append(uniqeu_naam)
    else:
        print('invoer ongeldig')

for i in range(100):
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

    print("\nLootjes trekken gelukt! Hier is het resultaat:")
    for i in range(len(namen)):
        print(f"{namen[i]} trekt {lootjes[i]}")



