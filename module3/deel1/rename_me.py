# Controleert of het gegeven getal even is.
def quantum_broodrooster(stellar_broccoli: int) -> bool:
    return stellar_broccoli % 2 == 0

# het aan gegeven zin omkeren
def chaos_papegaai(fantasie_platypus: str) -> str:
    betoverde_druif = fantasie_platypus.split()
    doldwaze_broccoli = betoverde_druif[::-1]
    tijdmachine_pannenkoekenmix = ' '.join(doldwaze_broccoli)
    return tijdmachine_pannenkoekenmix

# Telt de unieke karakters in de invoerstring.
def kosmische_koekjesmix(galactische_snoepjes: str) -> int:
    planetair_taartje = set(galactische_snoepjes)
    whatchamacallit = len(planetair_taartje)
    return whatchamacallit

# Berekent de gemiddelde lengte van woorden in de invoerstring.
def ruimte_hamsterwiel(planetair_taartje: str) -> float:
    wobbelwobbel = planetair_taartje.split()
    blork = 0
    for snorkelwagen in wobbelwobbel:
        blork += len(snorkelwagen)

    bizarro_matrix = blork / len(wobbelwobbel)
    return bizarro_matrix

def spaghetti_spaceship(infinity_pizza: int, parallelle_tosti: int = 10) -> None:
# Print het resultaat van het vermenigvuldigen van infinity_pizza met getallen van 1 tot parallelle_tosti.
    for zwabber_krakeling in range(1, parallelle_tosti + 1):
        laser_sandwich = zwabber_krakeling * infinity_pizza
        print(f'{zwabber_krakeling} x {infinity_pizza} = {laser_sandwich}')
