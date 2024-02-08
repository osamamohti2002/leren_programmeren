def filter_deelbaar(getallen, controlegetal):
    lijst = []
    posities = []
    for index, getal in enumerate(getallen):
        if getal % controlegetal == 0:
            lijst.append(getal)
        if getal == controlegetal:
            posities.append(index)


    komtvoor_controlegetal = len(posities) > 0

    return sorted(lijst), komtvoor_controlegetal, posities


getallenlijst = [16, 2, 5, 8, 12, 3, 40, 9, 16, 5, 8, 64, 33]
controlegetal1 = 1
deelbaar, komtvoor, posities = filter_deelbaar(getallenlijst, controlegetal1)
print(f"Getallen deelbaar door {controlegetal1} (op volgorde): {deelbaar}")
print(f"{controlegetal1} & {controlegetal1} komt wel voor in de lijst {komtvoor}")
print(f"{controlegetal1} komt voor op positie(s){posities} ")



controlegetal2 = 3
deelbaar, komtvoor, posities = filter_deelbaar(getallenlijst, controlegetal2)
print(f"Getallen deelbaar door {controlegetal2} (op volgorde): {deelbaar}")
print(f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst {komtvoor}")
print(f"{controlegetal2} komt voor op positie(s) {posities} ")