def stel_vraag(vraag, ok_antwoorden):
    while True:
        antwoord = input(vraag)
        if antwoord in ok_antwoorden:
            return antwoord
        else:
            print('ongeldige invoer')

def kluis_keuze():
    return stel_vraag('Je bent nu in de bank en je moet een kant kiezen om de kluis te vinden ga je (Links of Rechts)', ['rechts', 'links' ])

def rechts_keuze():
    return stel_vraag('je bent in de gang wil je door lopen of naar links', ['links', 'doorlopen'])

def doorlopen():
    return stel_vraag('je bent bij de einde van de gang wil links of rechts', ['links' , 'rechts'] )

def ontsnappings_vraag():
    return stel_vraag("Hoe wil je ontsnappen? Met de auto of met de scooter of via de dak: ", ['auto', 'scooter', 'dak'])


def auto_vraag():
    return stel_vraag('wil je via de snelweg of door de stad ontsnappen', ['snelweg', 'stad'])



def scooter_vraag():
    return stel_vraag('wil je doorrijden of door de zijstraatjes ontsnappen', ['doorrijden', 'zijstraatjes'])


def dak_vraag():
    return stel_vraag('politie is achter jou en benden is een zwembad wil je uit het dak springen of je zelf overgeven', ['springen', 'overgeven'])


def ontsnappen():
    return stel_vraag('je bent nu in de zwembad en je wilt snel ontsnappen wil je een auto of een scooter stellen',  ['auto', 'scooter'])


print('welkom bij het bank overval spel')
print('De missie is dat je de kluis vindt daarna van de politie te ontsnappen')

ontsnappings_keuze = ''
kluis = kluis_keuze()
if kluis == 'links':
    print('Goede keuze! je hebt de kluis bereikt.')
    ontsnappings_keuze = ontsnappings_vraag()
    if ontsnappings_keuze == 'dak':
        dak_ontsnapping = dak_vraag()
        if dak_ontsnapping == 'springen':
            ontsnappings_keuze = ontsnappen()
        elif dak_ontsnapping == 'overgeven':
            print('je hebt je zelf overgegeven en je hebt verloren')

elif kluis == 'rechts':
    keuze_rechts = rechts_keuze()
    if keuze_rechts == 'doorlopen':
        eind_gang = doorlopen()
        if eind_gang == 'rechts':
            print('er zijn bewakers je bent opgepakt')
        elif eind_gang == 'links':
            print('Goede keuze! je hebt de kluis bereikt.')
            ontsnappings_keuze = ontsnappings_vraag()

    elif keuze_rechts == 'links':
        print('Goede keuze! je hebt de kluis bereikt.')
        ontsnappings_keuze = ontsnappings_vraag()

if ontsnappings_keuze == 'auto':
    auto_ontsnapping = auto_vraag()
    if auto_ontsnapping == 'snelweg':
        print('De politie heeft de snelweg geblokkeerd. Je bent gepakt en verloren!')
    elif auto_ontsnapping == 'stad':
        print('je hebt geluk het is erg druk in de stad je hebt kunnen ontsnappen')
elif ontsnappings_keuze == 'scooter':
    scooter_ontsnapping = scooter_vraag()
    if scooter_ontsnapping == 'doorrijden':
        print('De politie heeft je ingehaald. Je bent gepakt en verloren!')
    elif scooter_ontsnapping == 'zijstraatjes':
        print('Je ontsnapt door de smalle zijstraatjes. Goed gedaan!')
# elif ontsnappings_keuze == 'dak':
#     dak_ontsnapping = dak_vraag()
#     if dak_ontsnapping == 'springen':
#         ontsnappings_keuze = ontsnappen()
#
#     elif dak_ontsnapping == 'overgeven':
#         print('je hebt je zelf overgegeven en je hebt verloren')

