# maak een programma die herhaaldelijk (met een input) '?' zegt tot dat het resultaat
# daarvan gelijk is aan 'quit'.
# print het aantal iteraties (het aantal keren dat de vraag is gesteld)


aatal = 0
antwoord = ''

while antwoord.lower() != 'quit':
    antwoord = input('?')
    aatal += 1

print(f'het aantal keren {aatal}')