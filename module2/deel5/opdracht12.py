from fruitmand import fruitmand


def fruit_langte(fruit):
    return len(fruit['name'])


kleuren_vertaling = {
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'red': 'rood',
    'brown': 'bruin'
}
langste_fruit_naam = max(fruitmand, key=fruit_langte)
vertaalde_kleuren = kleuren_vertaling[langste_fruit_naam['color']]

print(f"Kleur: {vertaalde_kleuren}, Gewicht: {langste_fruit_naam['weight']} gram, Naam: {langste_fruit_naam['name']} heeft {len(langste_fruit_naam['name'])} "
      f"letters ")