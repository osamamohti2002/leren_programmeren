#prijzen
aantal_personen = 4
TOEGANGSTICKET = 7.45
GAMESEAT = 0.37

#hoeveelheid
aantal_minuten = 45
gameseat_per_minuten = 5
#berekening
ticket_kosten = aantal_personen * TOEGANGSTICKET
gameseat_kosten = (aantal_minuten / gameseat_per_minuten) * GAMESEAT * aantal_personen
total = ticket_kosten + gameseat_kosten

print (total.__round__(2) )