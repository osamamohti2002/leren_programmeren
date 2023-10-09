def start_the_party(gastheer, gasten, drank, chips):
    start = 'No Party'
    if (gastheer or gasten and (chips and drank)):
        start = 'Start the Party'
    return start


# Alleen chips is geen feest.
# Een feest met chips, maar zonder drank kan niet beginnen.
# Een feest met gasten kan niet beginnen als er geen chips en geen drank is.
# Een feest moet minimaal gasten of een gastheer hebben.
# Een gastheer kan een feest geven zonder chips en gasten, maar niet zonder drank.
# Het feest kan alleen beginnen als de gastheer er is, tenzij er gasten, chips en drank zijn.

print('Case: Alleen chips is geen feest.')
# Alleen chips is geen feest
if start_the_party(False, False, False, True) == 'No Party':
    print('geslaagd')
else:
    print('Je conditie klopt niet \n')

print('\nCase: Een feest met gasten kan niet beginnen als er geen chips en geen drank is.')
# Een feest met gasten kan niet beginnen als er geen chips en geen drank is.
if start_the_party(False, True, False, False) == 'No Party':
    print('geslaagd')
else:
    print('Je conditie klopt niet')

print('\nCase: Een gastheer kan een feest geven zonder chips en gasten, maar niet zonder drank.')
# Een gastheer kan een feest geven zonder chips en gasten, maar niet zonder drank.
if start_the_party(True, False, True, False) == 'Start the Party':
    print('geslaagd')
else:
    print('Je conditie klopt niet')
if start_the_party(True, False, False, False) == 'No Party':
    print('geslaagd \n')
else:
    print('Je conditie klopt niet')

print('\nCase: Het feest kan alleen beginnen als de gastheer er is, tenzij er gasten, chips en drank zijn.')
# Het feest kan alleen beginnen als de gastheer er is, tenzij er gasten, chips en drank zijn.
if start_the_party(False, True, True, True) == 'Start the Party':
    print('geslaagd')
else:
    print('Je conditie klopt niet')
if start_the_party(True, False, False, False) == 'No Party':
    print('geslaagd')
else:
    print('Je conditie klopt niet')
if start_the_party(False, True, True, True) == 'Start the Party':
    print('geslaagd')
else:
    print('Je conditie klopt niet')