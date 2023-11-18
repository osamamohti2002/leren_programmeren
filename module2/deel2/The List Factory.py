# aantal_lijstjes = int(input("Voer het aantal lijstjes in: "))
#
#
# lijst = []
# for i in range(aantal_lijstjes):
#     langte = int(input('wat is de langte van je lijst'))
#     gegenereerde_lijst = list(range(i, (i * langte) + 1))
#     lijst.append(gegenereerde_lijst)
#     print(lijst)
#
# for i, lijst in enumerate(lijst, start=1):
#     print(f"Lijstje {i}: {lijst}")
#


# lijst.append(langte)
# print(lijst)

aantal_lijstjes = int(input("Voer het aantal lijstjes in: "))


lijst = []
for i in range(aantal_lijstjes * 1):
    langte = int(input('wat is de langte van je lijst'))
    lijst.append(langte)
    print(lijst)
for i in lijst:
    print(i)






# for i in lijst:
#     print(i)
# stap 2 for loop maken en lengtes vragen -> list
# stap 3 for elke iests in in de list
#stap 4 de gegenereerde  langte toevoegen aan de gegenereerde  lijsten
