MAX_GEWICHT = 120
MIN_GEWICHT = 90
MAX_LANGTE = 220
MIN_LANGTE = 150
GESLACHT_MAN = "man"
GESLACHT_VROUW = "vrouw"
IN_DE_WAR = "anders"
SNOR_LANGTE = 10
HAAR_LANGTE = 20
GLIMLACH_LANGTE = 10

print("---------- Sollicitatie formulier (Circusdirecteur)----------")
print("Er wordt aan u een aatal relevente vragen gesteld")
print("Gelieve die naar eer en geweten in te vullen")
print("Als blijkt dat u aan de creteria voldoet dan komt u in")
print("aanmerking voor een serius sollicitatiegesprek!")
print("Ontspan maar blijf wakker, hier komen de vragen")
print("--------------- Sucses ---------------")
print('Je kunt de vragen beantwoorden met ja / nee')

# sollicitati eisen

vrachtwagen_rijbewijs = input('Ben je in bezit van een geldige vrachtwagen rijbewijs? ')
hoed = input('Ben je in bezit van een hoge hoed? ')
gewicht = float(input('Wat is jou gewicht? '))
langte = int(input('Hoe lang ben je? '))
certificaat = input('Heeft Certificaat Overleven met gevaarlijk personeel? ')
dieren_dressuur = int(input('hoe veel jaar/jaren heb je ervaring met praktijkervaring met dieren-dressuur? '))
jongleren = int(input('hoe veel jaar ervaring heb je met jongleren? '))
acrobatiek = int(input('hoe veel jaar ervaring heb je met acrobatiek? '))
diploma_mbo = input("Bent u een bezit van een diploma MBO-4 Ondernemen? ")
ondernemer = int(input("Hoeveel ervare jaren heeft u? "))
werknemers = int(input("Met hoeveel werk nemers heeft u gewerkt? "))
geslacht = input("Wat is jou gelacht? man/vrouw/anders ")


if geslacht == "man":
    SNOR_LANGTE = int(input("Hoe breed is jouw snor in cm? "))
elif geslacht == "vrouw":
    HAAR_LANGTE = int(input("Hoe lang is uw krulhaar in cm? "))
elif geslacht == "anders":
    GLIMLACH_LANGTE = int(input("Hoe breed is uw glimlach in cm? "))


geschikte_kandidaat = (
        vrachtwagen_rijbewijs == "ja"
        and hoed == "ja"
        and gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT
        and langte >= MIN_LANGTE and langte <= MAX_LANGTE
        and certificaat == 'ja'
        and (dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3)
        and (diploma_mbo == "ja" or ondernemer >= 3 and werknemers >= 5)
        and (geslacht == "man" and SNOR_LANGTE >= 10 or geslacht == "vrouw" and HAAR_LANGTE >= 20 or geslacht == "anders" and GLIMLACH_LANGTE >= 10)
)
if geschikte_kandidaat:
    print('Gefeliciteerd! U komt in aanmerking voor deze functie.')
else:

    print('U voldoet niet aan onze strenge eisen voor de functie Circusdirecteur, Helaas het spijt ons. ')

    niet_voldane_criteria = []

    if not (vrachtwagen_rijbewijs == 'ja'):
        niet_voldane_criteria.append('Moet in bezit zijn van een vrachtwagen rijbewijs')

    if not (hoed == 'ja'):
        niet_voldane_criteria.append('Moet in bezit zijn van een hoge hoed')

    if not (gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT):
        niet_voldane_criteria.append('Gewicht moet tussen 90 kg en 120 kg liggen')

    if not (langte >= MIN_LANGTE and langte <= MAX_LANGTE):
        niet_voldane_criteria.append("Je langte moet tussen 150 and 220 cm. ")
    if not (certificaat == "ja"):
        niet_voldane_criteria.append("Je moet een certificaat hebben met overleven met gevaarlijke personeel")
    if not (jongleren > 5):
        niet_voldane_criteria.append("Je moet minimaal 5 jaar ervaring hebben")
    if not (dieren_dressuur > 4):
        niet_voldane_criteria("Je moet minimaal 4 jaar ervaring hebben.")
    if not (acrobatiek > 3):
        niet_voldane_criteria("Je moet minimaal 3 jaar ervaring hebben.")
    if not (diploma_mbo == "ja"):
        niet_voldane_criteria("Je moet een diploma mbo-4 hebben.")
    if not (ondernemer >= 3 and werknemers >= 5):
        niet_voldane_criteria.append("je moet minimaal 3 ondernemer geweest en bij minimaal 5 werknemers gewerkt")
    if not (SNOR_LANGTE >= 10):
        niet_voldane_criteria("U heeft korter snor dan wat wij vragen. ")
    if not (HAAR_LANGTE >= 20):
        niet_voldane_criteria("U heeft korter haar dan wat wij vragen. ")
    if not (anders >= 10):
        niet_voldane_criteria("U glimlach is korter dan wat wij vragen. ")

    print(niet_voldane_criteria)