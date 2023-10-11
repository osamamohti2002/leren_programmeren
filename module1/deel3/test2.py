MAX_GEWICHT = 120
MIN_GEWICHT = 90
MAX_LANGTE = 220
MIN_LANGTE = 150

ONDERNEMER = 3
PERSONEEL = 5
DIPLOMA = 4
SNOR_BREDTE = 10
KRULHAAR_LANGTE = 20
GELIMLACH = 10


print('+       sollicitatieformulier "Circusdirecteur"         +')
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print('er wordt u een antal relevante vragen gesteld...')
print('Gelive die naar eer en geweten in te vullen')
print('Als blijkt dat u aan de criteria voldoet dan komt u in aanmerking voor een serieus sollicitatiegesprek!')
print('Ontspan maar blijf wakker , hier komen de vragen')
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


#sollicitati eisen
geslacht = input('wat is geslacht?')
gewicht = float(input('Wat is jou gewicht?'))
langte = int(input('Hoe lang ben je?'))
vrachtwagen_rijbewijs = input('Ben je in bezit van een geldige vrachtwagen rijbewijs')
hoed = input('Ben je in bezit van een hoge hoed?')
certificaat = input('Heeft Certificaat Overleven met gevaarlijk personeel')
dieren_dressuur = int(input('hoe veel jaar/jaren heb je ervaring met praktijkervaring met dieren-dressuur'))
jongleren = int(input('hoe veel jaar ervaring heb je met jongleren'))
acrobatiek = int(input('hoe veel jaar ervaring heb je met acrobatiek'))
diploma = int(input('wat is je diploma niveau?'))


if (vrachtwagen_rijbewijs == 'ja'
    and hoed == 'ja'
    and gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT
    and langte >= MIN_LANGTE and langte <= MAX_LANGTE
    and certificaat == 'ja'
    and (dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3)
    and geslacht == GESLACHT_MAN

) and ( diploma == DIPLOMA or ondernemer
):
    if diploma < 4 :
        ondernemer = int(input('hoelang ben je ondernemer al?'))
        personeel = int(input('hoe veel medeweker heb je in dienst'))
        if ondernemer == ONDERNEMER and personeel == PERSONEEL:
            print('Gefeliciteerd je komt in aanmerking voor deze functie ')
    snor = input('Heeft u een snor? ')
    snor_breedte = int(input('Hoe breed is uw snor in cm? '))
    if snor == 'ja' and snor_breedte == SNOR_BREDTE:
        print('Gefeliciteerd je komt in aanmerking voor deze functie ')
    else:
        print(f'je voldoet niet aan onze eisen ')
elif geslacht == GESLACHT_VROUW:
    krulhaar = input('heb je krulhaar')
    krulhaar_langte = int(input('hoe lang is je krulhaar'))
    if krulhaar == 'ja' and krulhaar_langte == KRULHAAR_LANGTE:
        print('Gefeliciteerd je komt in aanmerking voor deze functie ')
    else:
        print(f'je voldoet niet aan onze eisen ')
elif geslacht == IN_DE_WAR:
    glimlach = int(input('hoe breed is je glicmlach'))
    if glimlach == GELIMLACH:
        print('Gefeliciteerd je komt in aanmerking voor deze functie ')
    else:
        print(f'je voldoet niet aan onze eisen ')




else:
    print('u voldoet niet aan onze strenge eizen voor de functie Circusdirecteur, Helaas het spijt ons ')