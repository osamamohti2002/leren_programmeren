from data import gegevens_verzamelen
informatie = gegevens_verzamelen()

for persoon in range(len(informatie)):
    print(f"{informatie[persoon]['naam']}, die in {informatie[persoon]['city']} woont is {informatie[persoon]['leeftijd']} jaar oud")