import random

m_en_m = ('groen', 'oranje', 'blauw', 'bruin')
aantal_m_en_ms =int(input("Hoe veel M&M's wil je hebben"))

zak = []

for _ in range(aantal_m_en_ms):
    kleur = random.choice(m_en_m)
    zak.append(kleur)

print(f"Inhoud van zak met M&M's: {zak}")

