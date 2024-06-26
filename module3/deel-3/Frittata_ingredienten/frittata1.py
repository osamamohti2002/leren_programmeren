from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons('Voor hoeveel personen is het recept? ')# replace this with better input


# ----- CALCULATIONS ----
# calculate factor
factor = nr_persons / RECIPE_PERSONS

# calculate amount_eggs
amount_eggs = round_piece(AMOUNT_EGGS * factor)

# calculate amount_milk
amount_milk = round_quarter(AMOUNT_MILK * factor)
print(AMOUNT_MILK * factor)
# calculate amount_salt
amount_salt = round_quarter(AMOUNT_SALT * factor)

# calculate amount_pepper
amount_pepper = round_quarter(AMOUNT_PEPPER * factor)

# calculate amount_oil
amount_oil = round_quarter(AMOUNT_OIL * factor)

# calculate amount_onions
amount_onions = round_piece(AMOUNT_ONIONS * factor)

# calculate amount_garlics
amount_garlics = round_piece(AMOUNT_GARLICS * factor)

# calculate amount_spinach
amount_spinach = round_quarter(AMOUNT_SPINACH * factor)

# calculate amount_paprikas
amount_paprikas = round_piece(AMOUNT_PAPRIKAS * factor)

# calculate amount_cheese
amount_cheese = round_quarter(AMOUNT_CHEESE * factor)



# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')

print(f"* {amount_eggs} {TXT_EGGS}")
# calculate amount_milk
print(f'* {amount_milk} {UNIT_CUPS} {TXT_MILK}')
# calculate amount_salt
print(f"* {amount_salt} {UNIT_TEASPOONS} {TXT_SALT}")
# calculate amount_pepper
print(f"* {amount_pepper} {UNIT_TEASPOONS} {TXT_PEPPER}")
# calculate amount_oil
print(f"* {amount_oil} {UNIT_SPOONS} {TXT_OIL}")
# calculate amount_onions
print(f'* {amount_onions} {TXT_ONIONS}')
# calculate amount_garlics
print(f'* {amount_garlics} {TXT_GARLICS}')
# calculate amount_spinach
print(f'* {amount_spinach} {UNIT_CUPS} {TXT_SPINACH}')
# calculate amount_paprikas
print(f'* {amount_paprikas} {TXT_PAPRIKAS}')
# calculate amount_cheese
print(f"* {amount_cheese} {TXT_CUPS} {TXT_CHEESE}")
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print('-----------------------------------------------')






