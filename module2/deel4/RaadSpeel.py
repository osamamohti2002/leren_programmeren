import random


# ronde = 0
# scoor = 0

# while scoor < 20:
#     getal_raden = int(input('raad een getal tussen 1 en 1000'))
#     getal = random.randint(1, 1000)
#     if getal_raden == getal:
#         print(getal_raden)
#         stoppen = input('wil je door gaan?')
#         if stoppen != 'ja':
#             continue
#         else:
#             break
#
#     else:
#         print(getal)
#
#

# while scoor < 20:
#     geraden_getal = int(input('raad een getal tussen 1 en 1000'))
#     getal = 100
#     if geraden_getal == getal:
#         ronde += 1
#         scoor += 1
#         print(f'goed gedaan je hebt nu in ronde {ronde} en je scoor is {scoor}')
#         print(getal)
#     else:
#         warm = getal - geraden_getal
#         if warm <= 50:
#             print('je bent warm')
#             print(getal)
#         elif warm >= 20:
#             print('je bent heel warm')
#             print(getal)
#         print(getal)


import random

geheim_getal = 1
score = 0
ronde = 0
for ronde in range(1, 21):
    gok = int(input("Raad een getal tussen 1 en 1000: "))
    verschil = abs(geheim_getal - gok)
    if verschil < 20:
        print("Je bent heel warm")
    elif verschil < 50:
        print("Je bent warm")
    elif gok == geheim_getal:
        print("Gefeliciteerd, je hebt het geraden!")
        score += 1
        print(score)
        break
    elif gok < geheim_getal:
        print("Hoger")
    else:
        print("Lager")
    print(geheim_getal)
    ronde += 1
    print(ronde)

print(f"\nScore na {ronde} ronden: {score}")
