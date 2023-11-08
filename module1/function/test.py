kluis = input('Je bent nu in de bank en je moet een kant kiezen om de kluis te vinden ga je (Links of Rechts)')
while True:
    if kluis == 'links':
        ontsnappingskeuze = input("Hoe wil je ontsnappen? Met de auto of met de scooter: ")
        if ontsnappingskeuze == 'auto':
            auto_optie = input('Wil je via de snelweg of via de stad ontsnappen')
            if auto_optie == 'snelweg':
                print('De politie heeft de snelweg geblokkeerd. Je bent gepakt en verloren!')
                break
            elif auto_optie == 'stad':
                print('je hebt geluk het is erg druk in de stad je hebt kunnen ontsnappen')
                break
            else:
                print('ongeldige invoer')
        elif ontsnappingskeuze == 'scooter':
            scooter_optie = input('Kies of je door blijft rijden of door smalle zijstraatjes gaat: (doorrijden of zijstraatjes)')
            if scooter_optie == 'doorrijden':
                print('De politie heeft je ingehaald. Je bent gepakt en verloren!')
                break
            elif scooter_optie == 'zijstraatjes':
                print('Je ontsnapt door de smalle zijstraatjes. Goed gedaan!')
                break
            else:
                print('ongeldige invoer')
        else:
            print('ongeldige invoer')
    elif kluis == 'rechts':
        print('Je bent opgepakt door de bewakers. Je hebt verloren')
        break
    else:
        print('ongeldige invoer')
        break





        


            
        