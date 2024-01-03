from fruitmand import fruitmand

for i, fruit in enumerate(fruitmand):
    if fruit['name'] == 'druif':
        fruitmand.pop(i)
        break

print({fruit['color'] for fruit in fruitmand})