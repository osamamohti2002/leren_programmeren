from test_lib import *
from recipe_lib import *


# test round piece
expected = 4
result = round_piece(3.4)
test(f'test round piece', expected, result)


expected = 8
result = round_piece(3.4)
test(f'test round piece', expected, result)


expected = 4
result = round_piece(4)
test(f'test round piece', expected, result)


# eind test round piece




# test round_quarter 
expected = 0.25
result = round_quarter(0.21)
test(f'test round quarter', expected, result)


expected = 0.75
result = round_quarter(0.70)
test(f'test round quarter', expected, result)


expected = 0.50
result = round_quarter(0.45)
test(f'test round quarter', expected, result)


expected = 1.0
result = round_quarter(0.90)
test(f'test round quarter', expected, result)

# eind test round_quarter 


# test str_single_plural
expected = "teentje knoflook"
result = str_single_plural(1, "teentje knoflook|teentjes knoflook")
test('test str_single_plural with 1 apple', expected, result)

expected = "kleine ui"
result = str_single_plural(1, 'kleine ui|kleine uien')
test('test str_single_plural with 1 apple', expected, result)

expected = "groot ei"
result = str_single_plural(4, "groot ei|grote eieren")
test('test str_single_plural with 1 apple', expected, result)

expected = "teentjes knoflook"
result = str_single_plural(1, "teentje knoflook|teentjes knoflook")
test('test str_single_plural with 1 apple', expected, result)

# eind test str_single_plural 





report()