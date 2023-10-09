gastheer =1
gasten = 0
drank = 0
chips = 0
# print((gasten and chips and drank) or (gastheer > "" and drank))
if ((gasten and chips and drank) or (gastheer and drank)):
    print('Start the Party')
else:
    print('geen feest')