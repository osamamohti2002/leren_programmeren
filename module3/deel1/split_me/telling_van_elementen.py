def telling_van_elementen(getallen):
    telling_elementen = {}
    for getal in getallen:
        if getal in telling_elementen:
            telling_elementen[getal] += 1
        else:
            telling_elementen[getal] = 1
    return telling_elementen

# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 16, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
telling_elementen = telling_van_elementen(getallenlijst)
print("Telling van elementen:")
for getal, aantal_keer in telling_elementen.items():
    print(f"{getal}: {aantal_keer}")
