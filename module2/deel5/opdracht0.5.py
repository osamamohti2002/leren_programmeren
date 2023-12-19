from fruitmand import fruitmand
#
# # Omkeren van de volgorde van de fruitmand
# fruitmand.reverse()
#
# # Print stuk voor stuk de namen van het fruit in omgekeerde volgorde
# for fruit in fruitmand:
#     print(fruit['name'])




# Omkeren van de volgorde van de fruitmand
for index in range(len(fruitmand) - 1, -1, -1):
    print(fruitmand[index]['name'])
