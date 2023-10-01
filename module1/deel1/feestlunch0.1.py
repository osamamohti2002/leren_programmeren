#kosten
CROISSANTJES = 0.39
STOKBRODEN = 2.78
KORTINGSBON = 0.50

#aantal wat nodig is
aantal_croissantjes = 17
aantal_stokbroden = 2
aantal_kortingsbonnen = 3

kosten_croissantjes = CROISSANTJES * aantal_croissantjes
kosten_stokbroden = STOKBRODEN * aantal_stokbroden
kortingsbonnen = KORTINGSBON * aantal_kortingsbonnen

total = kosten_croissantjes + kosten_stokbroden - kortingsbonnen

print(f'de feestlunch kost je bij de bakker {total} euro voor {aantal_croissantjes} en {aantal_stokbroden} als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn  ')


