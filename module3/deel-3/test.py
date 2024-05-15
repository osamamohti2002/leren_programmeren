# def str_single_plural(amount: float, txt: str) -> str:
#     splits_txt = txt.split()
#     if amount <= 1:
#         txt = splits_txt[0], splits_txt[1]
#     else:
#         txt = splits_txt[-1]
#     return txt

# TXT_GARLICS = 'teentje knoflook | teentjes knoflook'

# resultaat = str_single_plural(1, TXT_GARLICS)
# print("Uitkomst:", resultaat)  # Output: teentje




# TXT_GARLICS = 'teentje knoflook | teentjes knoflook'
# TXT_TEASPOONS = 'theelepel | theelepels'
# lepel = 'eetlepel | eetlepels'
# print(str_single_plural(1,TXT_GARLICS))  # Output: appel
# print(str_single_plural(3,TXT_TEASPOONS))  # Output: appel peren bananen


TXT_FRACTIONS = ('','¼','½','¾')

def round_quarter(amount: float) -> float:
    if amount > 10:
        return round(amount)
    else:
        if amount < 0.25:
            return 0.25
        remainder = amount % 0.25
        if remainder < 0.125:
            return amount - remainder
        else:
            return amount + (0.25 - remainder)

def str_amount_fraction(amount: float) -> str:
    amount = round_quarter(amount)
    ints = int(amount)
    quarter = int((amount - ints) / 0.25)
    str_ints = str(ints) if ints > 0 else ''
    return str_ints + TXT_FRACTIONS[quarter]

# Example usage
print(str_amount_fraction(1.37))  # Output: '1¼'
print(str_amount_fraction(0.5))   # Output: '½'
print(str_amount_fraction(2.75))  # Output: '2¾'
print(str_amount_fraction(0.0))   # Output: '¼'
print(str_amount_fraction(10.4))  # Output: '10'
