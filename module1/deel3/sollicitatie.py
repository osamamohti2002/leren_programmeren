MAX_GEWICHT = 120
MIN_GEWICHT = 90
MAX_LANGTE = 220
MIN_langte = 150


print('Je kunt de vragen beantwoorden met ja / nee')
#sollicitati eisen
vrachtwagen_rijbewijs = input('Ben je in bezit van een geldige vrachtwagen rijbewijs')
hoed = input('Ben je in bezit van een hoge hoed?')
gewicht = float(input('Wat is jou gewicht?'))
langte = int(input('Hoe lang ben je?'))
certificaat = input('Heeft Certificaat Overleven met gevaarlijk personeel')
dieren_dressuur = int(input('hoe veel jaar/jaren heb je ervaring met praktijkervaring met dieren-dressuur'))
jongleren = int(input('hoe veel jaar ervaring heb je met jongleren'))
acrobatiek = int(input('hoe veel jaar ervaring heb je met acrobatiek'))


if (vrachtwagen_rijbewijs == 'ja'
    and hoed == 'ja'
    and gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT
    and langte >= MIN_langte and langte <= MAX_LANGTE
    and certificaat == 'ja'
    and dieren_dressuur >= 4

):
    print('gefeliciteerd')
elif (
vrachtwagen_rijbewijs == 'ja'
    and hoed == 'ja'
    and gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT
    and langte >= MIN_langte and langte <= MAX_LANGTE
    and certificaat == 'ja'
    and jongleren >= 5 or acrobatiek >= 3
):
    print('gefeliciteerd 1')

else:
    print('donderop')