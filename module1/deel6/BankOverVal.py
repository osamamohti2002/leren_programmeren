def introductie():
    print('welkom bij het bank overval spel')
    print('De missie is dat je de kluis vindt daarna van de politie te ontsnappen')


def kluis_keuze():
    while True:
        try:
            kluis = input('Je bent nu in de bank en je moet een kant kiezen om de kluis te vinden ga je (Links of Rechts)')
            if kluis == 'rechts':
                print('Je bent opgepakt door de bewakers. Je hebt verloren')
                return False
            elif kluis == 'links':
                print('Goede keuze! je hebt de kluis bereikt.')
                return True
        except ValueError:
            print('ongeldige invoer')


def auto_ontsnapping():
    print('Met de auto heb je 2 opties')
    while True:
        try:
            auto_optie = input('Wil je via de snelweg of via de stad ontsnappen')
            if auto_optie == 'snelweg':
                print('De politie heeft de snelweg geblokkeerd. Je bent gepakt en verloren!')
                return False
            elif auto_optie == 'stad':
                print('je hebt geluk het is erg druk in de stad je hebt kunnen ontsnappen')
                return True
        except ValueError:
            print('ongeldige invoer')


def scooter_ontsnapping():
    print('Met de scooter heb je 2 opties')
    while True:
        try:
            scooter_optie = input('Kies of je door blijft rijden of door smalle zijstraatjes gaat: (doorrijden of zijstraatjes)')
            if scooter_optie == 'zijstraatjes':
                print('Je ontsnapt door de smalle zijstraatjes. Goed gedaan!')
                return True
            elif scooter_optie == 'doorrijden':
                print('De politie heeft je ingehaald. Je bent gepakt en verloren!')
                return False
        except ValueError:
            print('ongeldige invoer')


def main():
    introductie()
    if kluis_keuze():
        while True:
            try:
                ontsnappingskeuze = input("Hoe wil je ontsnappen? Met de auto of met de scooter: ")
                if ontsnappingskeuze == "auto":
                    auto_ontsnapping()
                elif ontsnappingskeuze == "scooter":
                    scooter_ontsnapping()
            except ValueError:
                print('ongeldige invoer')


if __name__ == '__main__':
    main()

