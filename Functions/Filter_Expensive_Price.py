prices=[100,250,400,1200,50,2000,850]
greater_than_500 = list(filter(lambda x: x > 500, prices))
less_than_equal_500 = list(filter(lambda x: x <= 500, prices))
print("Prices greater than 500:", greater_than_500)
print("Prices less than or equal to 500:", less_than_equal_500)