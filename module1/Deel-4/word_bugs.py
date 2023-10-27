a = len(input('Geef een woord: '))
b = len(input('Geef nog een woord: '))

if a > b:
    print('Woord a heeft meer letters dan woord b')
elif a < b:
    print('Woord a heeft minder letters dan woord b')
else:
    print('Woord a en woord b hebben evenveel letters')
