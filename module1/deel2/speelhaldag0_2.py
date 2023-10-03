# aantal_personen = int(4)
# aantal_minuten = int(45)
# gameseat_per_minuten =int (5)
#
# ticket_kosten = aantal_personen * TOEGANGSTICKET
# gameseat_kosten = (aantal_minuten / gameseat_per_minuten) * GAMESEAT * aantal_personen
#
# total = ticket_kosten + gameseat_kosten
# print(f'een gewldige dagje met {aantal_personen} mensen in de speelhal met {aantal_minuten} minuten VR kost je maar {total.__round__(2)} euro')


#prijzen
toegangsticket = float(input('hoeveel kost een toegangsticket?'))
gameseat = float(input('hoeveel kost het per 5 minuten?'))


#aantalen
aantal_personen = int(input('hoeveel mensen'))
aantal_minuten = int(input('hoeveel minuten'))
gameseat_per_minuten = 5

#berekening
ticket_kosten = aantal_personen * toegangsticket
gameseat_kosten = (aantal_minuten / gameseat_per_minuten) * gameseat * aantal_personen

total = ticket_kosten + gameseat_kosten
print(f'een gewldige dagje met {aantal_personen} mensen in de speelhal met {aantal_minuten} minuten VR kost je maar {total} euro')
