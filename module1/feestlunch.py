#kosten
CROISSANTJES = 0.39
STOKBRODEN = 2.78
KORTINGSBON = 0.50

#aantal wat nodig is
AANTAL_CROISSANTJES = 17
AANTAL_STOKBRODEN = 2
AANTAL_KORTINGSBONNEN = 3

kosten_croissantjes = CROISSANTJES * AANTAL_CROISSANTJES
kosten_stokbroden = STOKBRODEN * AANTAL_STOKBRODEN
kortingsbonnen = KORTINGSBON * AANTAL_KORTINGSBONNEN

total = kosten_croissantjes + kosten_stokbroden - kortingsbonnen
print(total)

