
aantal_lijsten = int(input("Voer het aantal lijstjes in: "))
main_lijst = []
start = 1
for lijst in range(1, aantal_lijsten + 1):
    lengte_lijst = int(input(f"Voer de lengte in voor lijst {lijst}: "))
    lijstje = list(range(start, lengte_lijst * lijst + 1, lijst))
    start += 1
    main_lijst.append(lijstje)
    print(f"Lijst {lijst}: {lijstje}")

print(main_lijst)