from fruitmand2 import fruitmand
import random

getal = int(input('voer aantal in '))

for _ in range(getal):
    fruit = random.choice(fruitmand)['name']
    print(fruit)
