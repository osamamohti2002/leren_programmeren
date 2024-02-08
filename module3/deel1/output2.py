from data import gegevens_verzamelen
informatie = gegevens_verzamelen()

for persoon in range(len(informatie)):
    print(f"In {informatie[persoon]['city']} woont de {informatie[persoon]['leeftijd']} jarige {informatie[persoon]['naam']}")