from fruitmand2 import fruitmand

gesorteerde_fruit_op_gewicht = sorted(fruitmand, key=lambda fruit: fruit['weight'], reverse=True)

for fruit in gesorteerde_fruit_op_gewicht:
    gewicht_in_kg = fruit['weight'] / 1000
    print(f"{fruit['name']} : {gewicht_in_kg} kg")

