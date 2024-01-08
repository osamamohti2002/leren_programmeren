from fruitmand2 import fruitmand

for i, fruit in enumerate(fruitmand):
    if fruit['name'] == 'druif':
        fruitmand.pop(i)
        break

print(set(fruit['color'] for fruit in fruitmand))

