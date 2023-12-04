boodschappenlijst = {}
while True:
    item = input("Voer het boodschappenitem in (of typ 'stop' om te eindigen): ").strip().lower()
    if item == 'stop':
        break
        
    hoeveelheid = input("Voer de hoeveelheid in: ").strip()
    if item in boodschappenlijst:
        boodschappenlijst[item] += int(hoeveelheid)
    else:
        boodschappenlijst[item] = int(hoeveelheid)

print("\nBoodschappenlijst:")
for item, hoeveelheid in boodschappenlijst.items():
    print(f"{hoeveelheid} X {item.capitalize()}")

