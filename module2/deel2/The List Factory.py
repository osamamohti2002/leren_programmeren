# lijst = int(input('aantal'))
# LIJST = []
# for item in range(lijst):
#     langte = int(input('langte'))
#     LIJST.append(item)
#
#     print(LIJST)
#
# main_lijst = []
# aantal_lijsten = int(input('hoe veel lijsten'))
#
# for lijst in range(aantal_lijsten):
#     langte = int(input(f'hoe veel elementen moet er in {lijst}'))
#     main_lijst.append(lijst)
#     # print(lijst)
#     # print(main_lijst)
#     for i in range(langte):
#         lijst = []
#         lijst.append(langte)
#         print(lijst)
#     main_lijst.append(lijst)
#
#
# print(main_lijst)



# main_lijst = []
# aantal_lijsten = int(input('hoeveel lijsten'))
# for lijst in range(aantal_lijsten):
#     langte = int(input(f'hoe lang is list {lijst + 1} '))
#     genereerd_lijst = []
#     # print(len(genereerd_lijst))
#     # main_lijst.append(genereerd_lijst)
#     # print(main_lijst)
#     for ele in range( langte):
#         element = lijst * ele
#         genereerd_lijst.append(element)
#     main_lijst.append(genereerd_lijst)
#     print(genereerd_lijst)
# print(main_lijst)




# for lijst in range(0, aantal_lijsten):
#     print(main_lijst)
#     elements = int(input('voeg je elements toe'))
#     main_lijst.append(elements)
#
# print(main_lijst)
# print(len(main_lijst))
#
#

# main_lijst = []
# aantal_lijsten = int(input('Hoeveel lijsten: '))
#
# for lijst_index in range(aantal_lijsten):
#     lengte = int(input(f'Hoeveel elementen moeten er in lijst {lijst_index}: '))
#     inner_list = []
#
#     for i in range(lengte):
#         element = input(f'Geef element voor lijst {lijst_index}: ')
#         inner_list.append(element)
#
#     main_lijst.append(inner_list)
#
# print(main_lijst)


aantal_lijsten = int(input("Voer het aantal lijstjes in: "))
lege_lijst =[]
for lijst in range(1, aantal_lijsten + 1):
    lengte_lijst = int(input(f"Voer de lengte in voor lijst {lijst}: "))

    lijstje = list(range(1, lengte_lijst * lijst + 1, lijst))
    lege_lijst.append(lijstje)
    print(f"Lijst {lijst}: {lijstje}")
print(lege_lijst)