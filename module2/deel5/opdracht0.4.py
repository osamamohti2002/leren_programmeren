from fruitmand import fruitmand
import random

getal = int(input('voer de aantal fruit in'))

for _ in range(getal):
    fruit = random.choice(fruitmand)['name']
    print(fruit)
