som = 0
while True:
    antwoord = input('quit of getal')
    if antwoord == 'quit':
        break
    try:
        som += int(antwoord)
    except ValueError:
        print('GETAL OF QUIT')


print(som)