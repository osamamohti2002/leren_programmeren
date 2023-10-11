a = int(input('voer a in '))
b = int(input('voer b in'))

if a > b :
    maximum = a
    print(f'a is het het grootset getal , {maximum} ')
    minimum = b
    print(f'het minimum is {minimum}')
    print(f'het maximum is {maximum}')


elif a < b :
    minimum = a
    print(f'a is de kleinste getal , {minimum}')
    maximum = b
    print(f'het minimum is {minimum}')
    print(f'het maximum is {maximum}')

else:
    print('a en b zijn even groot')
    minimum = a
    maximum = b
    print(minimum)
    print(maximum)