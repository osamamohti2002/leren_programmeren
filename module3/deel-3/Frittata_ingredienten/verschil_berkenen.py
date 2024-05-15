import string
def str_single_plural(amount: float, txt: str) -> str:
    splits_txt = string.split(txt)
    if amount <= 1:
      txt = splits_txt[0]





str_single_plural(1.2, 'kopje|kopjes')