import string
import random
import time




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

if password[11] in capital_letters or password[12] in capital_letters:
    password[11] = random.choice(small_letters or chars or numbers)
    password[12] = random.choice(small_letters or chars or numbers)


if password[-1] in small_letters or password[-1] in chars:
    password[-1] = random.choice(numbers or capital_letters)

if password[0] in chars:
    password[0] = random.choice(capital_letters or small_letters)


if password[1] in numbers or password[2] in numbers:
    password[1] = random.choice(capital_letters or small_letters or chars)
    password[2] = random.choice(capital_letters or small_letters or chars)


password = ''.join(password)
    
start = round(time.time() * 1000)
for _ in range(1000):
    password1 = password



einde = round(time.time() * 1000)

# print(einde - start)


print(password)
print(password[0])
print(password[1])
print(password[2])
print(password[11])
print(password[12])
print(password[-1])










