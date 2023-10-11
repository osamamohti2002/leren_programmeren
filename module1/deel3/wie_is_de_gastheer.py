MIJN_NAAM = 'osama'
SLB_NAAM = "jouke"

gastheer = input('wie is de gastheer')
gasten = False
drank = True
chips = False
# print((gasten and chips and drank) or (gastheer > "" and drank))
if (gastheer == MIJN_NAAM) or ((gasten and chips and drank) or (gastheer and drank)) and gastheer != SLB_NAAM:
    print('Start the Party')
else:
    print('geen feest')