gastheer = 0
gasten = 1
drank = 1
chips = 1
if gasten or gastheer or (chips and drank):
    print('Start the Party')
else:
    print('No Party')