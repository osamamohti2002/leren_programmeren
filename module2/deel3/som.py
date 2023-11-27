# maak een programma dat getallen vanaf 50 dus (50 , 51, 53 ,54 enzovoort) optelt
# totdat hun gezamelijke som groter is dan 1000
# print elke cijfer en de totaal som per iteratie , zoals dit:
#
# 1. 50+51 = 101
# 2. 50+51+52 = 153
# 3. 50+51+52+53 = 206
# 4. 50+51+52+53+54 = 260
#

total = 0
current_number = 50
iteration = 1

while total <= 1000:
    total += current_number
    current_number += 1
    iteration += 1
    print(f"{iteration}. {current_number} * {current_number} = {total}")
