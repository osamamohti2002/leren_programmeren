# voor naam : Osama
# acher naam : Mohti
# opdracht : pizza Calculator


#pizza's prijzen
PIZZA_PRIJZEN = {'PIZZA_GROOT': 14.99 , 'PIZZA_MEDUIM' : 11.99 , 'PIZZA_KLEIN' : 8.99 }
print(f'dit zijn onze prijzen en pizza maten {PIZZA_PRIJZEN}')



# aantal pizza's die de gebruiker moet kiezen
aantal_pizza_groot = int(input("Hoeveel grote pizza's wilt u hebben?"))
aantal_pizza_meduim = int(input("Hoeveel medium pizza's wilt u hebben?"))
aantal_pizza_klein = int(input("Hoeveel kleine pizza's wilt u hebben?"))

#berkening

kosten_pizza_groot = aantal_pizza_groot * PIZZA_PRIJZEN['PIZZA_GROOT']
kosten_pizza_medium = aantal_pizza_meduim * PIZZA_PRIJZEN['PIZZA_MEDUIM']
kosten_pizza_klein = aantal_pizza_klein * PIZZA_PRIJZEN['PIZZA_KLEIN']

totaal = kosten_pizza_groot + kosten_pizza_medium + kosten_pizza_klein
#de uit komst (bonnetje)
print('    -' * 30)
print('\n uw besteling')
print(f"|   Aantal grote pizza's = {aantal_pizza_groot}    x  € {kosten_pizza_groot}  ")
print(f"|   Aantal meduim pizza's = {aantal_pizza_meduim}    x  € {kosten_pizza_medium}")
print(f"|   Aantal kleine pizza's = {aantal_pizza_klein}    x  € {kosten_pizza_klein}")
print(f"|   de totale prijs = € {totaal.__round__(2) }")
print('     -' * 30)

