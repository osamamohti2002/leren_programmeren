import math
import string

UNIT_PIECES = 'piece'
UNIT_SPOONS = 'spoon'
UNIT_TEASPOONS = 'teaspoon'
UNIT_CUPS = 'cup'

TXT_PIECES = '|'
TXT_SPOONS = 'eetlepel|eetlepels'
TXT_TEASPOONS = 'theelepel|theelepels'
TXT_CUPS = 'kopje|kopjes'

# failsafe input of a number of persons
def input_nr_persons(prompt: str) -> int:
  while True:
    try:
      nr_persons = int(input(prompt))
      if nr_persons > 0: 
        return nr_persons
      print('getal moet groter zijn dan 0')
    except:
      print('voer een geldig geheel getal in!')


def round_piece(amount: float) -> int:
  return math.ceil(amount)

# returns amount rounded to the closest decimals: .00 or .25 or .50 or 0.75 unless amount >= 10
def round_quarter(amount: float) -> float:
    if amount > 10:
        return round(amount)    
    else:
        rounded_amount = round(amount * 4) / 4
        if rounded_amount < 0.25:
            return 0.25
        return rounded_amount


# returns single or plural description of a string 'single desciption|plural description' 
# depending on amount
def str_single_plural(amount: float, txt: str) -> str:
    splits_txt = txt.split('|')
    if amount == 1:
        return splits_txt[0]
    else:
        return splits_txt[-1]


# returns description of single or plural units
def str_units(amount: float, unit: str) -> str:
    if unit == UNIT_SPOONS:
        return str_single_plural(amount, TXT_SPOONS)
    elif unit == UNIT_TEASPOONS:
        return str_single_plural(amount, TXT_TEASPOONS)
    elif unit == UNIT_CUPS:
        return str_single_plural(amount, TXT_CUPS)
    elif unit == UNIT_PIECES:
        return str_single_plural(amount, TXT_PIECES)
    else:
        return f"{amount} {unit}"



# returns amount in string with 1/4 or 1/2 or 3/4
TXT_FRACTIONS = ('','¼','½','¾')
def str_amount_fraction(amount: float) -> str:
    amount = round_quarter(amount)
    ints = int(amount)
    quarter = int((amount - ints) / 0.25)
    str_ints = str(ints) if ints > 0 else ''
    return str_ints + TXT_FRACTIONS[quarter]


# units in ml
ML_SPOON = 15 # one spoon contains 15 ml
ML_TEASPOON = 5 # one teaspoon contains 5 ml
ML_CUP = 240 # one cup contains 240 ml

def unit2ml(amount: float, unit: str) -> float:
    if unit == UNIT_SPOONS:
        return round(amount * ML_SPOON, 1)
    elif unit == UNIT_TEASPOONS:
        return round(amount * ML_TEASPOON, 1)
    elif unit == UNIT_CUPS:
        return round(amount * ML_CUP, 1)
    else:
        return 0
# average densities in gram per ml for common ingredients, to calculate weight(gram) from milliliters(ml)
# 1ml of salt weighs 1.2 gram 
GRAM_PER_ML_SALT = 1.2
GRAM_PER_ML_PEPPER = 0.3
GRAM_PER_ML_CHEESE = 0.45
GRAM_PER_ML_SPINACH = 0.15

# returns amount in gram for amount in milliliter based on density (weight per volume)
def ml2gram(amount_ml: float, gram_per_ml: float) -> float:
  return amount_ml * gram_per_ml

