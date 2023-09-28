aantal_personen = 3
toegangsticket = 7.45
gameseat = 0.37
aantal_minuten = 45

ticket_kosten = aantal_personen * toegangsticket
gameseat_kosten = gameseat * aantal_minuten * aantal_personen

total = ticket_kosten + gameseat_kosten
print(total)
