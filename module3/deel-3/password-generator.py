import string
import random

# ==== Random 2 tot 6 hoofdletters ==== #
# ==== Een hoofdletter mag niet op de twee middelste posities staan ==== #
# ==== minimaal 8 klein letters ==== #
# ==== Het wachtwoord mag niet met een klein letter eindigen ==== #
# ==== 3 special tekens uit de volgende reeks @ # $ % & _ ? ==== #
# ==== de special tekens mogen niet op de eerste en laateste positie staan ==== #
# ==== random 4 tot 7 cijfers (0 t/m 9) ==== #
# ==== op de eerste 3 positie mag geen cijfer staan  ==== #

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 

# klein letters berekenen aan hert einde
def password_generator():
    num_capitals = random.randint(2, 6)
    num_numbers = random.randint(4, 7)
    num_chars = 3

    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    numbers = string.digits
    chars = "@#$%&_?"
    password = []

    password.extend(random.choices(capital_letters, k=num_capitals))
    password.extend(random.choices(numbers, k=num_numbers))
    password.extend(random.choices(chars, k=num_chars))

    overige_lengte = 24 - (num_capitals + num_numbers + num_chars)
    password.extend(random.choices(small_letters, k=overige_lengte))

    random.shuffle(password)

    while (password[0] in chars or password[-1] in chars) \
            or (password[0] in numbers or password[1] in numbers or password[2] in numbers) \
            or (password[11] in capital_letters or password[12] in small_letters) \
            or (password[-1] in small_letters):
        random.shuffle(password)

    password = ''.join(password)
    
    return password




generated_password = password_generator()
print(f"De random wachtwoord is {generated_password}")

print("-----------------------")
print(len(generated_password))
print("-----------------------")
print(generated_password[0])
print("-----------------------")
print(generated_password[-1])
print("-----------------------")
print(generated_password[11])
print(generated_password[12])















