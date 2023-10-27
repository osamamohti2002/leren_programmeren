from test_lib import test,report


def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    MONTH_DISCOUNT_PERC = 10

    discount_brands = month_discount_brands.split(',')
    
    if brand in discount_brands:
        return round((price * MONTH_DISCOUNT_PERC) / 100, 2)  
    else:
        return 0.0  


month_discount_brands = 'Vespa,Kymco,Yamaha'
price = 550.25
brand = 'Vespa'
discount = calc_discount(price, brand, month_discount_brands)
test("Test 1", 55.02, discount)  

brand = 'Piaggio'
discount = calc_discount(price, brand, month_discount_brands)
test("Test 2", 0.0, discount)  

price = 999.99
brand = 'Yamaha'
discount = calc_discount(price, brand, month_discount_brands)
test("Test 3", 100.00, discount) 

prijs = 999.99
brand = 'Kymco'
discount = calc_discount(price, brand, month_discount_brands)
test("Test 4", 100.00, discount)  

brand = 'Suzuki'
discount = calc_discount(price, brand, month_discount_brands)
test("Test 5", 0.0, discount) 

report()
