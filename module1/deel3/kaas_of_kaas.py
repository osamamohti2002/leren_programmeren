print('Welkom in het speeltje KAAS OF KAAS ')
print('In deze speeltje gaan we jou vragen stellen en op basis daar van zullen de juiste soort kaas raden')
print('graag antwoorden met ja of nee')

# het begin van het speeltje
start = input('Is de kaas geel ?').lower()



# midden 1 van het speeltje
midden_1 = 'Zitter er gaten in?'

#het einde van het speeltje midden game 1
eind_1 = 'Is de kaas belachelijk duur?'
eind_2 = 'Is de kaas hard als steen?'

# antwoorden van midden game 1
antwoord_1 = 'Emmenthaler'
antwoord_2 = 'Leerdammer'
antwoord_3 = 'Parmigiano Reggiano'
antwoord_4 = 'Goudse kaas'



# midden 2 van het speeltje
midden_2 = 'Heeft de kaas blauwe schimmel?'

#het einde van het speeltje midden 2

eind_3 = 'Heeft de kaas korst?'
eind_4 = 'Heeft de kaas korst?'

# antwoorden van midden game 2

antwoord_5 = 'Blue de Rochbaron'
antwoord_6 ="Foume d'ambert"
antwoord_7 = 'Camembert'
antwoord_8 = 'Mozzarella'

#start
if start == 'ja':
    midden_1 = input(midden_1).lower()

elif start == 'nee':
    midden_2 = input(midden_2).lower()
#midden game 1
if midden_1 == 'ja':
    eind_1 = input(eind_1).lower()
elif midden_1 == 'nee':
    eind_2 = input(eind_2).lower()

#midden game 2

if midden_2 == 'ja':
    eind_3 = input(eind_3).lower()
elif midden_2 == 'nee':
    eind_4 = input(eind_4).lower()

# eind game 1

if eind_1 == 'ja':
    print(f'je antwoord is {antwoord_1}')
elif eind_1 == 'nee':
    print(f'je antwoorde is {antwoord_2}')

# eind game 2

if eind_2 == 'ja':
    print(f'je antwoord is {antwoord_3}')
elif eind_2 == 'nee':
    print(f'je antwoord is {antwoord_4}')


# eind game 3

if eind_3 == 'ja':
    print(f'je antwoord is {antwoord_5}')
elif eind_3 == 'nee':
    print(f'je antwoord is {antwoord_6}')

# eind game 4

if eind_4 == 'ja':
    print(f'je antwoord is {antwoord_7}')
elif eind_4 == 'nee':
    print(f'je antwoord is {antwoord_8}')

