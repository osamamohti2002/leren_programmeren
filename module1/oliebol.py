#eerste Functie
OLIEBOL_PRIJS = 99
PRIJS_10_OLIEBOLLEN = 750
# APPELFLAP_PRIJS = 149

AANTAL_OLIEBOLLEN = 11
# AANTAL_APPEELFLAPPEN = 0

aantal_oliebollen_zakken = AANTAL_OLIEBOLLEN // 10
aantal_lose_olibollen = AANTAL_OLIEBOLLEN  % 10

total_oliebollen_prijs = aantal_oliebollen_zakken * PRIJS_10_OLIEBOLLEN + aantal_lose_olibollen * OLIEBOL_PRIJS
totaal_eru = total_oliebollen_prijs / 100

print(totaal_eru)