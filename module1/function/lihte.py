import random

def intro():
    print("welkom in het spel van Layla en de wolf! ")
    print("Layla moet van haar moeder eten brengen naar haar zieke oma. ")
    print("Je moet slimme keuze maken om het eten bij haar oma veilig komt.")
 
def twee_routes():
    print("Lyla heeft de eten gerekgen en nu gaat zij vertrekken, haar moedere heeft ze twee routes verteld waar bij een route het veilig route is ")
    choice = input("kies je voor route (1) of route (2)? ")
    if choice == '1':
        print('Goedgedaan Layla is veilig bij haar oma terecht gekomen!')
    elif choice == '2':
        print("Lyla gaat via het bos")
        bos()
 
def bos():
    print("Een vlinder heeft Layla gewaarschuwd om niet alleen via het bos te loppen")
    choice = input("veder gaan (1) of luisteren naar het vlinder en terug gaan (2)? ")
    if choice == "1":
        print("Lyla neemt toch wel het risico om verder te gaan")
        wolf()
    elif choice == '2':
        print("Goedgedaan je hebt naar het vlindere geluistered en Layla is veilig naar haar oma gekomen.! ")
 
def wolf():
    print("Layla loopt veder is het donkere bos met angst gevoel en opeens hoort een geluid achter het boom")
    choice = input("negeren en doorlopen (1) of  Kijken wat het is (2)? ")
    if choice == '1':
        print("Helaas je hebt verloren! de wolf heeft Layla achter gevolgd en heeft Layla en haar oma opgegeten ")
    elif choice == '2':
        print("Er is een Wolf acher het boom!")
        einde_verhaal()
 
def einde_verhaal():
    choice = input("er is een wolf!  wil je vrienden zijn met het wolf? (1) of wegrennen (2)? ")
    if choice == '1':
        print("Helaas de wolf heeft Layla opgegeten! ")
    elif choice == '2':
        print("Helaas toch heeft de wolf Layla kunnen pakken en eten ")



intro()
twee_routes()
