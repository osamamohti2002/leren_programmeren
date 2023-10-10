MAX_GEWICHT = 120
MIN_GEWICHT = 90
MAX_LANGTE = 220
MIN_LANGTE = 150

print('+       sollicitatieformulier "Circusdirecteur"         +')
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print('er wordt u een antal relevante vragen gesteld...')
print('Gelive die naar eer en geweten in te vullen')
print('Als blijkt dat u aan de criteria voldoet dan komt u in aanmerking voor een serieus sollicitatiegesprek!')
print('Ontspan maar blijf wakker , hier komen de vragen')
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


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
    and langte >= MIN_LANGTE and langte <= MAX_LANGTE
    and certificaat == 'ja'
    and dieren_dressuur >= 4
):
    print('Gefeliciteerd je komt in aanmerking voor deze functie ')
elif (
        vrachtwagen_rijbewijs == 'ja'
        and hoed == 'ja'
        and gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT
        and langte >= MIN_LANGTE and langte <= MAX_LANGTE
        and certificaat == 'ja'
        and jongleren >= 5 or acrobatiek >= 3
):
    print('Gefeliciteerd je komt in aanmerking voor deze functie')

else:
    print('u voldoet niet aan onze strenge eizen voor de functie Circusdirecteur, Helaas het spijt ons ')