from random import shuffle
import os
import time

namen_lijst = []

print("Start de programma")

while True:
    naam = input("Schrijf je naam in: ")

    if naam.isalpha():
        if naam not in namen_lijst:
            namen_lijst.append(naam)

            if len(namen_lijst) >= 3:
                vraag_aantal = input("Wil je nog een naam toevoegen? Antwoord met ja/nee: ")
                if vraag_aantal.lower() == 'ja':
                    continue
                else:
                    break
        else:
            print('Je hebt deze naam al toegevoegd')
    else:
        print('Voer een geldige naam in (alleen letters toegestaan).')

shuffle(namen_lijst)

lootjes_dict = {}

for i in range(len(namen_lijst)):
    gever = namen_lijst[i]
    ontvanger = namen_lijst[(i + 1) % len(namen_lijst)]
    lootjes_dict[gever] = ontvanger

print("Nu zijn de lootjes geheim getrokken.")

while True:
    vraag_naam = input("Voer een naam in om het bijbehorende lootje te zien (typ 'stop' om te stoppen): ")
    if vraag_naam.lower() == 'stop':
        break
    elif vraag_naam in lootjes_dict:
        print(f'{vraag_naam} trekt lootje voor {lootjes_dict[vraag_naam]}')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('Ongeldige naam, probeer opnieuw.')

print("Einde programma")



