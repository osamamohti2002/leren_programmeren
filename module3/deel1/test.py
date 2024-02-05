from collections import Counter
import math, random

def is_lijst_leeg(getallen):
    return not getallen

def controleer_numeric(controlegetal):
    return str(controlegetal).isnumeric()

def bereken_gemiddelde(getallen):
    aantal = len(getallen)
    som = sum(getallen)
    return som / aantal

def vind_grootste_kleinste_eerste(getallen):
    return max(getallen), min(getallen), getallen[0]

def deel_getallen(kleinste_getal, grootste_getal, controlegetal1, controlegetal2):
    delen1 = kleinste_getal / controlegetal1
    delen2 = grootste_getal / controlegetal2
    return delen1, delen2

def vind_unieke_elementen(getallen):
    return list(set(getallen))

def bereken_verschil_en_sorteer(getallen, controlegetal1):
    aantal_unieke_elementen = len(vind_unieke_elementen(getallen))
    verschil1 = abs(aantal_unieke_elementen - controlegetal1)
    return verschil1, sorted(getallen), sorted(vind_unieke_elementen(getallen))

def tel_elementen(getallen):
    telling_elementen = Counter(getallen)
    return telling_elementen

def vind_deelbare_getallen(unieke_getallen, controlegetal):
    deelbaar = [getal for getal in unieke_getallen if getal % controlegetal == 0]
    return sorted(deelbaar)

def bevat_getallen(getallen, controlegetal1, controlegetal2):
    return controlegetal1 in getallen and controlegetal2 in getallen

def vind_posities(getallen, controlegetal1):
    return [index for index, num in enumerate(getallen) if num == controlegetal1]

def bereken_standaardafwijking(getallen, gemiddelde):
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / len(getallen)
    return math.sqrt(variantie)

def shuffle_lijst(getallen):
    random.shuffle(getallen)
    return getallen

def kies_random_getal(getallen):
    return random.choice(getallen)

def bereken_verschil(random_getal, controlegetal2):
    return abs(random_getal - controlegetal2)

def analyseer_getallenlijst(getallen, controlegetal1, controlegetal2):
    if is_lijst_leeg(getallen):
        return {"Lijst is leeg, voer getallen in.": getallen}

    if not controleer_numeric(controlegetal1):
        return {"Eerste controle getal incorrect.": controlegetal1}

    if not controleer_numeric(controlegetal2):
        return {"Tweede controle getal incorrect.": controlegetal2}

    aantal = len(getallen)
    gemiddelde = bereken_gemiddelde(getallen)
    grootste, kleinste, eerste = vind_grootste_kleinste_eerste(getallen)
    delen1, delen2 = deel_getallen(kleinste, grootste, controlegetal1, controlegetal2)

    aantal_unieke_elementen, verschil1, gesorteerde_lijst, gesorteerde_lijst_uniek = bereken_verschil_en_sorteer(getallen, controlegetal1)
    telling_elementen = tel_elementen(getallen)

    deelbaar1 = vind_deelbare_getallen(vind_unieke_elementen(getallen), controlegetal1)
    deelbaar2 = vind_deelbare_getallen(vind_unieke_elementen(getallen), controlegetal2)

    komtvoor = bevat_getallen(getallen, controlegetal1, controlegetal2)
    posities = vind_posities(getallen, controlegetal1)

    standaardafwijking = bereken_standaardafwijking(getallen, gemiddelde)
    geshufflede_lijst = shuffle_lijst(getallen)
    random_getal = kies_random_getal(geshufflede_lijst)
    verschil2 = bereken_verschil(random_getal, controlegetal2)

    resultaten = {
        "Aantal getallen": aantal,
        "Gemiddelde": gemiddelde,
        "Grootste getal": grootste,
        "Kleinste getal": kleinste,
        "Eerste getal": eerste,
        f"{kleinste} / {controlegetal1}": delen1,
        f"{grootste} / {controlegetal2}": delen2,
        "Aantal unieke elementen": aantal_unieke_elementen,
        f"Het verschil tussen {aantal_unieke_elementen} & {controlegetal1}": verschil1,
        "Gesorteerde lijst getallen": gesorteerde_lijst,
        "Gesorteerde lijst unieke getallen": gesorteerde_lijst_uniek,
        "Telling van elementen": telling_elementen,
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaar1,
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar2,
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komtvoor,
        f"{controlegetal1} komt voor op positie(s)": posities,
        "Standaardafwijking": standaardafwijking,
        "Geshufflede lijst": geshufflede_lijst,
        "Willekeurige getal uit de lijst": random_getal,
        f"Het verschil tussen {random_getal} & {controlegetal2}": verschil2,
    }

    return resultaten


# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")
