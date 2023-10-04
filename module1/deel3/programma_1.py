getal_1 = int(input('voer getal 1 in '))
getal_2 = int(input('voer getal 2 in'))

if getal_1 > getal_2 :
    max = getal_1
    print(f'getal 1 is het het grootset getal , {getal_1} ')
    print(max)

elif getal_1 < getal_2:
    min = getal_1
    print(f'{getal_1} is de kleinste getal , {getal_1}')

else:
    print('getal 1 en getal 2 zijn even groot')