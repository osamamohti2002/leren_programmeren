aantal_personen = 4
TOEGANGSTICKET = 7.45

GAMESEAT = 0.37
aantal_minuten = 45
gameseat_per_minuten = 5

ticket_kosten = aantal_personen * TOEGANGSTICKET
gameseat_kosten = (aantal_minuten / gameseat_per_minuten) * GAMESEAT * aantal_personen

total = ticket_kosten + gameseat_kosten
print(f'een gewldige dagje met {aantal_personen} mensen in de speelhal met {aantal_minuten} minuten VR kost je maar {total.__round__(1)} euro')

def som(
    
):
    a = 3
    b =5 
    return a , b

total = a + b 
print(total)