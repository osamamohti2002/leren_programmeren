# import random
#
# # Definieer de rangen en kleuren
# kaarten = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Heer', 'Aas']
# soorten = ['Harten', 'Ruiten', 'Klaveren', 'Schoppen']
#
# # Genereer het volledige kaartspel
# deck = []
#
# for kaart in kaarten:
#     for soort in soorten:
#         kaart = f'{kaart} {soort}'
#         deck.append(kaart)
#
# # Schud het kaartspel
# random.shuffle(deck)
#
# # Toon de eerste 5 kaarten in het kaartspel
# for i, kaart in enumerate(deck[:7]):
#     print(f'Kaart {i+1}: {kaart}')
# # Toon de overgebleven kaarten in het kaartspel
# print(f'Rest van de kaarten in het kaartspel ({len(deck)-5} overgebleven):')
# print(deck[7:])
#
import random

# Definieer de rangen en kleuren
kaarten = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Heer', 'Aas']
soorten = ['Harten', 'Ruiten', 'Klaveren', 'Schoppen']
jokers = ['joker', 'joker']

# Genereer het volledige kaartspel
deck = []


for kaart in kaarten:
    for soort in soorten:
        huidige_kaart = f'{kaart} {soort}'
        deck.append(huidige_kaart)

# Schud het kaartspel
deck.extend(jokers)
random.shuffle(deck)

for _ in range(7):
    print(deck.pop(0))

print(deck)
print(len(deck))


# # Toon de eerste 7 kaarten in het kaartspel
# for i, kaart in enumerate(deck[:7]):
#     print(f'Kaart {i+1}: {kaart}')
#
# # Toon de overgebleven kaarten in het kaartspel
# print(f'Rest van de kaarten in het kaartspel ({len(deck)-7} overgebleven):')
# print(deck[7:])
