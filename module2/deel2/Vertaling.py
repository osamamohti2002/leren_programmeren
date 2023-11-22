# # Vraag de gebruiker om woorden en vertalingen in te voeren
# vertaalwoorden = {}
# aantal_woorden = int(input("Hoeveel woorden wil je vertalen?\n"))
#
# for _ in range(aantal_woorden):
#     origineel_woord = input("Voer een origineel woord in:\n")
#     vertaald_woord = input(f"Voer de vertaling van '{origineel_woord}' in:\n")
#     vertaalwoorden[origineel_woord] = vertaald_woord
#
# # Vraag de gebruiker om de oorspronkelijke tekst in te voeren
# originele_tekst = input("\nVoer de oorspronkelijke tekst in:\n")
#
# # Voer vertaling uit
# woorden = originele_tekst.split()
# vertaalde_tekst = ' '.join(vertaalwoorden.get(woord, woord) for woord in woorden)
#
# # Toon vertaalde tekst
# print("\nVertaalde tekst:")
# print(vertaalde_tekst)
# print(vertaalwoorden)


# Vraag de gebruiker om woorden en vertalingen in te voeren
vertaalwoorden = {input("Voer een origineel woord in:\n"): input(f"Voer de vertaling in:\n") for _ in range(int(input("Hoeveel woorden wil je vertalen?\n")))}

# Vraag de gebruiker om de oorspronkelijke tekst in te voeren
originele_tekst = input("\nVoer de oorspronkelijke tekst in:\n")

# Voer vertaling uit en toon direct
vertaalde_tekst = ''
for woord in originele_tekst.split():
    vertaalde_tekst += vertaalwoorden.get(woord, woord) + ' '

# Verwijder de extra spatie aan het einde
vertaalde_tekst = vertaalde_tekst.rstrip()

# Toon vertaalde tekst
print("\nVertaalde tekst:")
print(vertaalde_tekst)
