import random

def get_random_compliment(naam:str) -> str:
    MIJN_COMPLIMENTEN = ('je bent geweldig', 'je doet het super', 'Niemand zoals jij')
    compiment = random.choice(MIJN_COMPLIMENTEN)
    return f'{compiment} {naam}'

print(get_random_compliment('osama'))