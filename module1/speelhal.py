AANTAL_PERSONEN = 4
TOEGANGSTICKET = 7.45
GAMESEAT = 0.37
AANTAL_MINUTEN = 45

ticket_kosten = AANTAL_PERSONEN * TOEGANGSTICKET
gameseat_kosten = (AANTAL_MINUTEN / 5) * GAMESEAT * AANTAL_PERSONEN

total = ticket_kosten + gameseat_kosten
print(total.__round__(1))