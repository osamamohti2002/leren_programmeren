def round_to_nearest_5_cents(prijs):
    VIJF_CENT_STUIVER = 5
    return round(prijs * 100 / VIJF_CENT_STUIVER) *  VIJF_CENT_STUIVER / 100


original_amount = 2.24
rounded_amount = round_to_nearest_5_cents(original_amount)
print(rounded_amount)  

original_amount = 13.01
rounded_amount = round_to_nearest_5_cents(original_amount)
print(rounded_amount)  


original_amount = 69.69
rounded_amount = round_to_nearest_5_cents(original_amount)
print(rounded_amount)  

original_amount = 41.73
rounded_amount = round_to_nearest_5_cents(original_amount)
print(rounded_amount)  



original_amount = 0.09
rounded_amount = round_to_nearest_5_cents(original_amount)
print(rounded_amount)  

original_amount = 0.01
rounded_amount = round_to_nearest_5_cents(original_amount)
print(rounded_amount)  
