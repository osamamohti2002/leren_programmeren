# tekst = 'dit is een tekst'
# tekst_2 = 'a'
#
# # Dit is een manier om net zo vaak code uit te voeren als dat je vooraf wilt weten
# for i in range(len(tekst)):
#     print(tekst[i])

for x in range(4):
    print('je bent eri')


# # De c verandert per interatie in het karakter wat dan aan de beurt is. Hij begint bij index 0
# for c in tekst:
#     print(c)


tekst_3 = 'Abba was erg populier in de jaren 70'
telling = 0
for i in tekst_3:
    if i == 'a' or i == 'A':
        telling += 1
        print(f'dit is mijn {telling} en {i}')
print(telling)
