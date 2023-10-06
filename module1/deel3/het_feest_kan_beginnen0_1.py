#namen
mijn_naam = 'osama'
slb_naam = "jeuke"

# eisen
gastheer = input('Wie is het gaastheer? (niemand! laat het leeg )')
gasten = True
drank = True
chips = True

#stellingen

if gastheer.lower() == mijn_naam.lower():
    gastheer = True
    print('het feest kan beginnen')
elif gastheer.lower() == slb_naam.lower():
    gastheer = False
    print('geen feest')
elif gastheer.lower() == slb_naam:
    print('geen feest')

elif gastheer and (chips or drank) and gasten:
    print('het feest kan beginnen')
elif not gastheer:
    print("geen feest")

else:
    print('geen feest')


