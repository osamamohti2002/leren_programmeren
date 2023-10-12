MIJN_NAAM = 'osama'
SLB_NAAM = "jouke"

gastheer = input('wie is de gastheer')
gasten = int(input('hoeveel gasten'))
drank = False
chips = False
# print((gasten and chips and drank) or (gastheer > "" and drank))
if (gastheer == MIJN_NAAM) or ((gasten and chips and drank) or (gastheer and drank)) and gastheer  != SLB_NAAM or gastheer or 20 >= gasten >= 4:
    print('Start the Party')
else:
    print('geen feest')

