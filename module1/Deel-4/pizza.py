# voornaam = Lithe
# achternaam = Jnaid
# opdarcht = Pizza calculator

def vraag_aantal(pizza_soort):
    while True:
        print("uitgevoerd")
        try:
            aantal = float(input(f"Hoeveel {pizza_soort} pizza's wilt u bestellen? "))
            if aantal < 0:
                print("Aantal pizza's kan niet negatief zijn. Probeer opnieuw.")
            else:
                return aantal
        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in.")
            
# Prijzen voor Pizza soorten
PIZZA_PRIJZEN = {
    "groot" : 8.50,
    "medium" : 10.50,
    "klein" : 12.50
}

# Hier is de invoer van de gebruiker voor pizza soorten
aantal_groot = vraag_aantal("groot ") 
aantal_medium = vraag_aantal("medium")
aantal_klein = vraag_aantal("klein")


# Berekeningen van pizza prijzen 
kosten_groot = aantal_groot * PIZZA_PRIJZEN["groot"]
kosten_medium = aantal_medium * PIZZA_PRIJZEN["medium"]
kosten_klein = aantal_klein * PIZZA_PRIJZEN["klein"]
totaal_prijs = kosten_groot + kosten_medium + kosten_klein

# dat is de bonnetje van de bestelde pizza van de gebruiker
print("======= UW Bestelling=======")
print(f"{aantal_groot} x groot pizza's: € {kosten_groot}")
print(f"{aantal_medium} x medium pizza': € {kosten_medium}")
print(f"{aantal_klein} x klein pizza's: € {kosten_klein}")
print("============================")
print(f"Totaal prijs: € {totaal_prijs}")




