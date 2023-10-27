# example:
def increment(nr2: float) -> float:
  return nr2 + 1

def decrement(nr2: float) -> float:
  return nr2 - 1

def add(nr1: float, nr2: float) -> float:
  return nr1 + nr2

def substract(nr2: float, nr1: float) -> float:
  return nr2 - nr1

def multiply(nr1: float, nr2: float) -> float:
  return nr1 * nr2

def divide(nr1: float, nr2: float) -> float:
  try:
    if nr2 == 0:
        return None
    result = nr1 / nr2
    return result
  except ZeroDivisionError:
    return "Error: Division by zero is not allowed."
 