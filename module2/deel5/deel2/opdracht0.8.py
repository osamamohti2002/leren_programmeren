from fruitmand2 import fruitmand

watermolen = {
    'name': 'watermolen',
    'weight': 2500,
    'color': 'green',
    'round': True
}

fruitmand.append(watermolen)

total_gewicht = 0

for fruit in fruitmand:
    total_gewicht += fruit['weight']

print(total_gewicht)
