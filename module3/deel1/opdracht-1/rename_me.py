def is_even(getal: int) -> bool:
    return getal % 2 == 0

def omgekeerde_zin(zin: str) -> str:
    woorden = zin.split()
    omgekeerde_woorden = woorden[::-1]
    omgekeerde_zin = ' '.join(omgekeerde_woorden)
    return omgekeerde_zin

def tel_unieke_karakters(tekst: str) -> int:
    unieke_karakters = set(tekst)
    aantal_unieke_karakters = len(unieke_karakters)
    return aantal_unieke_karakters

def gemiddelde_woordlengte(zin: str) -> float:
    woorden = zin.split()
    totale_woordlengte = 0
    for woord in woorden:
        totale_woordlengte += len(woord)
    gemiddelde_woordlengte = totale_woordlengte / len(woorden)
    return gemiddelde_woordlengte

def print_veelvouden(getal: int, aantal_keer: int = 10) -> None:
    for keer in range(1, aantal_keer + 1):
        resultaat = keer * getal
        print(f'{keer} x {getal} = {resultaat}')
