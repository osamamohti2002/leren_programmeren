antwoord_1 = input('Is de kaas geel?')

if antwoord_1 == 'ja':
    gaten = input('zitten er gaten in?')
    if gaten == 'ja':
        belachelijk = input('Is de kaas belachelijk duur?')
        if belachelijk == 'ja':
            print('emmenthaler')
        elif belachelijk == 'nee':
            print('leerdammer')
    elif gaten == 'nee':
        steen = input('is de kaas hard als steen')
        if steen == 'ja':
            print('parmingiano reggiano')
        elif steen == 'nee':
            print('goudse kaas ')
elif antwoord_1 == 'nee':
    schimmel = input('heeft de kaas blauwe schimmel?')
    if schimmel == "ja":
        korst_1 = input('heeft da kaas korst?')
        if korst_1 == 'ja':
            print('blue de rochbaron')
        elif korst_1 == 'nee':
            print("Foume d'ambert")
    elif schimmel == 'nee':
        korst_2 = input('Heeft de kaas korst?')
        if korst_2 == "ja":
            print('camembert')
        elif korst_2 == 'nee':
            print('mozzarella')
else:
    print('ongeldige invoer')



