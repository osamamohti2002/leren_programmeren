import math


def bereken_variantie_en_standaardafwijking(getallen):
    aantal = len(getallen)
    gemiddelde = sum(getallen) / aantal

    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)

    return variantie, standaardafwijking


# Example usage:

getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
variantie, standaardafwijking = bereken_variantie_en_standaardafwijking(getallenlijst)

print(f"Variantie: {variantie}")
print(f"Standaardafwijking: {standaardafwijking}")
