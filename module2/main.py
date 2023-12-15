# totaal = 0
#
# for x in range(1,11):
#     totaal +=x
# print(totaal)

# resultaat = sum(range(11, 21, 2))
# print(resultaat)

# total = 0
# for i in range(11, 21, 2):
#     total += i
# print(total)
# artiesten = ['DUA LIPA', 'OFENBACH', 'INIGO QUINTERO', 'OFENBACH', 'INIGO QUINTERO', 'INIGO QUINTERO', 'OFENBACH',
#              'OFENBACH', 'DUA LIPA', 'DUA LIPA', 'INIGO QUINTERO', 'DUA LIPA', 'DUA LIPA', 'OFENBACH', 'INIGO QUINTERO', 'OFENBACH',
#              'INIGO QUINTERO', 'INIGO QUINTERO', 'OFENBACH', 'OFENBACH', 'DUA LIPA', 'DUA LIPA', 'INIGO QUINTERO', 'DUA LIPA', 'osama' , 'osama', 'Lithe' , 'Osker']
#
# aantal_artiesten = {}
#
# for naam in artiesten:
#     if naam not in aantal_artiesten:
#         aantal_artiesten[naam] = 1
#     else:
#         aantal_artiesten[naam] += 1
# for naam , teller in aantal_artiesten.items():
#     print(f'{naam}  {teller}')

# def voeg_woord_lengtes_toe(input_string):
#     woorden = input_string.split()
#     resultaat = [f"{woord} {len(woord)}" for woord in woorden]
#     return resultaat

# Voorbeeldgebruik:
# input_str1 = "appel banaan"
# output1 = voeg_woord_lengtes_toe(input_str1)
# print(output1)
#
# input_str2 = "jij zult winnen"
# output2 = voeg_woord_lengtes_toe(input_str2)
# print(output2)
#

# def add_length(zin):
#     woorden = zin.split
#     lijst = []
#     for woord in woorden:
#         element = f'{woord} {len(woord)}'
#         lijst.append(element)
#     return lijst
#
# zin = "jij zult winnen"
# output2 = add_length(zin)
# print(output2)

def add_length(zin):
    woorden = zin.split()
    lijst = []
    for woord in woorden:
        element = f"{woord} {len(woord)}"
        lijst.append(element)

    return lijst

# Voorbeeldgebruik:
input_str1 = "appel banaan"
output1 = add_length(input_str1)
print(output1)

input_str2 = "jij zult winnen"
output2 = add_length(input_str2)
print(output2)
