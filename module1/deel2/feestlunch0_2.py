# Prijzen
croissantjes_prijs = float(input('hoeveel kost een croissantje in centen?'))
stokbroden_prijs = float(input('hoeveel kost een stokbroden in centen?'))
kortingsbon= float(input('voer de waarde van een kortingsbon in centen'))

# #aantal wat nodig is
aantal_croissantjes = int(input('hoeveel coissantjes heb je nodig'))
aantal_stokbroden = int(input('hoeveel stokbroden heb je nodig'))
aantal_kortingsbonnen = int(input('heb je kortingsbon, zo je voer het aantal kortingsbonnen in'))

# brekening
kosten_croissantjes = croissantjes_prijs * aantal_croissantjes
kosten_stokbroden = stokbroden_prijs * aantal_stokbroden
kortingsbonnen = kortingsbon * aantal_kortingsbonnen
total = kosten_croissantjes + kosten_stokbroden - kortingsbonnen
print(f'de feestlunch kost je bij de bakker {total} euro voor {aantal_croissantjes} en {aantal_stokbroden} als de {aantal_kortingsbonnen} kortingsbonnen nog gedig zijn  ')





