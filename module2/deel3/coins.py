
# naam student: Osama Mohti
# studentnummer: 99078852
# doel van het programma:
# functie van het programma:
# structuur van het programma:

teBetalenBedrag = int(float(input('Te betalen bedrag: ')) * 100)
betaaldBedrag = int(float(input('Betaald bedrag: ')) * 100)
wisselgeld = betaaldBedrag - teBetalenBedrag

if wisselgeld > 0:
    muntWaarde = 50

    while wisselgeld > 0 and muntWaarde > 0:
        aantalMunten = wisselgeld // muntWaarde

        if aantalMunten > 0:
            print('Geef maximaal', aantalMunten, 'munt(en) van', muntWaarde, 'cent terug!')
            aantalTeruggegevenMunten = int(
                input('Hoeveel munten van ' + str(muntWaarde) + ' cent heb je teruggegeven? '))
            wisselgeld -= aantalTeruggegevenMunten * muntWaarde




        if muntWaarde == 50:
            muntWaarde = 20
        elif muntWaarde == 20:
            muntWaarde = 10
        elif muntWaarde == 10:
            muntWaarde = 5
        elif muntWaarde == 5:
            muntWaarde = 2
        elif muntWaarde == 2:
            muntWaarde = 1
        else:
            muntWaarde = 0

if wisselgeld > 0:
    print('Wisselgeld niet teruggegeven: ', str(wisselgeld) + ' cent')
else:
    print('klaar')