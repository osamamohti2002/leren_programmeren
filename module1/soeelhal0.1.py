AANTAL_PERSONEN = 4
TOEGANGSTICKET = 7.45
GAMESEAT = 0.37
AANTAL_MINUTEN = 45

ticket_kosten = AANTAL_PERSONEN * TOEGANGSTICKET
gameseat_kosten = (AANTAL_MINUTEN / 5) * GAMESEAT * AANTAL_PERSONEN

total = ticket_kosten + gameseat_kosten
print(f'een gewldige dagje met {AANTAL_PERSONEN} mensen in de speelhal met {AANTAL_MINUTEN} minuten VR kost je maar {total.__round__(1)} euro')
