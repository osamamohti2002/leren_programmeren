# password 24 karakters lang!
# Random 2 tot 6 hoofdletters.
# Een hoofdletter mag niet op de twee middelste posities staan.
## Minimaal 8 kleine letters.
## Het wachtwoord mag niet met een kleine letter eindigen.
# 3 speciale tekens uit de volgende reeks: @ # $ % & _ ?.
## De speciale tekens mogen niet op de eerste of laatste positie staan.
# Random 4 tot 7 cijfers (0 t/m 9).
## Op de eerste 3 posities mag geen cijfer staan



import time, string, random

def test_wachtwoord(ww) -> bool:
    if len(ww) < 24:
        print('te kort')
        return False
    if not 1 < len(list(filter(lambda a: a in string.ascii_uppercase, list(ww)))) < 7:
        print('te weinig hoofdletters')
        return False
    if ww[11] in string.ascii_uppercase or ww[12] in string.ascii_uppercase:
        print('In het midden geen hoofdletters')
        return False
    if len(list(filter(lambda a: a in string.ascii_lowercase, list(ww)))) < 8:
        print('te weinig kleine letters')
        return False
    if ww[-1] in string.ascii_lowercase:
        print('Laatste pos niet juist')
        return False
    if len(list(filter(lambda a: a in '@#$%&_?', list(ww)))) != 3:
        print('te weinig specials')
        return False
    if ww[0] in '@#$%&?' or ww[-1] in '@#$%&?':
        print('special op end')
        return False
    if not 3 < len(list(filter(lambda a: a.isdigit(), list(ww)))) < 8:
        print('te weinig getallen')
        return False
    if ww[0].isdigit() or ww[1].isdigit() or ww[2].isdigit():
        print('Eerste drie karakters staat een getal')
        return False
    return True



def get_wachtwoord():
    lengte = 24
    wachtwoord = ''
    wachtwoord1 = ''
    lowercase_letters = string.ascii_lowercase
    upper_case_letters = string.ascii_uppercase
    tekens = '@#$%&_?'
    getallen = '0123456789'
    random_uppercase_letter = random.randint(2, 6)
    random_cijfers = random.randint(4, 7)
    random_lowercase_letter = lengte - random_cijfers - random_uppercase_letter - 3
    wachtwoord1 += wachtwoord.join(random.choices(getallen, k=random_cijfers))  # var aanpassen
    wachtwoord1 += wachtwoord.join(random.choices(upper_case_letters, k=random_uppercase_letter))
    wachtwoord1 += wachtwoord.join(random.choices(lowercase_letters, k=random_lowercase_letter))
    wachtwoord1 += wachtwoord.join(random.choices(tekens, k=3))
    # random.shuffle(wachtwoord_met_tekens)
    while wachtwoord1[0] in getallen or wachtwoord1[1] in getallen or wachtwoord1[2] in getallen or \
            wachtwoord1[11] in upper_case_letters or wachtwoord1[12] in upper_case_letters or wachtwoord1[
        -1] in lowercase_letters or wachtwoord1[0] in tekens or wachtwoord1[-1] in tekens:
        wachtwoord1 = ''.join(random.shuffle(list(wachtwoord1)))
    repeat = True
    if len(wachtwoord1) > 24:
        nieuw_wachtwoord = ''
        for elk_teken in wachtwoord1:
            if elk_teken not in lowercase_letters:
                nieuw_wachtwoord += tekens
        geshuffelde_wachtwoord = nieuw_wachtwoord
    elif len(wachtwoord1) < 24:
        while repeat:
            wachtwoord1 += random.choice(tekens)
    else:
        repeat = False
    return (wachtwoord1)

# for x in range(10000):
#     ww = get_wachtwoord()
#     if not test_wachtwoord(ww):
#         print(ww)
start = time.time() * 1000
for x in range(1000):
    get_wachtwoord()
end = time.time() * 1000
print(end - start)