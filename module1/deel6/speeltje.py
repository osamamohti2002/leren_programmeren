def stel_vraag(vraag, ok_antwoorden):
    while True:
        antwoord = input(vraag)
        if antwoord in ok_antwoorden:
            return antwoord
        else:
            print('ongeldige invoer')


def kluis_keuze():
    return stel_vraag('Je bent nu in de bank en je moet een kant kiezen om de kluis te vinden. Ga je links of rechts? ',
                      ['rechts', 'links'])


def rechts_keuze():
    return stel_vraag('Je bent in de gang. Wil je doorlopen of naar links?', ['doorlopen', 'links'])


def doorlopen():
    return stel_vraag('Je bent bij het einde van de gang. Wil je naar links of rechts?', ['links', 'rechts'])


def ontsnappings_vraag():
    return stel_vraag('Hoe wil je ontsnappen? Met de auto, met de scooter, of via het dak? ',
                      ['auto', 'scooter', 'dak'])


def auto_vraag():
    return stel_vraag('Wil je via de snelweg of door de stad ontsnappen?', ['snelweg', 'stad'])


def scooter_vraag():
    return stel_vraag('Wil je doorrijden of door de zijstraatjes ontsnappen?', ['doorrijden', 'zijstraatjes'])


def dak_vraag():
    return stel_vraag(
        'De politie zit achter je en onder je is een zwembad. Wil je uit het dak springen of jezelf overgeven?',
        ['springen', 'opgeven'])


def ontsnappen():
    return stel_vraag('Je bent nu in het zwembad en je wilt snel ontsnappen. Wil je een auto of een scooter stelen?',
                      ['auto', 'scooter'])


print('Welkom bij het bankovervalspel')
print('De missie is dat je de kluis vindt en daarna ontsnapt aan de politie.')
scooter = ""
ontsnappings_keuze = ''
kluis = kluis_keuze()
if kluis == 'rechts':
    eind_gang = doorlopen()
    if eind_gang == 'rechts':
        print('Er zijn bewakers, je bent opgepakt.')
    elif eind_gang == 'links':
        print('Goede keuze! Je hebt de kluis bereikt.')
        ontsnappings_keuze = ontsnappings_vraag()
        if ontsnappings_keuze == 'auto':
            auto_vraag_result = auto_vraag()
            if auto_vraag_result == 'snelweg':
                print('De politie heeft de snelweg geblokkeerd. Je bent gepakt en verloren!')
            elif auto_vraag_result == 'stad':
                print('Je hebt geluk, het is erg druk in de stad. Je bent ontsnapt!')
        elif ontsnappings_keuze == 'scooter':
            scooter_vraag_result = scooter_vraag()
            if scooter_vraag_result == 'doorrijden':
                print('De politie heeft je ingehaald. Je bent gepakt en verloren!')
            elif scooter_vraag_result == 'zijstraatjes':
                print('Je ontsnapt door de smalle zijstraatjes. Goed gedaan!')
        elif ontsnappings_keuze == 'dak':
            dak_vraag_result = dak_vraag()
            if dak_vraag_result == 'opgeven':
                print('Je hebt jezelf overgegeven.')
            elif dak_vraag_result == 'springen':
                ontsnappings_keuze = ontsnappen()
                if ontsnappings_keuze == 'auto':
                    auto_vraag_result = auto_vraag()
                    if auto_vraag_result == 'snelweg':
                        print('De politie heeft de snelweg geblokkeerd. Je bent gepakt en verloren!')
                    elif auto_vraag_result == 'stad':
                        print('Je hebt geluk, het is erg druk in de stad. Je bent ontsnapt!')
                elif ontsnappings_keuze == 'scooter':
                    scooter_vraag_result = scooter_vraag()
                    if scooter_vraag_result == 'doorrijden':
                        print('De politie heeft je ingehaald. Je bent gepakt en verloren!')
                    elif scooter_vraag_result == 'zijstraatjes':
                        print('Je ontsnapt door de smalle zijstraatjes. Goed gedaan!')
elif kluis == 'links':
    print('Goede keuze! Je hebt de kluis bereikt.')
    ontsnappings_keuze = ontsnappings_vraag()
    if ontsnappings_keuze == 'auto':
        auto_vraag_result = auto_vraag()
        if auto_vraag_result == 'snelweg':
            print('De politie heeft de snelweg geblokkeerd. Je bent gepakt en verloren!')
        elif auto_vraag_result == 'stad':
            print('Je hebt geluk, het is erg druk in de stad. Je bent ontsnapt!')
    elif ontsnappings_keuze == 'scooter':
        scooter_vraag_result = scooter_vraag()
        if scooter_vraag_result == 'doorrijden':
            print('De politie heeft je ingehaald. Je bent gepakt en verloren!')
        elif scooter_vraag_result == 'zijstraatjes':
            print('Je ontsnapt door de smalle zijstraatjes. Goed gedaan!')
    elif ontsnappings_keuze == 'dak':
        dak_vraag_result = dak_vraag()
        if dak_vraag_result == 'opgeven':
            print('Je hebt jezelf overgegeven.')
        elif dak_vraag_result == 'springen':
            ontsnappings_keuze = ontsnappen()
            if ontsnappings_keuze == 'auto':
                auto_vraag_result = auto_vraag()
                if auto_vraag_result == 'snelweg':
                    print('De politie heeft de snelweg geblokkeerd. Je bent gepakt en verloren!')
                elif auto_vraag_result == 'stad':
                    print('Je hebt geluk, het is erg druk in de stad. Je bent ontsnapt!')

            elif ontsnappings_keuze == 'scooter':
                scooter_vraag_result = scooter_vraag()
                if scooter_vraag_result == 'doorrijden':
                    print('De politie heeft je ingehaald. Je bent gepakt en verloren!')
                elif scooter_vraag_result == 'zijstraatjes':
                    print('Je ontsnapt door de smalle zijstraatjes. Goed gedaan!')
