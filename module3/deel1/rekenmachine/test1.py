# rekenmachine.py
from test2 import *

print("Welkom In onze Rekenmachine")

first_round = True
n1 = None

while True:
    if first_round:
        print("wat wilt u doen?")
    else:
        print(f"Wil je wat met de uitkomst ({uitkomst}) doen?")

    acties = """
    A) getallen optellen
    B) getallen aftrekken
    C) getallen vermenigvuldigen
    D) getallen delen
    E) getallen ophogen
    F) getallen verlagen
    G) getallen verdubbelen
    H) getallen halveren
    I) niets
    """
    print(acties)

    choice = input('Wat wil je kiezen? ').upper()

    if choice == 'I':
        print('Eind programma')
        break

    if first_round or choice in ['E', 'F', 'G', 'H']:
        n1 = float(input('Welke getal? '))

    if choice in ['E', 'F']:
        n2 = 1
    elif choice in ['G', 'H']:
        n2 = 2
    else:
        n2 = float(input(f'Welk getal bij nummer {n1}? '))

    if choice == 'A':
        uitkomst = addition(n1, n2)
        print(f"{n1} + {n2} = {uitkomst}")
    elif choice == 'B':
        uitkomst = subtraction(n1, n2)
        print(f"{n1} - {n2} = {uitkomst}")
    elif choice == 'C':
        uitkomst = multiplication(n1, n2)
        print(f"{n1} * {n2} = {uitkomst}")
    elif choice == 'D':
        uitkomst = division(n1, n2)
        print(f"{n1} / {n2} = {uitkomst}")
    elif choice == 'E':
        uitkomst = addition(n1, n2)
    elif choice == 'F':
        uitkomst = subtraction(n1, n2)
    elif choice == 'G':
        uitkomst = multiplication(n1, n2)
    elif choice == 'H':
        uitkomst = division(n1, n2)

    first_round = False
